#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa7a4fc63

# Compiled with Coconut version 3.1.1-post_dev2

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.1-post_dev2', '', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

import os  #1 (line in Coconut source)
import re  #2 (line in Coconut source)
import sys  #3 (line in Coconut source)
from datetime import timedelta  #4 (line in Coconut source)

import psutil  #6 (line in Coconut source)
try:  #7 (line in Coconut source)
    from jsoncomment import JsonComment  #8 (line in Coconut source)
except ImportError:  #9 (line in Coconut source)
    print("\nWARNING: Could not import jsoncomment.")  #10 (line in Coconut source)
    JsonComment = None  #11 (line in Coconut source)


# Utilities

@_coconut_tco  #16 (line in Coconut source)
def ver_join(ver):  #16 (line in Coconut source)
    return _coconut_tail_call(".".join, (str(i) for i in ver))  #17 (line in Coconut source)


@_coconut_tco  #19 (line in Coconut source)
def ver_split(ver_str):  #19 (line in Coconut source)
    return _coconut_tail_call(tuple, (int(i) for i in ver_str.split(".")))  #20 (line in Coconut source)


@_coconut_tco  #22 (line in Coconut source)
def regex(re_str):  #22 (line in Coconut source)
    return _coconut_tail_call(re.compile, re_str, re.UNICODE)  #23 (line in Coconut source)


@_coconut_tco  #25 (line in Coconut source)
def full_regex(re_str):  #25 (line in Coconut source)
    return _coconut_tail_call(regex, "^" + re_str + "$")  #26 (line in Coconut source)


@_coconut_tco  #28 (line in Coconut source)
def format_vers(template):  #28 (line in Coconut source)
    return _coconut_tail_call(template.format, mc_version=ver_join(MC_VERSION), forge_version=ver_join(FORGE_VERSION))  #29 (line in Coconut source)


@_coconut_tco  #34 (line in Coconut source)
def fixpath(path):  #34 (line in Coconut source)
    return _coconut_tail_call(os.path.normpath, os.path.abspath(os.path.expanduser(path)))  #35 (line in Coconut source)


def first_that_exists(path_list):  #37 (line in Coconut source)
    for path in path_list:  #38 (line in Coconut source)
        if path is not None:  #39 (line in Coconut source)
            path = fixpath(path)  #40 (line in Coconut source)
            if os.path.exists(path):  #41 (line in Coconut source)
                return path  #42 (line in Coconut source)
    return [p for p in path_list if p is not None][0]  #43 (line in Coconut source)


def bool_env_var(env_var, default):  #45 (line in Coconut source)
    got = os.getenv(env_var)  #46 (line in Coconut source)
    if got is None:  #47 (line in Coconut source)
        return default  #48 (line in Coconut source)
    got = got.lower()  #49 (line in Coconut source)
    if got in YES_STRS:  #50 (line in Coconut source)
        return True  #51 (line in Coconut source)
    elif got in NO_STRS:  #52 (line in Coconut source)
        return False  #53 (line in Coconut source)
    else:  #54 (line in Coconut source)
        return default  #55 (line in Coconut source)


WINDOWS = os.name == "nt"  #57 (line in Coconut source)


# Commonly changed constants

MC_VERSION = (1, 20, 1)  #62 (line in Coconut source)
FORGE_VERSION = (47, 3, 0)  #63 (line in Coconut source)

SERVER_DIR = first_that_exists([os.getenv("MINECRAFT_SERVER_DIR"), "~/OneDrive/Minecraft/1.20 Mod Server"])  #65 (line in Coconut source)

MOD_ZIP_PATH = first_that_exists(["D:\\\\Minecraft Mods.zip", "~/OneDrive/Minecraft/Minecraft Mods/Minecraft Mods.zip", "~/OneDrive/Minecraft Mods/Minecraft Mods.zip", "~/Downloads/Minecraft Mods.zip"])  #70 (line in Coconut source)

DOWNLOADS_PATH = first_that_exists(["~/Downloads",])  #77 (line in Coconut source)

