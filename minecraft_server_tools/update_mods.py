import os
import sys
import json
import subprocess
import traceback
import datetime
import time
from urllib.parse import quote_plus
from pprint import pprint

import requests

from minecraft_server_tools import sync_mods
from minecraft_server_tools.constants import (
    COMMENT_JSON,
    MC_VERSION,
    COMPONENT_SEPS,
    NON_NAME_COMPONENT_REGEX,
    NAME_REGEXES_TO_SPACE,
    SEARCH_URL_TEMPLATE,
    SECRETS,
    GOOGLE_QUERY_TEMPLATE,
    NON_CURSEFORGE_MODS,
    MODLOADER,
    WRONG_MODLOADERS,
    MOD_PAGE_NAME_SUFFIX,
    CURSEFORGE_NAMES_FILE,
    CURSEFORGE_API_FILE,
    TIMESTAMP_FORMAT_REGEX,
    UPDATED_MODS_DIR_SUFFIX,
    OLD_MODS_DIR_SUFFIX,
    DEBUG,
    MAX_DEBUG_RESULTS,
    CURSEFORGE_NAME_ELEMS_TO_STRIP,
    CURSEFORGE_QUERY_TEMPLATES,
    ALWAYS_USE_LATEST_VERSION_FOR_MODS,
    CURSEFORGE_API_RETRIES,
    CURSEFORGE_API_RETRY_DELAY,
    PREFER_TWO_NUM_VER_TO_WRONG_THREE_NUM,
    ver_join,
    ver_split,
)


def google(query):
    print(f"Sending google search query {query!r}...")
    return requests.get(SEARCH_URL_TEMPLATE.format(
        google_api_key=SECRETS["google_api_key"],
        search_engine_id=SECRETS["search_engine_id"],
        query=quote_plus(query),
    )).json()


def get_mod_name(jar_name, silent=False):
    base_name = jar_name.removesuffix(".jar")
    for sep, min_count in COMPONENT_SEPS:
        components = base_name.split(sep)
        if len(components) > min_count:
            break
    else:
        if not silent:
            print(f"Failed to find components for jar {jar_name!r}.")
        components = [base_name]
    name_cmpnts = []
    for cmpnt in components:
        is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None
        if is_name_cmpnt:
            name_cmpnts.append(cmpnt)
        elif name_cmpnts:
            break
    if not name_cmpnts:
        if not silent:
            print(f"Failed to find name component for jar {jar_name!r}.")
        name_cmpnts = [components[0]]
    mod_name = " ".join(name_cmpnts)
    for to_space in NAME_REGEXES_TO_SPACE:
        mod_name = to_space.sub(" ", mod_name)
    mod_name = mod_name.strip()
    if not silent:
        print(f"Determined mod name {mod_name!r} for jar {jar_name!r}.")
    return mod_name


def get_curseforge_name(mod_name, jar_name):
    if mod_name in NON_CURSEFORGE_MODS:
        return None
    query = GOOGLE_QUERY_TEMPLATE.format(
        mod_name=mod_name,
        jar_name=jar_name,
        modloader=MODLOADER,
        mc_version=ver_join(MC_VERSION),
        mc_version_2=ver_join(MC_VERSION[:2]),
        mod_page_name_suffix=MOD_PAGE_NAME_SUFFIX,
    )
    try:
        while True:
            search_json = google(query)
            if "items" in search_json:
                break
            print(f"Got no results for query {query!r}.")
            if search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":
                raise Exception("Google API rate limit exceeded; try waiting or switching API keys.")
            query = search_json["spelling"]["correctedQuery"]
        items = search_json["items"]
        curseforge_name = None
        for result in items:
            mod_page = result["title"]
            if mod_page.lower().endswith(MOD_PAGE_NAME_SUFFIX.lower()):
                curseforge_name = clean_curseforge_name(mod_page[:-len(MOD_PAGE_NAME_SUFFIX)])
                break
            else:
                print(f"Skipping search result {mod_page!r}.")
        if curseforge_name is None:
            print(f"Could not find curseforge name for mod {mod_name!r} in results for query {query!r}:")
            pprint(items[:MAX_DEBUG_RESULTS])
            raise IOError(f"Could not find curseforge name for mod {mod_name!r}.")
        else:
            print(f"Found Curseforge name {curseforge_name!r} for mod {mod_name!r}.")
            return curseforge_name
    except (KeyError, IndexError):
        print(f"ERROR: Invalid search results for query {query!r}:")
        pprint(search_json)
        raise


