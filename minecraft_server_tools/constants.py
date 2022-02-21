import os
import re
import sys

import psutil
try:
    from jsoncomment import JsonComment
except ImportError:
    print("\nWARNING: Could not import jsoncomment.")
    JsonComment = None


# Utilities

def ver_join(ver):
    return ".".join(str(i) for i in ver)

def ver_split(ver_str):
    return tuple(int(i) for i in ver_str.split("."))

def full_regex(re_str):
    return re.compile("^" + re_str + "$")

def format_vers(template):
    return template.format(
        mc_version=ver_join(MC_VERSION),
        forge_version=ver_join(FORGE_VERSION),
    )

def fixpath(path):
    return os.path.normpath(os.path.expanduser(path))

def first_that_exists(path_list):
    for path in path_list:
        path = fixpath(path)
        if os.path.exists(path):
            return path
    return path_list[0]


# Commonly changed constants

WINDOWS = os.name == "nt"

MC_VERSION = (1, 18, 1)
FORGE_VERSION = (39, 0, 75)

EXTRA_INSTALL_FOLDERS = [
    "config",
    "defaultconfigs",
    "kubejs",
    "resourcepacks",
    "scripts",
    "global_data_packs",
    "global_resource_packs",
    "paintings",
    "shrines-data",
    "packmenu",
    "global_packs",
]

SERVER_DIR = first_that_exists([
    "~/1_18_mod_server",
    "~/OneDrive/Minecraft/1.18 Mod Server",
    "/mnt/c/Users/evanj/OneDrive/Minecraft/1.18 Mod Server",
])

MOD_ZIP_PATH = first_that_exists([
    "~/OneDrive/Minecraft/Minecraft Mods/Minecraft Mods.zip",
    "~/OneDrive/Minecraft Mods/Minecraft Mods.zip",
])

if WINDOWS:
    CLIENT_RAM = "16G"
else:
    CLIENT_RAM = "14G"

if WINDOWS:
    SERVER_RAM = "14G"
else:
    SERVER_RAM = "13G"


# Fix RAMs

GB = 1024**3
max_client_ram = psutil.virtual_memory().total // GB - 1
max_server_ram = psutil.virtual_memory().available // GB

if int(CLIENT_RAM[:-1]) > max_client_ram:
    print(f"\nReducing client RAM from {CLIENT_RAM}G to {max_client_ram}G.")
    CLIENT_RAM = str(max_client_ram) + "G"

if int(SERVER_RAM[:-1]) > max_server_ram:
    print(f"\nReducing server RAM from {SERVER_RAM}G to {max_server_ram}G.")
    SERVER_RAM = str(max_server_ram) + "G"


# Load secrets

SECRETS_FILE = os.path.join(SERVER_DIR, "secrets.json")

if JsonComment is not None:
    COMMENT_JSON = JsonComment()

    try:
        with open(SECRETS_FILE, "r") as fp:
            SECRETS = COMMENT_JSON.load(fp)
    except FileNotFoundError:
        SECRETS = {}
else:
    SECRETS = {}


# Mod sync constants

MODS_NAME = "mods"
BASE_MODS_NAME = MODS_NAME + "-base"
EXTRA_MODS_NAME = MODS_NAME + "-main"
REMOVED_MODS_NAME = MODS_NAME + "-removed"

CLIENT_MODS_NAME = "client_mods"
BASE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-base"
EXTRA_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-main"
REMOVED_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-removed"


# Auto updater Constants

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

MODLOADER = "forge"
WRONG_MODLOADERS = ["fabric"]

NON_CURSEFORGE_MODS = [
    "OptiFine",
    "preview OptiFine",
]

COMPONENT_SEPS = [
    ("-", 2),
    ("(", 1),
    ("+", 2),
    ("_", 2),
    ("-", 1),
    (" ", 2),
    ("+", 1),
    ("_", 1),
    (" ", 1),
]

NON_NAME_COMPONENT_REGEX = full_regex("(forge|fabric|dist(ro)?|release|alpha|beta|(mc|v|r)?[0-9.+_\-x()[\]]*(a|b|c|d|e|m)?)+")

NAME_ELEMS_TO_SPACE = [
    "-",
    "+",
    "_",
    "(",
    ")",
    "forge",
    "FORGE",
    "Forge",
    "fabric",
    "FABRIC",
    "Fabric",
    "dist",
    "distro",
    "release",
    "alpha",
    "beta",
    ver_join(MC_VERSION[:-1]),
    ".0",
    ".1",
    ".2",
    ".3",
    ".4",
    ".5",
    ".6",
    ".7",
    ".8",
    ".9",
    ".",
    "   ",
    "  ",
    "[ ]",
]

CURSEFORGE_NAME_ELEMS_TO_STRIP = [
    "-",
    "Download",
    "Files",
    "Mods",
    "Minecraft",
    "Curseforge",
    "...",
]

SEARCH_URL_TEMPLATE = "https://www.googleapis.com/customsearch/v1/siterestrict?key={google_api_key}&cx={search_engine_id}&q={query}&nfpr=1&nirf={query}"

MOD_PAGE_NAME_SUFFIX = " - Mods - Minecraft - Curseforge"