IS_MOD_SERVER = "mod" in SERVER_DIR.lower()  #81 (line in Coconut source)

if IS_MOD_SERVER:  #83 (line in Coconut source)
    CLIENT_RAM = "25G"  #84 (line in Coconut source)
# SERVER_RAM = "9G"
    SERVER_RAM = "18G"  #86 (line in Coconut source)
else:  #87 (line in Coconut source)
    CLIENT_RAM = SERVER_RAM = "5G"  #88 (line in Coconut source)

ALWAYS_USE_LATEST_VERSION_FOR_MODS = ["jei", "toofast", "gottagofast", "supplementaries", "packet fixer", "embeddium", "oculus", "immediately fast"]  #90 (line in Coconut source)

NON_CURSEFORGE_MODS = ["opti fine", "preview opti fine", "create structures", "memoryleakfix"]  #101 (line in Coconut source)

EXTRA_INSTALL_FOLDERS = ["config", "defaultconfigs", "kubejs", "resourcepacks", "datapacks", "scripts", "global_data_packs", "global_resource_packs", "paintings", "shrines-data", "packmenu", "global_packs", "patchouli_books", "modernfix", "configureddefaults", "blueprints"]  #108 (line in Coconut source)

EXTRA_INSTALL_FILES = ["patchouli_data.json",]  #127 (line in Coconut source)

OPTIONAL_INSTALL_FILES = ["options.txt", "optionsof.txt", "optionsshaders.txt"]  #131 (line in Coconut source)

OPTIONAL_INSTALL_FOLDERS = [os.path.join("journeymap", "config"), "shaderpacks", "ESM"]  #137 (line in Coconut source)

PRINT_DEBUG = bool_env_var("MC_DEBUG_PRINT", False)  #143 (line in Coconut source)
JPS_DEBUG = bool_env_var("MC_DEBUG_JPS", False)  # filter jstack: ^(\s*(at java|at jdk|at sun|at net.minecraft|at io.netty)\b)[^\n]*\n*  #144 (line in Coconut source)
LOG4J_DEBUG = bool_env_var("MC_DEBUG_LOG4J", False)  #145 (line in Coconut source)


# Fix RAMs

GB = 1024**3  #150 (line in Coconut source)
max_client_ram = psutil.virtual_memory().total // GB - 2  #151 (line in Coconut source)
max_server_ram = psutil.virtual_memory().total // GB - 3  #152 (line in Coconut source)

if int(CLIENT_RAM[:-1]) > max_client_ram:  #154 (line in Coconut source)
    print("\nWARNING: Reducing client RAM from {_coconut_format_0} to {_coconut_format_1}G.".format(_coconut_format_0=(CLIENT_RAM), _coconut_format_1=(max_client_ram)))  #155 (line in Coconut source)
    CLIENT_RAM = str(max_client_ram) + "G"  #156 (line in Coconut source)

if int(SERVER_RAM[:-1]) > max_server_ram:  #158 (line in Coconut source)
    print("\nWARNING: Reducing server RAM from {_coconut_format_0} to {_coconut_format_1}G.".format(_coconut_format_0=(SERVER_RAM), _coconut_format_1=(max_server_ram)))  #159 (line in Coconut source)
    SERVER_RAM = str(max_server_ram) + "G"  #160 (line in Coconut source)


# Load secrets

SECRETS_FILE = os.path.join(SERVER_DIR, "secrets.json")  #165 (line in Coconut source)


def load_json(filename, default=None):  #168 (line in Coconut source)
    assert COMMENT_JSON is not None, "loading json requires JsonComment"  #169 (line in Coconut source)
    try:  #170 (line in Coconut source)
        with open(filename, "r") as fp:  #171 (line in Coconut source)
            return COMMENT_JSON.load(fp)  #172 (line in Coconut source)
    except (FileNotFoundError, ValueError):  #173 (line in Coconut source)
        return default  #174 (line in Coconut source)



if JsonComment is None:  #177 (line in Coconut source)
    COMMENT_JSON = SECRETS = None  #178 (line in Coconut source)
