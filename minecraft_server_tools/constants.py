import os
import re
import sys
from datetime import timedelta

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

def regex(re_str):
    return re.compile(re_str, re.UNICODE)

def full_regex(re_str):
    return regex("^" + re_str + "$")

def format_vers(template):
    return template.format(
        mc_version=ver_join(MC_VERSION),
        forge_version=ver_join(FORGE_VERSION),
    )

def fixpath(path):
    return os.path.normpath(os.path.abspath(os.path.expanduser(path)))

def first_that_exists(path_list):
    for path in path_list:
        if path is not None:
            path = fixpath(path)
            if os.path.exists(path):
                return path
    return [p for p in path_list if p is not None][0]

WINDOWS = os.name == "nt"


# Commonly changed constants

SERVER_DIR = first_that_exists([
    os.getenv("MINECRAFT_SERVER_DIR"),
    "~/1_19_mod_server",
    "~/OneDrive/Minecraft/1.19 Mod Server",
])

MOD_ZIP_PATH = first_that_exists([
    "~/OneDrive/Minecraft/Minecraft Mods/Minecraft Mods.zip",
    "~/OneDrive/Minecraft Mods/Minecraft Mods.zip",
])

IS_MOD_SERVER = "mod" in SERVER_DIR.lower()

MC_VERSION = (1, 19, 2)

if IS_MOD_SERVER:
    FORGE_VERSION = (43, 2, 4)
else:
    FORGE_VERSION = (43, 1, 1)

if IS_MOD_SERVER:
    CLIENT_RAM = "16G"
    if WINDOWS:
        SERVER_RAM = "10G"
    else:
        SERVER_RAM = "26G"
else:
    CLIENT_RAM = SERVER_RAM = "5G"

ALWAYS_USE_LATEST_VERSION_FOR_MODS = [
    "toofast",
]

EXTRA_INSTALL_FOLDERS = [
    "config",
    "defaultconfigs",
    "kubejs",
    "resourcepacks",
    "shaderpacks",
    "scripts",
    "global_data_packs",
    "global_resource_packs",
    "paintings",
    "shrines-data",
    "packmenu",
    "global_packs",
    "patchouli_books",
]

EXTRA_INSTALL_FILES = [
    "patchouli_data.json",
]


# Fix RAMs

GB = 1024**3
max_client_ram = psutil.virtual_memory().total // GB - 1
max_server_ram = psutil.virtual_memory().total // GB - 3

if int(CLIENT_RAM[:-1]) > max_client_ram:
    print(f"\nWARNING: Reducing client RAM from {CLIENT_RAM} to {max_client_ram}G.")
    CLIENT_RAM = str(max_client_ram) + "G"

if int(SERVER_RAM[:-1]) > max_server_ram:
    print(f"\nWARNING: Reducing server RAM from {SERVER_RAM} to {max_server_ram}G.")
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
DEDUPLICATE_MODS_NAME = MODS_NAME + "-deduplicate"

CLIENT_MODS_NAME = "client_mods"
BASE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-base"
EXTRA_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-main"
REMOVED_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-removed"
DEDUPLICATE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-deduplicate"


# Auto updater Constants

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

MODLOADER = "Forge"
WRONG_MODLOADERS = ["Fabric", "Quilt"]

PREFER_TWO_NUM_VER_TO_WRONG_THREE_NUM = True

NON_CURSEFORGE_MODS = [
    "OptiFine",
    "preview OptiFine",
]

COMPONENT_SEPS = [
    ("-", 2),
    ("(", 1),
    ("+", 2),
    ("-", 1),
    ("_", 2),
    (" ", 2),
    ("+", 1),
    ("_", 1),
    (" ", 1),
]

NON_NAME_COMPONENT_REGEX = full_regex(
    r"[0-9].*|"
    r"(?!cave|a$|ae2)((forge|fabric|quilt|dist(ro)?|release|alpha|beta)(\..*)?|(mc|v|r)?[0-9.+_\-x()[\]]*(a|b|c|d|e|m)?)+"
)