def clean_curseforge_name(curseforge_name):
    old_curseforge_name = None
    while old_curseforge_name != curseforge_name:
        old_curseforge_name = curseforge_name
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:
            if curseforge_name.startswith(strip_str):
                curseforge_name = curseforge_name[len(strip_str):]
            if curseforge_name.endswith(strip_str):
                curseforge_name = curseforge_name[:-len(strip_str)]
        curseforge_name = curseforge_name.strip()
    return curseforge_name


def load_curseforge_names():
    if os.path.exists(CURSEFORGE_NAMES_FILE):
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:
            return COMMENT_JSON.load(ids_fobj)
    else:
        return {}


def save_curseforge_names(mod_names_to_curseforge_names):
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)


def get_curseforge_names_for(mod_names_to_jar_names):
    all_mod_names_to_curseforge_names = load_curseforge_names()
    found_curseforge_names_to_mod_names = {}
    try:
        for mod_name in mod_names_to_jar_names:
            if mod_name not in all_mod_names_to_curseforge_names:
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name])

                # do validation
                if curseforge_name in found_curseforge_names_to_mod_names:
                    raise ValueError(f"resolved multiple mod names to curseforge name {curseforge_name!r}: {found_curseforge_names_to_mod_names[curseforge_name]} and {mod_name}")
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name
    finally:
        save_curseforge_names(all_mod_names_to_curseforge_names)

    # get nulled mods
    requested_mod_names_to_curseforge_names = {}
    nulled_mods = []
    for mod_name in mod_names_to_jar_names:
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]
        if curseforge_name is None:
            nulled_mods.append(mod_name)
            print(f"Skipping mod {mod_name!r} due to explicitly nulled CurseForge name.")
        else:
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name
    return requested_mod_names_to_curseforge_names, nulled_mods


def get_jar_names(mods_dir):
    for fname in os.listdir(mods_dir):
        if fname.endswith(".jar"):
            yield fname


def get_mod_names_to_jar_names(mods_dir, silent=False):
    mod_names_to_jar_names = {}
    for jar_name in get_jar_names(mods_dir):
        mod_name = get_mod_name(jar_name, silent=silent)
        if mod_name in mod_names_to_jar_names:
            raise ValueError(f"resolved multiple jars to name {mod_name!r}: {mod_names_to_jar_names[mod_name]} and {jar_name}")
        mod_names_to_jar_names[mod_name] = jar_name
    return mod_names_to_jar_names


def run_curseforge_api_cmd(cmd):
    cmd = [str(x) for x in cmd]
    for _ in range(CURSEFORGE_API_RETRIES):
        print(f"Executing curseforge api cmd: {cmd!r}")
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)
        if cmd_result.stderr:
            print(f"\tcurseforge api cmd {cmd!r} failed: {cmd_result.stderr.decode('utf-8')}")
            time.sleep(CURSEFORGE_API_RETRY_DELAY)
        else:
            break
    else:
        raise Exception(f"Curseforge api cmd {cmd!r} failed {CURSEFORGE_API_RETRIES} times.")
    api_result = cmd_result.stdout.decode("utf-8")
    if not api_result:
        print("\tGot no output from curseforge api.")
        return []
    try:
        return json.loads(api_result)
    except json.decoder.JSONDecodeError:
        print("\nERROR: Could not parse curseforge api output:")
        print(api_result)
        raise


def has_bad_modloader(name):
    return (
        MODLOADER.lower() not in name.lower()
        and any(m.lower() in name.lower() for m in WRONG_MODLOADERS)
    )


def get_matching_mod(results, curseforge_name, mod_name):
    found_mod = None
    valid_modloader_results = []
    for mod in results:
        valid_modloader = not has_bad_modloader(mod["name"])
        if mod["name"] == curseforge_name:
            if not valid_modloader:
                print(f"\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {curseforge_name}")
            found_mod = mod
            break
        if valid_modloader:
            valid_modloader_results.append(mod)
    if found_mod is None:
        for mod in valid_modloader_results:
            if mod["name"].startswith(curseforge_name):
                found_mod = mod
                break
    if found_mod is None:
        for mod in valid_modloader_results:
            if curseforge_name in mod["name"]:
                found_mod = mod
                break
    if found_mod is None:
        slug_name = mod_name.replace(" ", "").lower()
        for mod in valid_modloader_results:
            if mod["slug"].replace("-", "").lower() == slug_name:
                found_mod = mod
                break
    if found_mod is None:
        core_curseforge_name = get_core_name(curseforge_name)
        if core_curseforge_name:
            for mod in valid_modloader_results:
                if core_curseforge_name in mod["name"]:
                    found_mod = mod
                    break
    if found_mod is not None and found_mod["name"] != curseforge_name:
        print(f"\tWARNING: found Curseforge mod with different name: {curseforge_name!r} -> {found_mod['name']!r}")
    return found_mod


