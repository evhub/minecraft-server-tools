import os

from minecraft_server_tools import sync_mods, update_mods
from minecraft_server_tools.constants import (
    SERVER_DIR,
    ADD_IF_NEW_MODS_NAME,
    ADD_IF_NEW_CLIENT_MODS_NAME,
)


ADD_IF_NEW_MODS_DIR = os.path.join(SERVER_DIR, ADD_IF_NEW_MODS_NAME)
ADD_IF_NEW_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, ADD_IF_NEW_CLIENT_MODS_NAME)


def get_all_mod_names(mods_dirs):
    all_mod_names = {}
    for mods_dir in mods_dirs:
        all_mod_names.update(update_mods.get_mod_names_to_jar_names(mods_dir, silent=True))
    return all_mod_names


def add_new_mods(new_mods_dir, to_mods_dir, all_mod_names):
    to_mods_dir_mod_names = update_mods.get_mod_names_to_jar_names(to_mods_dir, silent=True)
    made_changes = False
    if os.path.exists(new_mods_dir):
        print(f"\nLooking for new mods in: {new_mods_dir}")
        for mod_name, jar_name in update_mods.get_mod_names_to_jar_names(new_mods_dir).items():
            from_path = os.path.join(new_mods_dir, jar_name)
            if mod_name not in all_mod_names:
                to_path = os.path.join(to_mods_dir, jar_name)
                print(f"Adding new mod: {mod_name} (from {jar_name!r})")
                os.rename(from_path, to_path)
                made_changes = True
            elif mod_name in to_mods_dir_mod_names:
                sync_mods.rm_mod(from_path)
        if made_changes:
            sync_mods.main()
        else:
            print(f"Found no new mods in: {new_mods_dir}\n")
    else:
        print(f"\nSkipping adding new mods from: {new_mods_dir}\n")
    return made_changes


def main():
    sync_mods.main()

    all_mod_names = get_all_mod_names([
        sync_mods.MODS_DIR,
        sync_mods.CLIENT_MODS_DIR,
        sync_mods.REMOVED_MODS_DIR,
        sync_mods.REMOVED_CLIENT_MODS_DIR,
    ])
    add_new_mods(ADD_IF_NEW_CLIENT_MODS_DIR, sync_mods.EXTRA_CLIENT_MODS_DIR, all_mod_names)
    add_new_mods(ADD_IF_NEW_MODS_DIR, sync_mods.EXTRA_MODS_DIR, all_mod_names)


if __name__ == "__main__":
    main()
