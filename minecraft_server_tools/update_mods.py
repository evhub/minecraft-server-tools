import os
import json
import subprocess
import traceback
import datetime
from urllib.parse import quote_plus
from pprint import pprint

import requests

from minecraft_server_tools import sync_mods
from minecraft_server_tools.constants import (
    MC_VERSION,
    COMPONENT_SEPS,
    NON_NAME_COMPONENT_REGEX,
    NAME_ELEMS_TO_SPACE,
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
    MAX_DEBUG_RESULTS,
    EXTRA_CLIENT_MODS_DIR,
    EXTRA_MODS_DIR,
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


def get_mod_name(jar_name):
    assert jar_name.endswith(".jar")
    base_name = jar_name[:-len(".jar")]
    for sep, min_count in COMPONENT_SEPS:
        components = base_name.split(sep)
        if len(components) > min_count:
            break
    else:
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
        print(f"Failed to find name component for jar {jar_name!r}.")
        name_cmpnts = [components[0]]
    mod_name = " ".join(name_cmpnts)
    for to_space in NAME_ELEMS_TO_SPACE:
        mod_name = mod_name.replace(to_space, " ")
    mod_name = mod_name.strip()
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
    )
    search_json = google(query)
    i = 0
    while True:
        try:
            mod_page = search_json["items"][i]["title"]
        except (KeyError, IndexError):
            print(f"Invalid search results for query {query!r}:")
            pprint(search_json)
            raise
        if mod_page.lower().endswith(MOD_PAGE_NAME_SUFFIX):
            curseforge_name = clean_curseforge_name(mod_page[:-len(MOD_PAGE_NAME_SUFFIX)])
            print(f"Found Curseforge name {curseforge_name!r} for mod {mod_name!r}.")
            return curseforge_name
        else:
            print(f"Skipping search result {mod_page!r}.")
        i += 1


def clean_curseforge_name(curseforge_name):
    old_curseforge_name = None
    while old_curseforge_name != curseforge_name:
        old_curseforge_name = curseforge_name
        curseforge_name = curseforge_name.strip(" -")
        if curseforge_name.startswith("Files"):
            curseforge_name = curseforge_name[len("Files"):]
        if curseforge_name.endswith("Mods"):
            curseforge_name = curseforge_name[:-len("Mods")]
        if curseforge_name.endswith("..."):
            curseforge_name = curseforge_name[:-len("...")]
    return curseforge_name


def load_curseforge_names():
    if os.path.exists(CURSEFORGE_NAMES_FILE):
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:
            return json.load(ids_fobj)
    else:
        return {}


def save_curseforge_names(mod_names_to_curseforge_names):
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)


def get_curseforge_names_for(mod_names_to_jar_names):
    all_mod_names_to_curseforge_names = load_curseforge_names()
    try:
        for mod_name in mod_names_to_jar_names:
            if mod_name not in all_mod_names_to_curseforge_names:
                all_mod_names_to_curseforge_names[mod_name] = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name])
    finally:
        save_curseforge_names(all_mod_names_to_curseforge_names)
    requested_mod_names_to_curseforge_names = {}
    for mod_name in mod_names_to_jar_names:
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]
        if curseforge_name is None:
            print(f"Skipping mod {mod_name!r} due to explicitly nulled CurseForge name.")
        else:
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name
    return requested_mod_names_to_curseforge_names


def get_jar_names(mods_dir):
    for fname in os.listdir(mods_dir):
        if fname.endswith(".jar"):
            yield fname


def get_mod_names_to_jar_names(mods_dir):
    return {get_mod_name(jar_name): jar_name for jar_name in get_jar_names(mods_dir)}


def run_curseforge_api_cmd(cmd):
    cmd = [str(x) for x in cmd]
    print("Executing curseforge api cmd: " + " ".join(cmd))
    api_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True).stdout
    try:
        return json.loads(api_result)
    except json.decoder.JSONDecodeError:
        print("Could not parse curseforge api output:\n" + api_result)
        raise


def get_matching_mod(results, curseforge_name, allow_inexact_name=True):
    for mod in results:
        if mod["name"] == curseforge_name:
            return mod
    if allow_inexact_name:
        for mod in results:
            if mod["name"].startswith(curseforge_name) or mod["name"].endswith(curseforge_name):
                print(f"Found mod with different name {mod['name']!r} for mod {curseforge_name!r}.")
                return mod


def get_curseforge_mod(curseforge_name):
    version_results = run_curseforge_api_cmd(["search", curseforge_name, ver_join(MC_VERSION)])
    mod = get_matching_mod(version_results, curseforge_name, allow_inexact_name=False)
    if mod is not None:
        return mod
    print(f"Could not find mod {curseforge_name!r} in version-specific results.")

    versionless_results = run_curseforge_api_cmd(["search", curseforge_name])
    mod = get_matching_mod(versionless_results, curseforge_name)
    if mod is not None:
        return mod
    print(f"Could not find mod {curseforge_name!r} in version-less results:")
    pprint(versionless_results[:MAX_DEBUG_RESULTS])
    raise IOError(f"Could not find mod {curseforge_name!r}.")