def log_curseforge_results(results, verbose=False):
    if verbose:
        pprint(results[:MAX_DEBUG_RESULTS])
    else:
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])


def get_core_name(name):
    return get_mod_name(name, silent=True)


def get_curseforge_mod(curseforge_name, mod_name):
    core_curseforge_name = get_core_name(curseforge_name)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:
        query = query_template.format(
            curseforge_name=curseforge_name,
            core_curseforge_name=core_curseforge_name,
            mod_name=mod_name,
        )

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)
        if mod is not None:
            return mod
        if DEBUG:
            print(f"\tCould not find mod {curseforge_name!r} in modloader-version-specific results for query {query!r}.")

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)
        if mod is not None:
            return mod
        if DEBUG:
            print(f"\tCould not find mod {curseforge_name!r} in modloader-compatibly-versioned results for query {query!r}.")

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])
        mod = get_matching_mod(version_results, curseforge_name, mod_name)
        if mod is not None:
            return mod
        if DEBUG:
            print(f"\tCould not find mod {curseforge_name!r} in version-specific results for query {query!r}.")

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)
        if mod is not None:
            return mod
        if DEBUG:
            print(f"\tCould not find mod {curseforge_name!r} in compatibly-versioned results for query {query!r}.")

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)
        if mod is not None:
            return mod
        if DEBUG:
            print(f"\tCould not find mod {curseforge_name!r} in modloader-versioned results for query {query!r}.")

        versionless_results = run_curseforge_api_cmd(["search", query])
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)
        if mod is not None:
            return mod
        if DEBUG:
            print(f"\tCould not find mod {curseforge_name!r} in version-less results for query {query!r}.")

    print(f"\nERROR: Failed to find mod {curseforge_name!r} in any results.\n")


def get_curseforge_id(curseforge_name, mod_name):
    mod = get_curseforge_mod(curseforge_name, mod_name)
    if mod is not None:
        return mod["id"]


def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):
    mod_names_to_curseforge_ids = {}
    missing_mods = []
    for mod_name, curseforge_name in mod_names_to_curseforge_names.items():
        curseforge_id = get_curseforge_id(curseforge_name, mod_name)
        if curseforge_id is None:
            missing_mods.append(mod_name)
        else:
            mod_names_to_curseforge_ids[mod_name] = curseforge_id
    return mod_names_to_curseforge_ids, missing_mods


def get_curseforge_files(curseforge_id):
    return run_curseforge_api_cmd(["getfiles", curseforge_id])


def get_time_from_timestamp(timestamp):
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)
    if match_results is None:
        raise ValueError(f"failed to parse timestamp {timestamp!r}")
    return datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))


def timestamp_sort(curseforge_files):
    return sorted(curseforge_files, key=lambda f: get_time_from_timestamp(f["fileDate"]), reverse=True)


def get_max_version(versions):
    ver_tuples = []
    for ver_str in versions:
        try:
            ver_tuples.append(ver_split(ver_str))
        except ValueError:
            pass
    return max(ver_tuples)


def sort_releases(curseforge_files, mod_name):
    return sorted(curseforge_files, key=lambda f: (
        get_max_version(f["gameVersions"]),
        (
            0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS
            else -f["releaseType"]
        ),
        get_time_from_timestamp(f["fileDate"]),
    ), reverse=True)


def best_release(curseforge_files, mod_name):
    return sort_releases(curseforge_files, mod_name)[0]


def get_jar_name_for_curseforge_file(curseforge_file):
    url = curseforge_file["downloadUrl"]
    if url is None:
        raise ValueError("got invalid downloadUrl in: " + repr(curseforge_file))
    return url.rsplit("/", 1)[-1]


def correct_modloader(versions, jar_name):
    versions = [v.lower() for v in versions]

    if MODLOADER.lower() in versions:
        return True
    if any(wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS):
        return False

    jar_name = jar_name.lower()
    if MODLOADER.lower() in jar_name:
        return True
    if any(wrong_modloader.lower() in jar_name for wrong_modloader in WRONG_MODLOADERS):
        return False

    return True


