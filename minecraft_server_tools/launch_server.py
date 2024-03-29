import os
import sys
import subprocess
from urllib.request import urlretrieve

from minecraft_server_tools.constants import (
    WINDOWS,
    JAVA_EXECUTABLE,
    SERVER_RAM,
    BASE_JVM_ARGS,
    FORGE_ARGS,
    FORGE_INSTALLER_URL,
    OLD_JARS_REGEX,
    SERVER_DIR,
    FORGE_JAR,
    FORGE_INSTALLER_JAR,
    JVM_ARGS_FILE,
    FORGE_LAUNCH_CMD,
    FML_ARGS,
    CLIENT_RAM,
    SERVER_GC,
    CLIENT_GC,
    get_jvm_args_for_gc,
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


def ensure_forge_server():
    if not os.path.exists(FORGE_INSTALLER_JAR_PATH):
        print(f"Downloading forge installer {FORGE_INSTALLER_JAR_PATH}...")
        urlretrieve(FORGE_INSTALLER_URL, FORGE_INSTALLER_JAR_PATH)
        install_forge_server()


def clean_forge_jars(dir_to_clean=SERVER_DIR):
    for fname in os.listdir(dir_to_clean):
        if OLD_JARS_REGEX.match(fname) is not None:
            print(f"Removing old jar {fname}...")
            os.remove(os.path.join(dir_to_clean, fname))


def get_java_args(client=False):
    if client:
        ram = CLIENT_RAM
        gc = CLIENT_GC
    else:
        ram = SERVER_RAM
        gc = SERVER_GC
    args = (
        ["-Xmx" + ram, "-Xms" + ram]
        + BASE_JVM_ARGS
        + get_jvm_args_for_gc(gc)
    )
    if not client:
        args += FML_ARGS
    return args


def fix_run_bat():
    with open(os.path.join(SERVER_DIR, "run.bat"), "r+") as run_bat:
        content = run_bat.read()
        run_bat.seek(0)
        run_bat.truncate()
        run_bat.write(content.replace("pause", "exit"))


def write_jvm_args():
    with open(JVM_ARGS_FILE, "w") as jvm_args_file:
        jvm_args_file.write("\n".join(get_java_args()) + "\n")


def start_server(dry_run=False):
    clean_forge_jars()
    ensure_forge_server()
    fix_run_bat()
    write_jvm_args()
    if not dry_run:
        if os.path.exists(FORGE_JAR_PATH):
            run_java(get_java_args() + [FORGE_JAR_PATH] + FORGE_ARGS)
        else:
            run_high_priority(FORGE_LAUNCH_CMD + FORGE_ARGS)


def main():
    start_server(dry_run="--dry-run" in sys.argv)


if __name__ == "__main__":
    main()
