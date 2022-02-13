import os
import re
import sys

from jsoncomment import JsonComment


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
]

HOSTED_SERVER_DIR = fixpath("~/1_18_mod_server")

SERVER_DIR = first_that_exists([
    HOSTED_SERVER_DIR,
    "~/OneDrive/Minecraft/1.18 Mod Server",
    "/mnt/c/Users/evanj/OneDrive/Minecraft/1.18 Mod Server",
])

MOD_ZIP_PATH = first_that_exists([
    "~/OneDrive/Minecraft/Minecraft Mods/Minecraft Mods.zip",
    "~/OneDrive/Minecraft Mods/Minecraft Mods.zip",
])

if os.path.exists(HOSTED_SERVER_DIR):
    # server RAM
    if WINDOWS:
        MAX_RAM = "7G"
    else:
        MAX_RAM = "13G"
else:
    # client RAM
    if WINDOWS:
        MAX_RAM = "12G"
    else:
        MAX_RAM = "7G"


# Load secrets

SECRETS_FILE = os.path.join(SERVER_DIR, "secrets.json")

COMMENT_JSON = JsonComment()

try:
    with open(SECRETS_FILE, "r") as fp:
        SECRETS = COMMENT_JSON.load(fp)
except FileNotFoundError:
    SECRETS = {}


# Mod sync constants

MODS_NAME = "mods"
BASE_MODS_NAME = "mods-base"
EXTRA_MODS_NAME = "mods-main"
REMOVED_MODS_NAME = "mods-removed"

CLIENT_MODS_NAME = "client_mods"
BASE_CLIENT_MODS_NAME = "client_mods-base"
EXTRA_CLIENT_MODS_NAME = "client_mods-main"
REMOVED_CLIENT_MODS_NAME = "client_mods-removed"


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
    "   ",
    "  ",
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

JVM_ARGS = [
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
    # "-XX:+UseLargePagesInMetaspace",  # OLD
    "-XX:+UseG1GC",
    "-XX:MaxMetaspaceExpansion=64M",
    "-XX:G1ReservePercent=20",
    "-XX:G1NewSizePercent=20",
    "-XX:G1HeapRegionSize=32M",
    "-XX:MaxGCPauseMillis=40",
    "-XX:InitiatingHeapOccupancyPercent=20",  # atm: 15; default: 45
    "-XX:G1MixedGCCountTarget=4",  # NEW; default: 8
    "-XX:MaxTenuringThreshold=1",  # NEW; default: 15
    # "-XX:TargetSurvivorRatio=90",  # atm: 32; default: 50
    # "-XX:G1MixedGCLiveThresholdPercent=35",  # atm: 90; default: 85
    # "-XX:G1MaxNewSizePercent=60",  # atm: 40; default: 60
    # "-XX:G1HeapWastePercent=5",  # NEW; default: 5
    # "-XX:G1RSetUpdatingPauseTimePercent=5",  # NEW; default: 10
]

JAVA_ARGS = JVM_ARGS + [
    "-Dfml.queryResult=confirm",
    "-Dfml.readTimeout=300",
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