def get_latest_version(mod_name, curseforge_id):
    curseforge_files = get_curseforge_files(curseforge_id)

    curseforge_files_and_versions = []
    for file_data in curseforge_files:
        versions = file_data["gameVersions"]
        if (
            file_data["downloadUrl"] is not None
            and correct_modloader(versions, get_jar_name_for_curseforge_file(file_data))
        ):
            curseforge_files_and_versions.append((file_data, versions))

    correctly_versioned_files = []
    for file_data, versions in curseforge_files_and_versions:
        if ver_join(MC_VERSION) in versions:
            correctly_versioned_files.append(file_data)
    if correctly_versioned_files:
        return best_release(correctly_versioned_files, mod_name)
    print(f"No correctly versioned files found for mod {mod_name!r}.")

    if PREFER_TWO_NUM_VER_TO_WRONG_THREE_NUM:
        two_num_ver_files = []
        for file_data, versions in curseforge_files_and_versions:
            if ver_join(MC_VERSION[:2]) in versions:
                two_num_ver_files.append(file_data)
        if two_num_ver_files:
            return best_release(two_num_ver_files, mod_name)

    compatibly_versioned_files = []
    for file_data, versions in curseforge_files_and_versions:
        for ver in versions:
            if ver.startswith(ver_join(MC_VERSION[:2])):
                compatibly_versioned_files.append(file_data)
                break
    if compatibly_versioned_files:
        return best_release(compatibly_versioned_files, mod_name)
    print(f"No compatibly versioned files found for mod {mod_name!r} in:")
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])


def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids):
    mod_names_to_latest_versions = {}
    missing_mods = []
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():
        latest_version = get_latest_version(mod_name, curseforge_id)
        if latest_version is None:
            missing_mods.append(mod_name)
        else:
            mod_names_to_latest_versions[mod_name] = latest_version
    return mod_names_to_latest_versions, missing_mods


def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):
    updated_mod_names_to_files = {}
    for mod_name, latest_file in mod_names_to_latest_versions.items():
        old_jar = mod_names_to_jar_names[mod_name]
        new_jar = get_jar_name_for_curseforge_file(latest_file)
        if new_jar.replace(" ", "+") != old_jar.replace(" ", "+"):
            updated_mod_names_to_files[mod_name] = latest_file
    return updated_mod_names_to_files


def download_file(curseforge_file, updated_mods_dir, mod_name):
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)
    url = curseforge_file["downloadUrl"]
    new_jar_path = os.path.join(updated_mods_dir, jar_name)
    if not os.path.exists(new_jar_path):
        print(f"Downloading {jar_name}...")
        new_mod_name = get_mod_name(jar_name, silent=True)
        if new_mod_name != mod_name:
            print(f"\tWARNING: new mod name: {mod_name!r} -> {new_mod_name!r}")
        result = requests.get(url)
        with open(new_jar_path, "wb") as jar_fobj:
            jar_fobj.write(result.content)


def update_files(updated_mod_names_to_files, updated_mods_dir):
    seen_jar_names = {}
    for mod_name, curseforge_file in updated_mod_names_to_files.items():
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)
        if jar_name in seen_jar_names:
            print(f"\tWARNING: resolved multiple mod names to same jar name {jar_name!r}: {seen_jar_names[jar_name]!r} and {mod_name!r}")
        else:
            seen_jar_names[jar_name] = mod_name
        download_file(curseforge_file, updated_mods_dir, mod_name)


def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):
    for mod_name in updated_mod_names_to_files:
        jar_name = mod_names_to_jar_names[mod_name]
        current_jar_path = os.path.join(mods_dir, jar_name)
        new_jar_path = os.path.join(old_mods_dir, jar_name)
        os.rename(current_jar_path, new_jar_path)


def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None):
    if interact is None and not DEBUG:
        interact = False
    try:
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names)
        if not dry_run:
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)
            if updated_mod_names_to_files:
                if not os.path.exists(updated_mods_dir):
                    os.mkdir(updated_mods_dir)
                if not os.path.exists(old_mods_dir):
                    os.mkdir(old_mods_dir)
                update_files(updated_mod_names_to_files, updated_mods_dir)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)
        else:
            missing_ids_mods = []
            missing_files_mods = []
        return nulled_mods + missing_ids_mods + missing_files_mods
    except Exception:
        if interact is not False:
            traceback.print_exc()

            from coconut import embed
            embed()
        raise
    if interact:
        from coconut import embed
        embed()


def update_all(mods_dirs, dry_run=False, interact=None):
    couldnt_update = []
    for mods_dir in mods_dirs:
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact)
    for mod_name in couldnt_update:
        print(f"Unable to automatically update mod: {mod_name}")


def main():
    sync_mods.main()

    update_all(
        [
            sync_mods.EXTRA_CLIENT_MODS_DIR,
            sync_mods.EXTRA_MODS_DIR,
            sync_mods.BASE_CLIENT_MODS_DIR,
            sync_mods.BASE_MODS_DIR,
        ],
        dry_run="--dry-run" in sys.argv,
    )

    # from coconut import embed
    # embed()


if __name__ == "__main__":
    main()
