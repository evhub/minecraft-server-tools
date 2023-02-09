import os

from minecraft_server_tools import sync_mods, update_mods
from minecraft_server_tools.constants import (
    SERVER_DIR,
    DEDUPLICATE_MODS_NAME,
    DEDUPLICATE_CLIENT_MODS_NAME,
)


DEDUPLICATE_MODS_DIR = os.path.join(SERVER_DIR, DEDUPLICATE_MODS_NAME)
DEDUPLICATE_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, DEDUPLICATE_CLIENT_MODS_NAME)


def get_all_mod_names(mods_dirs):
    all_mod_names = {}
    for dirname in mods_dirs:
        if os.path.exists(dirname):
            for mod_name, jar_name in update_mods.get_mod_names_to_jar_names(dirname, silent=True).items():
                assert mod_name not in all_mod_names, f"found multiple jars with same mod name {mod_name!r}: {all_mod_names[mod_name]!r}, {jar_name!r}"
                all_mod_names[mod_name] = jar_name
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


def deduplicate_mods(new_mods_dir, all_mod_names):
    if os.path.exists(new_mods_dir):
        print(f"\nDeduplicating mods in: {new_mods_dir}")
        for mod_name, jar_name in update_mods.get_mod_names_to_jar_names(new_mods_dir).items():
            from_path = os.path.join(new_mods_dir, jar_name)
            if mod_name in all_mod_names:
                sync_mods.rm_mod(from_path)


def main():
    sync_mods.main()

    print("\nFixing to deduplicate mods...")
    sync_mods.remove_mods_in_from(
        sync_mods.get_location_table_for(DEDUPLICATE_MODS_DIR),
        sync_mods.get_location_table_for(DEDUPLICATE_CLIENT_MODS_DIR),
    )

    all_mod_names = get_all_mod_names([
        sync_mods.MODS_DIR,
        sync_mods.CLIENT_MODS_DIR,
        sync_mods.REMOVED_MODS_DIR,
        sync_mods.REMOVED_CLIENT_MODS_DIR,
    ])
    deduplicate_mods(DEDUPLICATE_CLIENT_MODS_DIR, all_mod_names)
    deduplicate_mods(DEDUPLICATE_MODS_DIR, all_mod_names)


if __name__ == "__main__":
    main()
