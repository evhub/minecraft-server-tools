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
)


def run_cmd(cmd):
    return subprocess.run(cmd, check=True, shell=True)


def run_java(cmd):
    if WINDOWS:
        return run_cmd(["START", "/B", "/I", "/WAIT", "/HIGH", JAVA_EXECUTABLE] + cmd)
    else:
        return run_cmd([JAVA_EXECUTABLE] + cmd)


def install_forge_server():
    run_java(["-jar", FORGE_INSTALLER_JAR, "--installServer"])


def install_forge_client():
    run_java(["-jar", FORGE_INSTALLER_JAR, "--installClient"])


def ensure_forge_server():
    if not os.path.exists(FORGE_INSTALLER_JAR):
        urlretrieve(FORGE_INSTALLER_URL, FORGE_INSTALLER_JAR)
        install_forge_server()


def start_server():
    ensure_forge_server()
    run_java(["-Xmx" + MAX_RAM, "-Xms" + MAX_RAM] + JAVA_ARGS + ["-jar", FORGE_JAR] + FORGE_ARGS)


if __name__ == "__main__":
    start_server()