else:  #179 (line in Coconut source)
    COMMENT_JSON = JsonComment()  #180 (line in Coconut source)
    SECRETS = load_json(SECRETS_FILE, _coconut.dict())  #181 (line in Coconut source)
    if SECRETS:  #182 (line in Coconut source)
        os.environ["CURSEFORGE_API_KEY"] = SECRETS["curseforge_api_key"]  #183 (line in Coconut source)


# Mod sync constants

MODS_NAME = "mods"  #188 (line in Coconut source)
BASE_MODS_NAME = MODS_NAME + "-base"  #189 (line in Coconut source)
EXTRA_MODS_NAME = MODS_NAME + "-extra"  #190 (line in Coconut source)
REMOVED_MODS_NAME = MODS_NAME + "-removed"  #191 (line in Coconut source)
STAGING_MODS_NAME = MODS_NAME + "-staging"  #192 (line in Coconut source)
DEDUPLICATE_MODS_NAME = MODS_NAME + "-deduplicate"  #193 (line in Coconut source)

CLIENT_MODS_NAME = "client_mods"  #195 (line in Coconut source)
BASE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-base"  #196 (line in Coconut source)
EXTRA_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-extra"  #197 (line in Coconut source)
REMOVED_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-removed"  #198 (line in Coconut source)
STAGING_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-staging"  #199 (line in Coconut source)
DEDUPLICATE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-deduplicate"  #200 (line in Coconut source)


# Auto updater Constants

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  #205 (line in Coconut source)

MODLOADER = "Forge"  #207 (line in Coconut source)
WRONG_MODLOADERS = ["Fabric", "Quilt"]  #208 (line in Coconut source)
MAYBE_WRONG_MODLOADERS = ["NeoForge",]  #209 (line in Coconut source)

COMPONENT_SEPS = [("-", 2), ("(", 1), ("+", 2), ("-", 1), ("_", 2), (" ", 2), ("+", 1), ("_", 1), (" ", 1)]  #211 (line in Coconut source)

NON_NAME_COMPONENT_REGEX = full_regex(r"[0-9].*|" + r"(?!cave|a$|ae2|rare|da)((forge|fabric|quilt|dist(ro)?|release|alpha|beta)(\..*)?|(mc|v|r)?[0-9.+_\-x()[\]]*(a|b|c|d|e|m)?)+")  #223 (line in Coconut source)

NAME_REGEXES_TO_SPACE = [regex(r) for r in (r"-", r"\+", r"_", r"\(", r"\)", r"%20", r"%5[bd]", r"%27", r"(neo)?forge\b", r"(NEO)?FORGE", r"(Neo)?Forge\b", r"fabric\b", r"FABRIC", r"Fabric\b", r"quilt\b", r"QUILT", r"Quilt\b", r"\bdist(ro)?", r"release", r"\balpha\b", r"\bALPHA\b", r"\bAlpha\b", r"\bbeta\b", r"\bBETA\b", r"\bBeta\b", r"MC", r"\bmc\b", r"1\.\d+", r"[.vV]0", r"[.vV]1", r"[.vV]2", r"[.vV]3", r"[.vV]4", r"[.vV]5", r"[.vV]6", r"[.vV]7", r"[.vV]8", r"[.vV]9", r"\.", r" / ", r" \| ", r"   ", r"  ", r" / ", r"\[ \]", r"  ")]  #228 (line in Coconut source)

CURSEFORGE_NAME_ELEMS_TO_STRIP = ["-", "Download", "Files", "Mods", "Minecraft", "Curseforge", "..."]  #279 (line in Coconut source)

AVOID_FILES_PUBLISHED_WITHIN = timedelta(days=7)  #289 (line in Coconut source)

MOD_PAGE_NAME_SUFFICES = (" - Files - Minecraft Mods - Curseforge", " - Comments - Minecraft Mods - Curseforge", " - Minecraft Mods - CurseForge")  #291 (line in Coconut source)

# must start with {mod_name} {modloader}
GOOGLE_QUERY_TEMPLATE = '{mod_name} {modloader} {mc_version_2} "Minecraft Mods" -Modpacks'  #298 (line in Coconut source)

