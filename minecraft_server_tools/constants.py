import os
import re

from jsoncomment import JsonComment


# Load secrets

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

SECRETS_FILE = os.path.join(ROOT_DIR, "secrets.json")

try:
    with open(SECRETS_FILE, "r") as fp:
        SECRETS = JsonComment().load(fp)
except FileNotFoundError:
    SECRETS = {}


# Mod sync constants

WINDOWS = os.name == "nt"

if WINDOWS:
    SERVER_DIR = "C:\\Users\\evanj\\OneDrive\\Minecraft\\ATM6 Mod Server"
else:
    SERVER_DIR = os.path.expanduser("~/atm6_server")

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

MC_VERSION = (1, 16, 5)

def ver_join(ver):
    return ".".join(str(i) for i in ver)

def ver_split(ver_str):
    return tuple(int(i) for i in ver_str.split("."))

COMPONENT_SEPS = [
    ("-", 2),
    ("(", 1),
    ("+", 2),
    ("_", 2),
    ("-", 1),
]
NON_NAME_COMPONENT_REGEX = re.compile("^(forge|[mcv0-9.+_\-x()]*)$")
NAME_ELEMS_TO_SPACE = [
    "-",
    "+",
    "_",
    "forge",
    "FORGE",
    "Forge",
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

SEARCH_URL_TEMPLATE = "https://www.googleapis.com/customsearch/v1/siterestrict?key={google_api_key}&cx={search_engine_id}&q={query}"

EXTRA_QUERY_INFO = "forge " + ver_join(MC_VERSION[:-1])

NON_CURSEFORGE_MODS = ["OptiFine", "preview OptiFine"]

WRONG_MODLOADER_VERSION = "fabric"

MOD_PAGE_NAME_SUFFIX = " - minecraft - curseforge"

CURSEFORGE_NAMES_FILE = os.path.join(ROOT_DIR, "curseforge_names.json")

CURSEFORGE_API_FILE = os.path.join(ROOT_DIR, "curseforge_api.js")

TIMESTAMP_FORMAT_REGEX = re.compile("^(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)\.?(\d+)?Z$")

UPDATED_MODS_DIR_SUFFIX = "-updates"
OLD_MODS_DIR_SUFFIX = "-old"

MAX_DEBUG_RESULTS = 50


# Server start constants

JAVA_EXECUTABLE = "java"

if WINDOWS:
    MAX_RAM = "7G"
else:
    MAX_RAM = "13G"

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

FORGE_VERSION = (36, 0, 21)

def format_vers(template):
    return template.format(
        mc_version=ver_join(MC_VERSION),
        forge_version=ver_join(FORGE_VERSION),
    )

FORGE_INSTALLER_URL = format_vers("https://files.minecraftforge.net/maven/net/minecraftforge/forge/{mc_version}-{forge_version}/forge-{mc_version}-{forge_version}-installer.jar")
FORGE_JAR = os.path.join(SERVER_DIR, format_vers("forge-{mc_version}-{forge_version}.jar"))
FORGE_INSTALLER_JAR = os.path.join(SERVER_DIR, format_vers("forge-{mc_version}-{forge_version}-installer.jar"))
