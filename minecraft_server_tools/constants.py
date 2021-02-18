import os
import re
import json


# Load secrets

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

SECRETS_FILE = os.path.join(ROOT_DIR, "secrets.json")

with open(SECRETS_FILE, "r") as fp:
    secrets = json.load(fp)


# Mod sync constants

SERVER_DIR = "C:\\Users\\evanj\\OneDrive\\Minecraft\\ATM6 Mod Server"

MODS_DIR = os.path.join(SERVER_DIR, "mods")
BASE_MODS_DIR = os.path.join(SERVER_DIR, "mods-base")
EXTRA_MODS_DIR = os.path.join(SERVER_DIR, "mods-extra")

CLIENT_MODS_DIR = os.path.join(SERVER_DIR, "mods-client")
BASE_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, "mods-client-base")
EXTRA_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, "mods-client-extra")

ALL_MOD_DIRS = (
    MODS_DIR,
    BASE_MODS_DIR,
    EXTRA_MODS_DIR,
    CLIENT_MODS_DIR,
    BASE_CLIENT_MODS_DIR,
    EXTRA_CLIENT_MODS_DIR,
)


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

SEARCH_URL = "https://www.googleapis.com/customsearch/v1/siterestrict?key={api_key}&cx={search_engine_id}&q={query}"
SEARCH_ENGINE_ID = secrets["search_engine_id"]
API_KEY = secrets["api_key"]

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