CURSEFORGE_NAMES_FILE = os.path.join(ROOT_DIR, "curseforge_names.json")  #300 (line in Coconut source)
FIX_MOD_NAMES = False  #301 (line in Coconut source)

CURSEFORGE_API_FILE = os.path.join(ROOT_DIR, "curseforge_api.js")  #303 (line in Coconut source)

CURSEFORGE_QUERY_TEMPLATES = ['"{curseforge_name}"', "{core_curseforge_name}", "{mod_name}"]  #305 (line in Coconut source)

TIMESTAMP_FORMAT_REGEX = full_regex(r"(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)\.?(\d+)?Z")  #311 (line in Coconut source)

UPDATED_MODS_DIR_SUFFIX = "-updates"  #313 (line in Coconut source)
OLD_MODS_DIR_SUFFIX = "-old"  #314 (line in Coconut source)

MAX_DEBUG_RESULTS = 2  #316 (line in Coconut source)

CURSEFORGE_API_RETRIES = 3  #318 (line in Coconut source)
CURSEFORGE_API_RETRY_DELAY = 0.1  #319 (line in Coconut source)


# Server start constants

USE_GRAAL = not JPS_DEBUG  #324 (line in Coconut source)
USE_LARGE_PAGES = False  #325 (line in Coconut source)

OS_NAME = ("windows" if WINDOWS else "macos" if sys.platform == "darwin" else "linux")  #327 (line in Coconut source)

GRAAL_ZIP_NAME = "graalvm-jdk-22_{_coconut_format_0}-x64_bin.zip".format(_coconut_format_0=(OS_NAME))  #333 (line in Coconut source)
GRAAL_URL = "https://download.oracle.com/graalvm/22/latest/{_coconut_format_0}".format(_coconut_format_0=(GRAAL_ZIP_NAME))  #334 (line in Coconut source)

GRAAL_BASE_DIR = os.path.join(ROOT_DIR, "graal")  #336 (line in Coconut source)
GRAAL_ZIP_PATH = os.path.join(GRAAL_BASE_DIR, GRAAL_ZIP_NAME)  #337 (line in Coconut source)

# in my testing, G1 performs the best
CLIENT_GC = "G1"  # brucethemoose: G1, Shenandoah, or ZGenerational  #340 (line in Coconut source)
SERVER_GC = "G1"  # brucethemoose: G1 or Z  #341 (line in Coconut source)

