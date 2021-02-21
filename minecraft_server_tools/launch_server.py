import os
import subprocess
from urllib.request import urlretrieve

from minecraft_server_tools.constants import (
    WINDOWS,
    JAVA_EXECUTABLE,
    MAX_RAM,
    JAVA_ARGS,
    FORGE_ARGS,
    FORGE_VERSION,
    FORGE_INSTALLER_URL,
    FORGE_JAR_PATH,
    FORGE_INSTALLER_JAR_PATH,
    OLD_JARS_REGEX,
    SERVER_DIR,
)


def run_cmd(cmd, check=True, shell=None):
    if shell is None:
        shell = WINDOWS
    print("> " + " ".join(str(x) for x in cmd))
    return subprocess.run(cmd, check=check, shell=shell)


def run_java(cmd):
    if WINDOWS:
        return run_cmd(["START", "/B", "/I", "/WAIT", "/HIGH", JAVA_EXECUTABLE] + cmd)
    else:
        return run_cmd([JAVA_EXECUTABLE] + cmd)


def install_forge_server():
    print(f"Installing forge from installer {FORGE_INSTALLER_JAR_PATH}...")
    run_java(["-jar", FORGE_INSTALLER_JAR_PATH, "--installServer"])


def clean_forge_jars(dir_to_clean=SERVER_DIR):
    for fname in os.listdir(dir_to_clean):
        if OLD_JARS_REGEX.match(fname) is not None:
            print(f"Removing old jar {fname}...")
            os.remove(os.path.join(dir_to_clean, fname))


def ensure_forge_server():
    if not os.path.exists(FORGE_INSTALLER_JAR_PATH):
        print(f"Downloading forge installer {FORGE_INSTALLER_JAR_PATH}...")
        urlretrieve(FORGE_INSTALLER_URL, FORGE_INSTALLER_JAR_PATH)
        install_forge_server()


def start_server():
    clean_forge_jars()
    ensure_forge_server()
    run_java(["-Xmx" + MAX_RAM, "-Xms" + MAX_RAM] + JAVA_ARGS + ["-jar", FORGE_JAR_PATH] + FORGE_ARGS)


if __name__ == "__main__":
    start_server()
