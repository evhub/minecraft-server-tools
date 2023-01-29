import os
import sys
import shutil
import zipfile
import tempfile
import json
from contextlib import contextmanager

from tqdm import tqdm

from minecraft_server_tools import sync_mods, launch_server
from minecraft_server_tools.constants import (
    WINDOWS,
    SERVER_DIR,
    MINECRAFT_DIR,
    EXTRA_INSTALL_FOLDERS,
    EXTRA_INSTALL_FILES,
    FORGE_INSTALLER_JAR,
    README_FILE,
    MOD_ZIP_PATH,
    OPTIONAL_INSTALL_FILES,
    OPTIONAL_INSTALL_FOLDERS,
    MODS_NAME,
    CLIENT_MODS_NAME,
    YES_STRS,
    PROFILES_FILE,
)

MINECRAFT_MODS_DIR = os.path.join(MINECRAFT_DIR, MODS_NAME)


def sync_client_mods(source_dir):
    print("\nInstalling mods...")
    all_client_mods = sync_mods.get_location_table_for(os.path.join(source_dir, MODS_NAME))
    all_client_mods.update(sync_mods.get_location_table_for(os.path.join(source_dir, CLIENT_MODS_NAME)))

    current_client_mods = sync_mods.get_location_table_for(MINECRAFT_MODS_DIR)

    sync_mods.set_mods_from_to(all_client_mods, current_client_mods, MINECRAFT_MODS_DIR)


def install_extras(source_dir, do_optional=True, clean=True):
    print("\nInstalling other files/folders...")
    for install_dir in EXTRA_INSTALL_FOLDERS + (OPTIONAL_INSTALL_FOLDERS if do_optional else []):
        from_dir = os.path.join(source_dir, install_dir)
        to_dir = os.path.join(MINECRAFT_DIR, install_dir)
        print(f"\t{install_dir}...")
        cleaned = False
        if clean and os.path.exists(to_dir):
            shutil.rmtree(to_dir)
            cleaned = True
        if os.path.exists(from_dir):
            shutil.copytree(from_dir, to_dir, dirs_exist_ok=True)
        elif cleaned:
            print("\t\t(cleaned)")
        else:
            print("\t\t(skipped)")

    for install_file in EXTRA_INSTALL_FILES + (OPTIONAL_INSTALL_FILES if do_optional else []):
        from_path = os.path.join(source_dir, install_file)
        to_path = os.path.join(MINECRAFT_DIR, install_file)
        print(f"\t{install_file}...")
        if os.path.exists(from_path):
            shutil.copy(from_path, to_path)
        else:
            print("\t\t(skipped)")


def ensure_forge_client(source_dir):
    if not os.path.exists(os.path.join(MINECRAFT_DIR, FORGE_INSTALLER_JAR)):
        print("\nOpening forge installer; select 'Install client' and press 'Ok'.")
        launch_server.run_java(["-jar", os.path.join(source_dir, FORGE_INSTALLER_JAR)])


def get_paths_to_zip():
    for install_fname in (
        EXTRA_INSTALL_FILES
        + OPTIONAL_INSTALL_FILES
    ):
        yield os.path.join(MINECRAFT_DIR, install_fname)
    for install_dirname in (
        EXTRA_INSTALL_FOLDERS
        + OPTIONAL_INSTALL_FOLDERS
        + [MODS_NAME]
    ):
        install_dirpath = os.path.join(MINECRAFT_DIR, install_dirname)
        for dirpath, dirnames, filenames in os.walk(install_dirpath):
            yield dirpath
            for fname in filenames:
                yield os.path.join(dirpath, fname)


def zip_mods():
    print(f"\nZipping mod files to {MOD_ZIP_PATH}...")
    with zipfile.ZipFile(MOD_ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for install_path in tqdm(list(get_paths_to_zip())):
            zf.write(install_path, os.path.relpath(install_path, MINECRAFT_DIR))


def set_jvm_args():
    print(f"\nSetting JVM arguments...")
    java_args = " ".join(launch_server.get_java_args(client=True))
    with open(PROFILES_FILE, "r+") as profiles_file:
        top_level_json = json.load(profiles_file)
        top_level_json["profiles"]["forge"]["javaArgs"] = java_args

        profiles_file.seek(0)
        profiles_file.truncate()
        json.dump(top_level_json, profiles_file, indent=2)
    print(f"\tto: {java_args}")


def open_readme():
    installed_readme = os.path.join(MINECRAFT_DIR, README_FILE)
    print(f"\nOpening {installed_readme}...")
    if WINDOWS:
        launch_server.run_cmd(["explorer", installed_readme], check=False)
    else:
        launch_server.run_cmd(["xdg-open", installed_readme], check=False)


@contextmanager
def unzipped_mods():
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"\nUnzipping mods to temporary directory {temp_dir!r}...")
        shutil.unpack_archive(MOD_ZIP_PATH, temp_dir)
        yield temp_dir


def install_from_dir(source_dir, do_optional=False):
    launch_server.clean_forge_jars(MINECRAFT_DIR)

    ensure_forge_client(source_dir)
    sync_client_mods(source_dir)
    install_extras(source_dir, do_optional)

    set_jvm_args()


def install_from_server():
    """Install from server and return whether or not to install optional files."""
    sync_mods.main()
    launch_server.start_server(dry_run=True)

    install_from_dir(SERVER_DIR, do_optional=True)

    zip_mods()
    return True


def install_from_zip():
    """Install from zip and return whether or not to install optional files."""
    if "--yes-optional" in sys.argv:
        do_optional = True
    elif "--no-optional" in sys.argv:
        do_optional = False
    else:
        do_optional = input(f"\nInstall optional files {OPTIONAL_INSTALL_FILES + OPTIONAL_INSTALL_FOLDERS}? [y/N] ").lower() in YES_STRS
    if do_optional:
        print("Will install optional files.")
    else:
        print("Will NOT install optional files.")
    with unzipped_mods() as temp_dir:
        install_from_dir(temp_dir, do_optional)
    return do_optional


def main():
    if os.path.exists(SERVER_DIR):
        print("\nInstalling from server...")
        return install_from_server()
    elif os.path.exists(MOD_ZIP_PATH):
        print("\nInstalling from zipfile...")
        return install_from_zip()
    else:
        raise IOError("Could not find files for install.")


if __name__ == "__main__":
    main()
