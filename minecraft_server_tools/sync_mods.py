from __future__ import print_function

import os
import shutil

from minecraft_server_tools.constants import (
    SERVER_DIR,
    MODS_NAME,
    BASE_MODS_NAME,
    EXTRA_MODS_NAME,
    REMOVED_MODS_NAME,
    CLIENT_MODS_NAME,
    BASE_CLIENT_MODS_NAME,
    EXTRA_CLIENT_MODS_NAME,
    REMOVED_CLIENT_MODS_NAME,
    BINARY_SEARCH_FILE,
    load_json,
)

MODS_DIR = os.path.join(SERVER_DIR, MODS_NAME)
BASE_MODS_DIR = os.path.join(SERVER_DIR, BASE_MODS_NAME)
EXTRA_MODS_DIR = os.path.join(SERVER_DIR, EXTRA_MODS_NAME)
REMOVED_MODS_DIR = os.path.join(SERVER_DIR, REMOVED_MODS_NAME)
CLIENT_MODS_DIR = os.path.join(SERVER_DIR, CLIENT_MODS_NAME)
BASE_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, BASE_CLIENT_MODS_NAME)
EXTRA_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, EXTRA_CLIENT_MODS_NAME)
REMOVED_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, REMOVED_CLIENT_MODS_NAME)


def ensure_dirs():
    for dirpath in [
        MODS_DIR,
        EXTRA_MODS_DIR,
        CLIENT_MODS_DIR,
        EXTRA_CLIENT_MODS_DIR,
    ]:
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)


def get_location_table_for(mods_dir):
    mod_location_table = {}
    if os.path.exists(mods_dir):
        for name in os.listdir(mods_dir):
            path = os.path.join(mods_dir, name)
            if os.path.isfile(path):
                assert name not in mod_location_table, f"found duplicate mod file at both {mod_location_table[name]!r} and {path!r}"
                mod_location_table[name] = path
    return mod_location_table


def display_mod_path(mod_path):
    mod_dir, mod_name = os.path.split(mod_path)
    _, mod_dir_name = os.path.split(mod_dir)
    return os.path.join(mod_dir_name, mod_name)


def rm_mod(path):
    print("Removing {mod}...".format(mod=display_mod_path(path)))
    os.remove(path)


def remove_mods_in_from(remove_mod_location_table, current_mod_location_table):
    for mod, cur_path in current_mod_location_table.items():
        if mod in remove_mod_location_table and os.path.exists(cur_path):
            rm_mod(cur_path)


def add_mod(from_path, to_path):
    print("Adding {mod} from {src}...".format(mod=display_mod_path(to_path), src=display_mod_path(from_path)))
    os.makedirs(os.path.dirname(to_path), exist_ok=True)
    shutil.copy(from_path, to_path)


def set_mods_from_to(target_mod_location_table, current_mod_location_table, set_mods_dir):
    for mod, cur_path in current_mod_location_table.items():
        if mod not in target_mod_location_table and os.path.exists(cur_path):
            print("Removing {mod}...".format(mod=display_mod_path(cur_path)))
            os.remove(cur_path)
    add_mods_from_to(target_mod_location_table, current_mod_location_table, set_mods_dir)


def add_mods_from_to(target_mod_location_table, current_mod_location_table, set_mods_dir):
    for mod, tar_path in target_mod_location_table.items():
        if mod not in current_mod_location_table:
            new_path = os.path.join(set_mods_dir, mod)
            add_mod(tar_path, new_path)


def load_binary_search_file():
    return load_json(BINARY_SEARCH_FILE, {
        "searching": False,
    })


def get_sorted_location_table_items_for(folder):
    return list(sorted(get_location_table_for(folder).items()))


def get_binary_search_location_table(binary_search):
    folder_a = binary_search["folder_a"]
    folder_b = binary_search["folder_b"]

    mods_a = get_sorted_location_table_items_for(folder_a)
    mods_b = get_sorted_location_table_items_for(folder_b)
    assert len(mods_a) == len(mods_b), f"{len(mods_a)} != {len(mods_b)} ({folder_a}, {folder_b})"

    num_a = binary_search["num_a"]

    new_mods = dict(mods_a[:num_a] + mods_b[num_a:])
    assert len(new_mods) == len(mods_a), f"{len(new_mods)} != {len(mods_a)}"
    return new_mods


def main():
    ensure_dirs()

    print("\nFixing client only mods...")
    extra_server_mods = get_location_table_for(EXTRA_MODS_DIR)
    extra_client_only_mods = get_location_table_for(EXTRA_CLIENT_MODS_DIR)

    remove_mods_in_from(extra_server_mods, extra_client_only_mods)

    base_server_mods = get_location_table_for(BASE_MODS_DIR)
    base_client_only_mods = get_location_table_for(BASE_CLIENT_MODS_DIR)

    remove_mods_in_from(base_server_mods, base_client_only_mods)


    print("\nFixing main mods...")
    all_base_mods = get_location_table_for(BASE_MODS_DIR)
    all_base_mods.update(get_location_table_for(BASE_CLIENT_MODS_DIR))

    extra_server_mods = get_location_table_for(EXTRA_MODS_DIR)
    extra_client_only_mods = get_location_table_for(EXTRA_CLIENT_MODS_DIR)

    remove_mods_in_from(all_base_mods, extra_server_mods)
    remove_mods_in_from(all_base_mods, extra_client_only_mods)

    remove_mods_in_from(extra_server_mods, extra_client_only_mods)


    print("\nMerging server mods...")
    all_server_mods = get_location_table_for(BASE_MODS_DIR)
    all_server_mods.update(get_location_table_for(EXTRA_MODS_DIR))

    current_server_mods = get_location_table_for(MODS_DIR)

    set_mods_from_to(all_server_mods, current_server_mods, MODS_DIR)


    print("\nMerging client only mods...")
    all_client_only_mods = get_location_table_for(BASE_CLIENT_MODS_DIR)
    all_client_only_mods.update(get_location_table_for(EXTRA_CLIENT_MODS_DIR))

    current_client_only_mods = get_location_table_for(CLIENT_MODS_DIR)

    set_mods_from_to(all_client_only_mods, current_client_only_mods, CLIENT_MODS_DIR)


    print("\nFixing removed mods...")
    removed_server_mods = get_location_table_for(REMOVED_MODS_DIR)
    remove_mods_in_from(all_server_mods, removed_server_mods)

    removed_client_mods = get_location_table_for(REMOVED_CLIENT_MODS_DIR)
    remove_mods_in_from(removed_server_mods, removed_client_mods)
    remove_mods_in_from(all_server_mods, removed_client_mods)
    remove_mods_in_from(all_client_only_mods, removed_client_mods)


    binary_search = load_binary_search_file()
    if binary_search["searching"]:

        print("\nAdding mods from binary search...")
        binary_search_mods = get_binary_search_location_table(binary_search)

        destination_dir = binary_search["destination"]
        destination_mods = get_location_table_for(destination_dir)

        add_mods_from_to(binary_search_mods, destination_mods, destination_dir)



if __name__ == "__main__":
    main()