def get_jvm_args(gc, vm, large_pages=USE_LARGE_PAGES):  #343 (line in Coconut source)
    args = ["-server", "-Xss4M", "-XX:+UnlockExperimentalVMOptions", "-XX:+UnlockDiagnosticVMOptions", "-XX:+AlwaysPreTouch", "-XX:+DisableExplicitGC", "-XX:+OptimizeStringConcat", "-XX:+UseCompressedOops", "-XX:+ScavengeBeforeFullGC", "-XX:+ParallelRefProcEnabled", "-XX:+AlwaysActAsServerClassMachine", "-XX:-DontCompileHugeMethods", "-XX:+UseFastUnorderedTimeStamps", "-XX:+UseCriticalJavaThreadPriority", "-XX:+EnableDynamicAgentLoading", "-XX:MaxGCPauseMillis=37", "-XX:MaxMetaspaceExpansion=64M", "-XX:NmethodSweepActivity=1", "-XX:ReservedCodeCacheSize=400M", "-XX:NonNMethodCodeHeapSize=12M", "-XX:ProfiledCodeHeapSize=194M", "-XX:NonProfiledCodeHeapSize=194M", "-XX:ThreadPriorityPolicy=1", "-XX:ConcGCThreads={_coconut_format_0}".format(_coconut_format_0=(psutil.cpu_count(logical=False) * 3 // 4))]  # brucethemoose: 1  # brucethemoose: 194M  # brucethemoose: 400M  # default: True  # default: 5M  # brucethemoose: 194M  # brucethemoose: 37; atm: 200; default: 200  # brucethemoose  # brucethemoose: 12M  # default: True  # brucethemoose: real cores - 2  # always  # brucethemoose  # always  # aikar-flags  # brucethemoose  # always  # brucethemoose  # default: True  # brucethemoose  # brucethemoose: 1  # java warning  #344 (line in Coconut source)
    if not JPS_DEBUG:  #379 (line in Coconut source)
        args += ["-XX:+PerfDisableSharedMem",]  # aikar-flags, brucethemoose  #380 (line in Coconut source)

    if large_pages:  #384 (line in Coconut source)
        args += ["-XX:+UseLargePages", "-XX:LargePageSizeInBytes=2M"]  # hilltty-flags, brucethemoose  # hilltty-flags, brucethemoose  #385 (line in Coconut source)

    if vm == "java":  #390 (line in Coconut source)
        args += ["-XX:+UseNUMA", "-XX:+UseVectorCmov", "-XX:MaxNodeLimit=240000", "-XX:NodeLimitFudgeFactor=8000"]  # hilltty-flags, brucethemoose: True; mukul1127: False  # brucethemoose: 240000  # brucethemoose: 8000  # brucethemoose  #391 (line in Coconut source)
    elif vm == "graal":  #397 (line in Coconut source)
        args += ["-XX:+EagerJVMCI", "-Dgraal.TuneInlinerExploration=1"]  # brucethemoose  # brucethemoose: 1  #398 (line in Coconut source)
    else:  #402 (line in Coconut source)
        raise ValueError("unknown java VM {_coconut_format_0!r}".format(_coconut_format_0=(vm)))  #403 (line in Coconut source)

    if gc == "G1":  #405 (line in Coconut source)
        args += ["-XX:+UseG1GC", "-XX:AllocatePrefetchStyle=3", "-XX:SurvivorRatio=32", "-XX:InitiatingHeapOccupancyPercent=10", "-XX:MaxTenuringThreshold=1", "-XX:G1ReservePercent=20", "-XX:G1NewSizePercent=23", "-XX:G1HeapRegionSize=32M", "-XX:G1MixedGCCountTarget=3", "-XX:G1RSetUpdatingPauseTimePercent=0", "-XX:G1HeapWastePercent=20", "-XX:G1SATBBufferEnqueueingThresholdPercent=30", "-XX:G1ConcMarkStepDurationMillis=5.0", "-XX:GCTimeRatio=99", "-XX:G1ConcRSHotCardLimit=16", "-XX:G1ConcRefinementServiceIntervalMillis=150"]  # brucethemoose: 16  # brucethemoose: 3  # brucethemoose: 23; atm: 30; aikar: 40  # brucethemoose: 20; atm: 5; default: 5  # brucethemoose: 30  # atm: 32; brucethemoose: 32; default: 8  # brucethemoose: 0; atm: 5; default: 10  # brucethemoose: 3; atm: 4; default: 8  # brucethemoose: 16M; atm: 8M; aikar: 16M  # brucethemoose: 5  # brucethemoose: 1; atm: 1; default: 15  # brucethemoose: 10; atm: 15; aikar: 20; default: 45  # brucethemoose: 99  # brucethemoose: 150  # brucethemoose: 20; atm: 20; aikar: 15  #406 (line in Coconut source)
    elif gc == "Shenandoah":  #427 (line in Coconut source)
        args += ["-XX:+UseShenandoahGC", "-XX:AllocatePrefetchStyle=1", "-XX:ShenandoahGCMode=iu", "-XX:ShenandoahGuaranteedGCInterval=1000000"]  # brucethemoose: 1  # brucethemoose: 1000000  # hilltty-flags  #428 (line in Coconut source)
    elif gc == "Z":  #434 (line in Coconut source)
        args += ["-XX:+UseZGC", "-XX:AllocatePrefetchStyle=1", "-XX:+ZGenerational"]  # brucethemoose (incompatible with -ZProactive; Java 21+)  # brucethemoose: 1  #435 (line in Coconut source)
    else:  #441 (line in Coconut source)
        raise ValueError("unknown java GC {_coconut_format_0!r}".format(_coconut_format_0=(gc)))  #442 (line in Coconut source)

    return args  #444 (line in Coconut source)


LOG4J_CONFIG_FILE = os.path.join(SERVER_DIR, "log4jconfig.xml")  #446 (line in Coconut source)
FML_ARGS = ["-Dfml.queryResult=confirm", "-Dfml.readTimeout=900", "-Dfml.ignoreInvalidMinecraftCertificates=true"] + (['-Dlog4j.configurationFile="' + LOG4J_CONFIG_FILE + '"',] if LOG4J_DEBUG and os.path.exists(LOG4J_CONFIG_FILE) else [])  #447 (line in Coconut source)

FORGE_ARGS = ["nogui",]  #456 (line in Coconut source)

START_ARGS = ["/HIGH", "/B", "/I"]  #458 (line in Coconut source)

JVM_ARGS_FILE = os.path.join(SERVER_DIR, "user_jvm_args.txt")  #460 (line in Coconut source)

if WINDOWS:  #462 (line in Coconut source)
    FORGE_LAUNCH_CMD = [os.path.join(SERVER_DIR, "run.bat"),]  #463 (line in Coconut source)
else:  #464 (line in Coconut source)
    FORGE_LAUNCH_CMD = ["sh", os.path.join(SERVER_DIR, "run.sh")]  #465 (line in Coconut source)

FORGE_INSTALLER_URL = format_vers("https://maven.minecraftforge.net/net/minecraftforge/forge/{mc_version}-{forge_version}/forge-{mc_version}-{forge_version}-installer.jar")  #467 (line in Coconut source)

FORGE_INSTALLER_JAR = format_vers("forge-{mc_version}-{forge_version}-installer.jar")  #469 (line in Coconut source)
FORGE_JAR = format_vers("forge-{mc_version}-{forge_version}.jar")  #470 (line in Coconut source)

OLD_JARS_REGEX = full_regex(format_vers(r"(forge-(?!{mc_version}-{forge_version})[0-9.]+-[0-9.]+(-installer)?|minecraft_server\.(?!{mc_version})[0-9.]+)\.jar"))  #472 (line in Coconut source)


# Client install constants

if sys.platform.startswith("win"):  #477 (line in Coconut source)
    MINECRAFT_DIR = fixpath("~/AppData/Roaming/.minecraft")  #478 (line in Coconut source)
elif sys.platform.startswith("darwin"):  #479 (line in Coconut source)
    MINECRAFT_DIR = fixpath("~/Library/Application Support/minecraft")  #480 (line in Coconut source)
else:  #481 (line in Coconut source)
    MINECRAFT_DIR = fixpath("~/.minecraft")  #482 (line in Coconut source)

PROFILES_FILE = os.path.join(MINECRAFT_DIR, "launcher_profiles.json")  #484 (line in Coconut source)

README_FILE = "README.txt"  #486 (line in Coconut source)

EXTRA_INSTALL_FILES += [README_FILE, FORGE_INSTALLER_JAR]  #488 (line in Coconut source)

YES_STRS = ["y", "yes", "t", "true", "1"]  #493 (line in Coconut source)

NO_STRS = ["n", "no", "f", "false", "0"]  #501 (line in Coconut source)


# Make launcher constants

LAUNCHER_FILE = first_that_exists(["~/Applications/Minecraft.app", "/Applications/Minecraft.app", r"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe", r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Minecraft Launcher\Minecraft Launcher.ink", r"C:\Users\Public\Desktop\Minecraft Launcher.ink"])  #512 (line in Coconut source)

MODPACK_NAME = "Evan's Modded Minecraft"  #520 (line in Coconut source)


# Searchable mods constants

SEARCHABLE_MODS_NAME = MODS_NAME + "-searchable"  #525 (line in Coconut source)
SEARCHABLE_CLIENT_MODS_NAME = CLIENT_MODS_NAME + "-searchable"  #526 (line in Coconut source)


# Binary search constants

BINARY_SEARCH_FILE = os.path.join(SERVER_DIR, "binary_search.json")  #531 (line in Coconut source)