GOOGLE_QUERY_TEMPLATE = '{mod_name} {modloader} {mc_version_2} "{mod_page_name_suffix}"'

CURSEFORGE_NAMES_FILE = os.path.join(ROOT_DIR, "curseforge_names.json")

CURSEFORGE_API_FILE = os.path.join(ROOT_DIR, "curseforge_api.js")

CURSEFORGE_QUERY_TEMPLATE = '"{curseforge_name}"'

TIMESTAMP_FORMAT_REGEX = full_regex("(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)\.?(\d+)?Z")

UPDATED_MODS_DIR_SUFFIX = "-updates"
OLD_MODS_DIR_SUFFIX = "-old"

MAX_DEBUG_RESULTS = 20


# Server start constants

JAVA_EXECUTABLE = "java"

CLIENT_GC = "G1"
SERVER_GC = "Shenandoah"

BASE_JVM_ARGS = [
    # "-d64",  # OLD
    "-server",
    # "-XX:+AggressiveOpts",  # OLD
    "-XX:+UnlockExperimentalVMOptions",
    "-XX:+OptimizeStringConcat",
    "-XX:+AlwaysPreTouch",
    # "-XX:+ExplicitGCInvokesConcurrentAndUnloadsClasses",  # OLD
    "-XX:+DisableExplicitGC",  # NEW
    "-XX:+ParallelRefProcEnabled",
    "-XX:+UseCompressedOops",
    "-XX:+ScavengeBeforeFullGC",
    "-XX:+PerfDisableSharedMem",
    "-XX:+UseStringDeduplication",
    "-XX:+OmitStackTraceInFastThrow",  # NEW
    # "-XX:+UseLargePagesInMetaspace",  # OLD
    # "-XX:+UseLargePages",  # NEW
    "-XX:MaxMetaspaceExpansion=64M",  # default: 5M
    "-XX:MaxGCPauseMillis=40",  # atm: 200; default: 200
    "-XX:InitiatingHeapOccupancyPercent=20",  # atm: 15; default: 45
    "-XX:MaxTenuringThreshold=1",  # atm: 1; default: 15
    # "-XX:TargetSurvivorRatio=90",  # atm: 32; default: 50
]

def get_jvm_args_for_gc(gc):
    if gc == "G1":
        return [
            "-XX:+UseG1GC",
            "-XX:G1ReservePercent=20",
            "-XX:G1NewSizePercent=20",
            "-XX:G1HeapRegionSize=32M",
            "-XX:G1MixedGCCountTarget=4",  # NEW; default: 8
            # "-XX:G1MixedGCLiveThresholdPercent=35",  # atm: 90; default: 85
            # "-XX:G1MaxNewSizePercent=60",  # atm: 40; default: 60
            # "-XX:G1HeapWastePercent=5",  # NEW; default: 5
            # "-XX:G1RSetUpdatingPauseTimePercent=5",  # NEW; default: 10
        ]
    elif gc == "Shenandoah":
        return [
            "-XX:+UseShenandoahGC",
        ]
    elif gc == "Z":
        return [
            "-XX:+UseZGC",
        ]
    else:
        raise ValueError(f"unknown GC {gc!r}")

FML_ARGS = [
    "-Dfml.queryResult=confirm",
    "-Dfml.readTimeout=300",
    "-Dfml.ignoreInvalidMinecraftCertificates=true",
]

FORGE_ARGS = ["nogui"]

JVM_ARGS_FILE = os.path.join(SERVER_DIR, "user_jvm_args.txt")

if WINDOWS:
    FORGE_LAUNCH_CMD = [os.path.join(SERVER_DIR, "run.bat")]
else:
    FORGE_LAUNCH_CMD = ["sh", os.path.join(SERVER_DIR, "run.sh")]

FORGE_INSTALLER_URL = format_vers("https://files.minecraftforge.net/maven/net/minecraftforge/forge/{mc_version}-{forge_version}/forge-{mc_version}-{forge_version}-installer.jar")

FORGE_INSTALLER_JAR = format_vers("forge-{mc_version}-{forge_version}-installer.jar")
FORGE_JAR = format_vers("forge-{mc_version}-{forge_version}.jar")

OLD_JARS_REGEX = full_regex(format_vers("(forge-(?!{mc_version}-{forge_version})[0-9.]+-[0-9.]+(-installer)?|minecraft_server\.(?!{mc_version})[0-9.]+)\.jar"))


# Client install constants

if sys.platform.startswith("win"):
    MINECRAFT_DIR = fixpath("~/AppData/Roaming/.minecraft")
elif sys.platform.startswith("darwin"):
    MINECRAFT_DIR = fixpath("~/Library/Application Support/minecraft")
else:
    MINECRAFT_DIR = fixpath("~/.minecraft")

PROFILES_FILE = os.path.join(MINECRAFT_DIR, "launcher_profiles.json")

README_FILE = "README.txt"

EXTRA_INSTALL_FILES = [
    README_FILE,
    FORGE_INSTALLER_JAR,
]

OPTIONAL_INSTALL_FILES = [
    "options.txt",
    "optionsof.txt",
]

YES_STRS = [
    "y",
    "yes",
]


# Searchable mods constants

SEARCHABLE_MODS_NAME = MODS_NAME + "-searchable"
SEARCHABLE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-searchable"
