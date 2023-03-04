import os

from minecraft_server_tools import (
    sync_mods,
    update_mods,
    deduplicate_mods,
)
from minecraft_server_tools.constants import (
    UPDATED_MODS_DIR_SUFFIX,
    OLD_MODS_DIR_SUFFIX,
)


def update_mods_from(update_from_dir, mods_dir):
    names_to_jars_mods = update_mods.get_mod_names_to_jar_names(mods_dir, silent=True)
    names_to_jars_update_from = update_mods.get_mod_names_to_jar_names(update_from_dir, silent=True)

    updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX
    old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX

    made_dirs = False
    for name, mods_jar in names_to_jars_mods.items():
        update_jar = names_to_jars_update_from.get(name)
        if update_jar is not None and mods_jar != update_jar:
            if not made_dirs:
                update_mods.make_dirs(updated_mods_dir, old_mods_dir)
                made_dirs = True

            print(f"{mods_jar} -> {update_jar}")
            current_jar_path = os.path.join(mods_dir, mods_jar)
            old_jar_path = os.path.join(old_mods_dir, mods_jar)
            os.rename(current_jar_path, old_jar_path)

            update_from_jar_path = os.path.join(update_from_dir, update_jar)
            updates_jar_path = os.path.join(updated_mods_dir, update_jar)
            os.rename(update_from_jar_path, updates_jar_path)


def main():
    sync_mods.main()

    update_mods_from(deduplicate_mods.DEDUPLICATE_CLIENT_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR)
    update_mods_from(deduplicate_mods.DEDUPLICATE_CLIENT_MODS_DIR, sync_mods.EXTRA_CLIENT_MODS_DIR)

    update_mods_from(deduplicate_mods.DEDUPLICATE_MODS_DIR, sync_mods.BASE_MODS_DIR)
    update_mods_from(deduplicate_mods.DEDUPLICATE_MODS_DIR, sync_mods.EXTRA_MODS_DIR)


if __name__ == "__main__":
    main()
