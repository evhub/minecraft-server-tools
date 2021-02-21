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
    FORGE_JAR,
    FORGE_INSTALLER_JAR,
    OLD_JARS_REGEX,
    SERVER_DIR,
)


def run_cmd(cmd, **kwargs):
    print("> " + " ".join(str(x) for x in cmd))
    return subprocess.run(cmd, check=True, **kwargs)


def run_java(cmd):
    if WINDOWS:
        return run_cmd(["START", "/B", "/I", "/WAIT", "/HIGH", JAVA_EXECUTABLE] + cmd, shell=True)
    else:
        return run_cmd([JAVA_EXECUTABLE] + cmd)


def install_forge_server():
    print(f"Installing forge from installer {FORGE_INSTALLER_JAR}...")
    run_java(["-jar", FORGE_INSTALLER_JAR, "--installServer"])


def clean_forge_jars():
    for fname in os.listdir(SERVER_DIR):
        if OLD_JARS_REGEX.match(fname) is not None:
            print(f"Removing old jar {fname}...")
            os.remove(os.path.join(SERVER_DIR, fname))


def ensure_forge_server():
    if not os.path.exists(FORGE_INSTALLER_JAR):
        print(f"Downloading forge installer {FORGE_INSTALLER_JAR}...")
        urlretrieve(FORGE_INSTALLER_URL, FORGE_INSTALLER_JAR)
        install_forge_server()


def start_server():
    clean_forge_jars()
    ensure_forge_server()
    run_java(["-Xmx" + MAX_RAM, "-Xms" + MAX_RAM] + JAVA_ARGS + ["-jar", FORGE_JAR] + FORGE_ARGS)


if __name__ == "__main__":
    start_server()