NAME_REGEXES_TO_SPACE = [
    regex(r) for r in (
        r"-",
        r"\+",
        r"_",
        r"\(",
        r"\)",
        r"forge\b",
        r"FORGE",
        r"Forge\b",
        r"fabric\b",
        r"FABRIC",
        r"Fabric\b",
        r"quilt\b",
        r"QUILT",
        r"Quilt\b",
        r"\bdist(ro)?",
        r"release",
        r"\balpha\b",
        r"\bALPHA\b",
        r"\bAlpha\b",
        r"\bbeta\b",
        r"\bBETA\b",
        r"\bBeta\b",
        r"MC",
        r"\bmc\b",
        r"1\.\d+",
        r"\.0",
        r"\.1",
        r"\.2",
        r"\.3",
        r"\.4",
        r"\.5",
        r"\.6",
        r"\.7",
        r"\.8",
        r"\.9",
        r"\.",
        r" / ",
        r" \| ",
        r"   ",
        r"  ",
        r" / ",
        r"\[ \]",
        r"  ",
    )
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

AVOID_FILES_PUBLISHED_WITHIN = timedelta(days=2)

SEARCH_URL_TEMPLATE = "https://www.googleapis.com/customsearch/v1/siterestrict?key={google_api_key}&cx={search_engine_id}&q={query}&nfpr=1&nirf={query}"

MOD_PAGE_NAME_SUFFIX = " - Mods - Minecraft - Curseforge"

GOOGLE_QUERY_TEMPLATE = '{mod_name} {modloader} {mc_version_2} "{mod_page_name_suffix}"'

CURSEFORGE_NAMES_FILE = os.path.join(ROOT_DIR, "curseforge_names.json")

CURSEFORGE_API_FILE = os.path.join(ROOT_DIR, "curseforge_api.js")

CURSEFORGE_QUERY_TEMPLATES = [
    '"{curseforge_name}"',
    "{core_curseforge_name}",
    "{mod_name}",
]

TIMESTAMP_FORMAT_REGEX = full_regex("(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)\.?(\d+)?Z")

UPDATED_MODS_DIR_SUFFIX = "-updates"
OLD_MODS_DIR_SUFFIX = "-old"

DEBUG = False
MAX_DEBUG_RESULTS = 2

CURSEFORGE_API_RETRIES = 3
CURSEFORGE_API_RETRY_DELAY = 0.1


# Large page setup constants

USE_LARGE_PAGES = False


# Server start constants

JAVA_EXECUTABLE = "java"

CLIENT_GC = "G1"
SERVER_GC = "Shenandoah"

BASE_JVM_ARGS = [
    # "-d64",  # OLD
    "-server",
    # "-XX:+AggressiveOpts",  # OLD
    "-XX:+UnlockExperimentalVMOptions",  # always
    "-XX:+AlwaysPreTouch",  # always
    "-XX:+DisableExplicitGC",  # always
    # "-XX:+ExplicitGCInvokesConcurrentAndUnloadsClasses",  # OLD
    "-XX:+OptimizeStringConcat",
    "-XX:+ParallelRefProcEnabled",  # aikar-flags
    "-XX:+UseCompressedOops",
    "-XX:+ScavengeBeforeFullGC",
    "-XX:+PerfDisableSharedMem",  # aikar-flags
    "-XX:+UseStringDeduplication",
    # "-XX:+OmitStackTraceInFastThrow",
    # "-XX:+UseLargePagesInMetaspace",  # OLD
    "-XX:+UseLargePages",  # hilltty-flags
    "-XX:MaxMetaspaceExpansion=64M",  # default: 5M
    "-XX:MaxGCPauseMillis=60",  # atm: 200; default: 200
    "-XX:InitiatingHeapOccupancyPercent=20",  # atm: 15; default: 45
    "-XX:MaxTenuringThreshold=1",  # atm: 1; default: 15
    # "-XX:TargetSurvivorRatio=90",  # atm: 32; default: 50
    # "-XX:SurvivorRatio=32",  # atm: 32; default: 8
    "-XX:+UseNUMA",  # hilltty-flags
    "-XX:-UseBiasedLocking",  # hilltty-flags
] + ([
    "-XX:LargePageSizeInBytes=2M",  # hilltty-flags
] if USE_LARGE_PAGES else [])

def get_jvm_args_for_gc(gc):
    if gc == "G1":
        return [
            "-XX:+UseG1GC",
            "-XX:G1ReservePercent=20",  # atm: 20
            "-XX:G1NewSizePercent=20",  # atm: 30
            "-XX:G1HeapRegionSize=32M",  # atm: 8M
            "-XX:G1MixedGCCountTarget=4",  # atm: 4; default: 8
            # "-XX:G1MixedGCLiveThresholdPercent=35",  # atm: 90; default: 85
            # "-XX:G1MaxNewSizePercent=60",  # atm: 40; default: 60
            # "-XX:G1HeapWastePercent=5",  # atm: 5; default: 5
            # "-XX:G1RSetUpdatingPauseTimePercent=5",  # atm: 5; default: 10
        ]
    elif gc == "Shenandoah":
        return [
            "-XX:+UseShenandoahGC",
            "-XX:ShenandoahGCMode=iu",  # hilltty-flags
        ]
    elif gc == "Z":
        return [
            "-XX:+UseZGC",
        ]
    else:
        raise ValueError(f"unknown GC {gc!r}")

FML_ARGS = [
    "-Dfml.queryResult=confirm",
    "-Dfml.readTimeout=900",
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

OLD_JARS_REGEX = full_regex(format_vers(r"(forge-(?!{mc_version}-{forge_version})[0-9.]+-[0-9.]+(-installer)?|minecraft_server\.(?!{mc_version})[0-9.]+)\.jar"))


# Client install constants

if sys.platform.startswith("win"):
    MINECRAFT_DIR = fixpath("~/AppData/Roaming/.minecraft")
elif sys.platform.startswith("darwin"):
    MINECRAFT_DIR = fixpath("~/Library/Application Support/minecraft")
else:
    MINECRAFT_DIR = fixpath("~/.minecraft")

PROFILES_FILE = os.path.join(MINECRAFT_DIR, "launcher_profiles.json")

README_FILE = "README.txt"

EXTRA_INSTALL_FILES += [
    README_FILE,
    FORGE_INSTALLER_JAR,
]

OPTIONAL_INSTALL_FILES = [
    "options.txt",
    "optionsof.txt",
    "optionsshaders.txt",
]

OPTIONAL_INSTALL_FOLDERS = [
    os.path.join("journeymap", "config"),
]

YES_STRS = [
    "y",
    "yes",
]


# Make launcher constants

LAUNCHER_FILE = first_that_exists([
    "~/Applications/Minecraft.app",
    "/Applications/Minecraft.app",
    r"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe",
    r"C:\Users\Public\Desktop\Minecraft Launcher.ink",
])

DESKTOP_DIR = first_that_exists([
    "~/Desktop",
    "~/OneDrive/Desktop",
])

NEW_LAUNCHER_PATH = fixpath(os.path.join(
    DESKTOP_DIR,
    "Evan's Modded Minecraft" + (".bat" if WINDOWS else ".sh"),
))


# Searchable mods constants

SEARCHABLE_MODS_NAME = MODS_NAME + "-searchable"
SEARCHABLE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-searchable"
