import os
import shutil

from minecraft_server_tools import sync_mods, launch_server
from minecraft_server_tools.constants import (
    MODS_DIR,
    CLIENT_MODS_DIR,
    MINECRAFT_MODS_DIR,
    SERVER_DIR,
    MINECRAFT_DIR,
    EXTRA_INSTALL_FOLDERS,
    EXTRA_INSTALL_FILES,
    FORGE_INSTALLER_JAR,
    FORGE_INSTALLER_JAR_PATH,
    README_FILE,
    WINDOWS,
)


def sync_client_mods():
    print("\nInstalling mods...")
    all_client_mods = sync_mods.get_location_table_for(MODS_DIR)
    all_client_mods.update(sync_mods.get_location_table_for(CLIENT_MODS_DIR))

    current_client_mods = sync_mods.get_location_table_for(MINECRAFT_MODS_DIR)

    sync_mods.set_mods_from_to(all_client_mods, current_client_mods, MINECRAFT_MODS_DIR)


def install_extras():
    print("\nInstalling other files/folders...")
    for install_dir in EXTRA_INSTALL_FOLDERS:
        from_dir = os.path.join(SERVER_DIR, install_dir)
        to_dir = os.path.join(MINECRAFT_DIR, install_dir)
        print(f"\t{install_dir}...")
        shutil.copytree(from_dir, to_dir, dirs_exist_ok=True)

    for install_file in EXTRA_INSTALL_FILES:
        from_path = os.path.join(SERVER_DIR, install_file)
        to_path = os.path.join(MINECRAFT_DIR, install_file)
        print(f"\t{install_file}...")
        shutil.copy(from_path, to_path)


def ensure_forge_client():
    if not os.path.exists(os.path.join(MINECRAFT_DIR, FORGE_INSTALLER_JAR)):
        print("Opening forge installer; select 'Install client' and press 'Ok'.")
        launch_server.run_java(["-jar", FORGE_INSTALLER_JAR_PATH])


def open_readme():
    installed_readme = os.path.join(MINECRAFT_DIR, README_FILE)
    print(f"Opening {installed_readme}...")
    if WINDOWS:
        launch_server.run_cmd(["explorer", installed_readme], check=False)
    else:
        launch_server.run_cmd(["xdg-open", installed_readme], check=False)


def main():
    sync_mods.main()

    launch_server.clean_forge_jars(MINECRAFT_DIR)

    ensure_forge_client()
    sync_client_mods()
    install_extras()
    open_readme()


if __name__ == "__main__":
    main()
