import os
import re

from jsoncomment import JsonComment


# Commonly changed constants

MC_VERSION = (1, 16, 5)

FORGE_VERSION = (36, 0, 21)

WINDOWS = os.name == "nt"

if WINDOWS:
    SERVER_DIR = "C:\\Users\\evanj\\OneDrive\\Minecraft\\ATM6 Mod Server"
    MAX_RAM = "7G"
else:
    # SERVER_DIR = os.path.expanduser("~/atm6_server")
    SERVER_DIR = "/mnt/c/Users/evanj/OneDrive/Minecraft/ATM6 Mod Server"
    # MAX_RAM = "13G"
    MAX_RAM = "6G"


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


# Load secrets

SECRETS_FILE = os.path.join(SERVER_DIR, "secrets.json")

try:
    with open(SECRETS_FILE, "r") as fp:
        SECRETS = JsonComment().load(fp)
except FileNotFoundError:
    SECRETS = {}


# Mod sync constants

MODS_DIR = os.path.join(SERVER_DIR, "mods")
BASE_MODS_DIR = os.path.join(SERVER_DIR, "mods-base")
EXTRA_MODS_DIR = os.path.join(SERVER_DIR, "mods-extra")

CLIENT_MODS_DIR = os.path.join(SERVER_DIR, "mods-client")
BASE_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, "mods-client-base")
EXTRA_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, "mods-client-extra")

ALL_MOD_DIRS = [
    MODS_DIR,
    BASE_MODS_DIR,
    EXTRA_MODS_DIR,
    CLIENT_MODS_DIR,
    BASE_CLIENT_MODS_DIR,
    EXTRA_CLIENT_MODS_DIR,
]


# Auto updater Constants

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

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

SEARCH_URL_TEMPLATE = "https://www.googleapis.com/customsearch/v1/siterestrict?key={google_api_key}&cx={search_engine_id}&q={query}&nfpr=1&nirf={query}"

MODLOADER = "forge"
WRONG_MODLOADERS = ["fabric"]

GOOGLE_QUERY_TEMPLATE = "{mod_name} {modloader} {mc_version}"

NON_CURSEFORGE_MODS = ["OptiFine", "preview OptiFine"]

MOD_PAGE_NAME_SUFFIX = " - minecraft - curseforge"

CURSEFORGE_NAMES_FILE = os.path.join(ROOT_DIR, "curseforge_names.json")

CURSEFORGE_API_FILE = os.path.join(ROOT_DIR, "curseforge_api.js")

TIMESTAMP_FORMAT_REGEX = full_regex("(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)\.?(\d+)?Z")

UPDATED_MODS_DIR_SUFFIX = "-updates"
OLD_MODS_DIR_SUFFIX = "-old"

MAX_DEBUG_RESULTS = 20


# Server start constants

JAVA_EXECUTABLE = "java"

JAVA_ARGS = [
    "-d64",
    "-server",
    "-XX:+AggressiveOpts",
    "-XX:+UnlockExperimentalVMOptions",
    "-XX:+OptimizeStringConcat",
    "-XX:+AlwaysPreTouch",
    "-XX:+ExplicitGCInvokesConcurrentAndUnloadsClasses",
    "-XX:+ParallelRefProcEnabled",
    "-XX:+UseCompressedOops",
    "-XX:+ScavengeBeforeFullGC",
    "-XX:+PerfDisableSharedMem",
    "-XX:+UseLargePagesInMetaspace",
    "-XX:MaxMetaspaceExpansion=64M",
    "-XX:TargetSurvivorRatio=90",
    "-XX:MaxGCPauseMillis=40",
    "-XX:+UseG1GC",
    "-XX:+UseStringDeduplication",
    "-XX:InitiatingHeapOccupancyPercent=20",
    "-XX:G1HeapRegionSize=32M",
    "-XX:G1MixedGCLiveThresholdPercent=35",
    "-XX:G1ReservePercent=20",
    "-XX:G1NewSizePercent=20",
    "-XX:G1MaxNewSizePercent=60",
    "-Dfml.queryResult=confirm",
    "-Dfml.readTimeout=300",
]

FORGE_ARGS = ["nogui"]

FORGE_INSTALLER_URL = format_vers("https://files.minecraftforge.net/maven/net/minecraftforge/forge/{mc_version}-{forge_version}/forge-{mc_version}-{forge_version}-installer.jar")
FORGE_JAR = os.path.join(SERVER_DIR, format_vers("forge-{mc_version}-{forge_version}.jar"))
FORGE_INSTALLER_JAR = os.path.join(SERVER_DIR, format_vers("forge-{mc_version}-{forge_version}-installer.jar"))

OLD_JARS_REGEX = full_regex(format_vers("(forge-(?!{mc_version}-{forge_version})[0-9.]+-[0-9.]+(-installer)?|minecraft_server\.(?!{mc_version})[0-9.]+)\.jar"))
