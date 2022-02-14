import os
import subprocess
from urllib.request import urlretrieve

from minecraft_server_tools.constants import (
    WINDOWS,
    JAVA_EXECUTABLE,
    SERVER_RAM,
    JVM_ARGS,
    FORGE_ARGS,
    FORGE_INSTALLER_URL,
    OLD_JARS_REGEX,
    SERVER_DIR,
    FORGE_JAR,
    FORGE_INSTALLER_JAR,
    JVM_ARGS_FILE,
    FORGE_LAUNCH_CMD,
    FML_ARGS,
)

FORGE_JAR_PATH = os.path.join(SERVER_DIR, FORGE_JAR)
FORGE_INSTALLER_JAR_PATH = os.path.join(SERVER_DIR, FORGE_INSTALLER_JAR)


def run_cmd(cmd, check=True, shell=False):
    print("> " + " ".join(str(x) for x in cmd))
    return subprocess.run(cmd, check=check, shell=shell)


def run_high_priority(cmd, name="Minecraft Server"):
    if WINDOWS:
        return run_cmd(["START", name, "/B", "/I", "/WAIT", "/HIGH"] + cmd, shell=True)
    else:
        return run_cmd(cmd)


def run_java(cmd):
    return run_high_priority([JAVA_EXECUTABLE] + cmd)


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


def get_java_args(ram=SERVER_RAM):
    return ["-Xmx" + ram, "-Xms" + ram] + JVM_ARGS + FML_ARGS


def write_jvm_args():
    with open(JVM_ARGS_FILE, "w") as jvm_args_file:
        jvm_args_file.write("\n".join(get_java_args()) + "\n")


def start_server():
    clean_forge_jars()
    ensure_forge_server()
    write_jvm_args()
    if os.path.exists(FORGE_JAR_PATH):
        run_java(get_java_args() + [FORGE_JAR_PATH] + FORGE_ARGS)
    else:
        run_high_priority(FORGE_LAUNCH_CMD + FORGE_ARGS)


if __name__ == "__main__":
    start_server()
