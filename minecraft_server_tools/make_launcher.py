from minecraft_server_tools import install_client
from minecraft_server_tools.constants import (
    WINDOWS,
    ROOT_DIR,
    LAUNCHER_FILE,
    NEW_LAUNCHER_PATH,
)

OPEN_CMD = "" if WINDOWS else "open "


def get_launcher_file_contents(install_client_args=""):
    """Get the contents that should go in the launcher script."""
    return f"""
cd "{ROOT_DIR}"
git pull
py -3 -m pip install -Ue .
py -3 -m minecraft_server_tools.install_client{install_client_args}
{OPEN_CMD}"{LAUNCHER_FILE}"
    """.strip()


def make_launcher_file(do_optional=False):
    """Create the launcher script."""
    if do_optional is None:
        install_client_args = ""
    elif do_optional:
        install_client_args = " --yes-optional"
    else:
        install_client_args = " --no-optional"
    with open(NEW_LAUNCHER_PATH, "w") as new_launcher_file:
        new_launcher_file.write(get_launcher_file_contents(install_client_args))


def main():
    install_client.main()
    make_launcher_file()


if __name__ == "__main__":
    main()