def get_curseforge_id(curseforge_name):
    return get_curseforge_mod(curseforge_name)["id"]


def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):
    return {mod_name: get_curseforge_id(curseforge_name) for mod_name, curseforge_name in mod_names_to_curseforge_names.items()}


def get_curseforge_files(curseforge_id):
    return run_curseforge_api_cmd(["getfiles", curseforge_id])


def get_time_from_timestamp(timestamp):
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)
    if match_results is None:
        raise ValueError(f"failed to parse timestamp {timestamp!r}")
    return datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))


def timestamp_sort(curseforge_files):
    return sorted(curseforge_files, key=lambda f: get_time_from_timestamp(f["timestamp"]), reverse=True)


def get_max_version(versions):
    ver_tuples = []
    for ver_str in versions:
        try:
            ver_tuples.append(ver_split(ver_str))
        except ValueError:
            pass
    return max(ver_tuples)


def sort_releases(curseforge_files):
    return sorted(curseforge_files, key=lambda f: (
        get_max_version(f["minecraft_versions"]),
        -f["release_type"],
        get_time_from_timestamp(f["timestamp"]),
    ), reverse=True)


def best_release(curseforge_files):
    return sort_releases(curseforge_files)[0]


def get_latest_version(mod_name, curseforge_id):
    curseforge_files = get_curseforge_files(curseforge_id)

    curseforge_files_and_versions = []
    for file_data in curseforge_files:
        versions = [v.lower() for v in file_data["minecraft_versions"]]
        if not any(wrong_modloader in versions for wrong_modloader in WRONG_MODLOADERS):
            curseforge_files_and_versions.append((file_data, versions))

    correctly_versioned_files = []
    for file_data, versions in curseforge_files_and_versions:
        if ver_join(MC_VERSION) in versions:
            correctly_versioned_files.append(file_data)
    if correctly_versioned_files:
        return best_release(correctly_versioned_files)
    print(f"No correctly versioned files found for mod {mod_name!r}.")

    compatibly_versioned_files = []
    for file_data, versions in curseforge_files_and_versions:
        for ver in versions:
            if ver.startswith(ver_join(MC_VERSION[:-1])):
                compatibly_versioned_files.append(file_data)
                break
    if compatibly_versioned_files:
        return best_release(compatibly_versioned_files)
    print(f"No compatibly versioned files found for mod {mod_name!r} in:")
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])


def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids):
    mod_names_to_latest_versions = {}
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():
        latest_version = get_latest_version(mod_name, curseforge_id)
        if latest_version:
            mod_names_to_latest_versions[mod_name] = latest_version
    return mod_names_to_latest_versions


def get_jar_name_for_curseforge_file(curseforge_file):
    return curseforge_file["download_url"].rsplit("/", 1)[-1]


def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):
    updated_mod_names_to_files = {}
    for mod_name, latest_file in mod_names_to_latest_versions.items():
        old_jar = mod_names_to_jar_names[mod_name]
        new_jar = get_jar_name_for_curseforge_file(latest_file)
        if new_jar.replace(" ", "+") != old_jar.replace(" ", "+"):
            updated_mod_names_to_files[mod_name] = latest_file
    return updated_mod_names_to_files


def download_file(curseforge_file, updated_mods_dir):
    url = curseforge_file["download_url"]
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)
    if not os.path.exists(new_jar_path):
        print(f"Downloading {jar_name}...")
        result = requests.get(url)
        with open(new_jar_path, "wb") as jar_fobj:
            jar_fobj.write(result.content)


def update_files(updated_mod_names_to_files, updated_mods_dir):
    for curseforge_file in updated_mod_names_to_files.values():
        download_file(curseforge_file, updated_mods_dir)


def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):
    for mod_name in updated_mod_names_to_files:
        jar_name = mod_names_to_jar_names[mod_name]
        current_jar_path = os.path.join(mods_dir, jar_name)
        new_jar_path = os.path.join(old_mods_dir, jar_name)
        os.rename(current_jar_path, new_jar_path)


def update_mods(mods_dir, updated_mods_dir, old_mods_dir, interact=None):
    try:
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)
        mod_names_to_curseforge_names = get_curseforge_names_for(mod_names_to_jar_names)
        mod_names_to_curseforge_ids = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)
        mod_names_to_latest_versions = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids)
        updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)
        if updated_mod_names_to_files:
            if not os.path.exists(updated_mods_dir):
                os.mkdir(updated_mods_dir)
            if not os.path.exists(old_mods_dir):
                os.mkdir(old_mods_dir)
            update_files(updated_mod_names_to_files, updated_mods_dir)
            move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)
    except Exception:
        if interact is not False:
            traceback.print_exc()

            from coconut import embed
            embed()
        raise
    if interact:

        from coconut import embed
        embed()


def update_all(mods_dirs, interact=None):
    for mods_dir in mods_dirs:
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX
        update_mods(mods_dir, updated_mods_dir, old_mods_dir, interact=interact)


def main():
    sync_mods.main()

    update_all([
        EXTRA_CLIENT_MODS_DIR,
        EXTRA_MODS_DIR,
    ])

    # from coconut import embed
    # embed()


if __name__ == "__main__":
    main()
