#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa95229a2

# Compiled with Coconut version 3.2.0-post_dev1

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev1', '', True)
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
import sys  #2 (line in Coconut source)
import subprocess  #3 (line in Coconut source)
import shutil  #4 (line in Coconut source)
import argparse  #5 (line in Coconut source)
import time  #6 (line in Coconut source)
try:  #7 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #7 (line in Coconut source)
except _coconut.NameError:  #7 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #7 (line in Coconut source)
sys = _coconut_sys  #7 (line in Coconut source)
if sys.version_info >= (3,):  #7 (line in Coconut source)
    from urllib.request import urlretrieve  #7 (line in Coconut source)
else:  #7 (line in Coconut source)
    from urllib2 import urlretrieve  #7 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #7 (line in Coconut source)
    sys = _coconut_sys_0  #7 (line in Coconut source)
try:  #8 (line in Coconut source)
    _coconut_sys_1 = sys  # type: ignore  #8 (line in Coconut source)
except _coconut.NameError:  #8 (line in Coconut source)
    _coconut_sys_1 = _coconut_sentinel  #8 (line in Coconut source)
sys = _coconut_sys  #8 (line in Coconut source)
if sys.version_info >= (3,):  #8 (line in Coconut source)
    from urllib.error import HTTPError  #8 (line in Coconut source)
else:  #8 (line in Coconut source)
    from urllib2 import HTTPError  #8 (line in Coconut source)
if _coconut_sys_1 is not _coconut_sentinel:  #8 (line in Coconut source)
    sys = _coconut_sys_1  #8 (line in Coconut source)
from contextlib import contextmanager  #9 (line in Coconut source)

import requests  #11 (line in Coconut source)

from minecraft_server_tools.constants import WINDOWS  #13 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_RAM  #13 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_ARGS  #13 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_INSTALLER_URL  #13 (line in Coconut source)
from minecraft_server_tools.constants import OLD_JARS_REGEX  #13 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_DIR  #13 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_JAR  #13 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_INSTALLER_JAR  #13 (line in Coconut source)
from minecraft_server_tools.constants import JVM_ARGS_FILE  #13 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_LAUNCH_CMD  #13 (line in Coconut source)
from minecraft_server_tools.constants import FML_ARGS  #13 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_RAM  #13 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_GC  #13 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_GC  #13 (line in Coconut source)
from minecraft_server_tools.constants import DOWNLOADS_PATH  #13 (line in Coconut source)
from minecraft_server_tools.constants import USE_GRAAL  #13 (line in Coconut source)
from minecraft_server_tools.constants import GRAAL_URL  #13 (line in Coconut source)
from minecraft_server_tools.constants import GRAAL_ZIP_PATH  #13 (line in Coconut source)
from minecraft_server_tools.constants import GRAAL_BASE_DIR  #13 (line in Coconut source)
from minecraft_server_tools.constants import get_jvm_args  #13 (line in Coconut source)
from minecraft_server_tools.constants import MODPACK_NAME  #13 (line in Coconut source)
from minecraft_server_tools.constants import START_ARGS  #13 (line in Coconut source)
from minecraft_server_tools.constants import WORLD_CONFIG_DIR  #13 (line in Coconut source)
from minecraft_server_tools.constants import DEFAULTCONFIGS_DIR  #13 (line in Coconut source)

FORGE_JAR_PATH = os.path.join(SERVER_DIR, FORGE_JAR)  #40 (line in Coconut source)
FORGE_INSTALLER_JAR_PATH = os.path.join(SERVER_DIR, FORGE_INSTALLER_JAR)  #41 (line in Coconut source)
DOWNLOADED_INSTALLER_PATH = os.path.join(DOWNLOADS_PATH, FORGE_INSTALLER_JAR)  #42 (line in Coconut source)


def remove_file_with_retry(filepath, max_retries=5, initial_delay=0.2):  #45 (line in Coconut source)
    """Remove a single file with retry logic for Windows file locking."""  #46 (line in Coconut source)
    delay = initial_delay  #47 (line in Coconut source)
    for attempt in range(max_retries):  #48 (line in Coconut source)
        try:  #49 (line in Coconut source)
            os.remove(filepath)  #50 (line in Coconut source)
            return True  #51 (line in Coconut source)
        except PermissionError:  #52 (line in Coconut source)
            if attempt < max_retries - 1:  #53 (line in Coconut source)
                time.sleep(delay)  #54 (line in Coconut source)
                delay *= 2  #55 (line in Coconut source)
    return False  #56 (line in Coconut source)



def remove_dir_if_exists(directory, max_retries=5, initial_delay=0.1):  #59 (line in Coconut source)
    """Remove a directory if it exists.

    Uses a multi-strategy approach for Windows/OneDrive file locking:
    1. Remove all files individually with retries
    2. Try os.rmdir() for the empty directory
    3. Fall back to Windows rmdir command if needed
    4. Retry with exponential backoff
    """  #67 (line in Coconut source)
    if not os.path.exists(directory):  #68 (line in Coconut source)
        return  #69 (line in Coconut source)

    dir_name = os.path.basename(directory)  #71 (line in Coconut source)

# First, remove all files individually
    for filename in os.listdir(directory):  #74 (line in Coconut source)
        filepath = os.path.join(directory, filename)  #75 (line in Coconut source)
        if os.path.isfile(filepath):  #76 (line in Coconut source)
            if not remove_file_with_retry(filepath):  #77 (line in Coconut source)
                print("  Warning: Could not remove file {_coconut_format_0}".format(_coconut_format_0=(filename)))  #78 (line in Coconut source)

# Now try to remove the empty directory with retries
    delay = initial_delay  #81 (line in Coconut source)
    for attempt in range(max_retries):  #82 (line in Coconut source)
        try:  #83 (line in Coconut source)
# Check if directory is empty
            remaining = os.listdir(directory)  #85 (line in Coconut source)
            if remaining:  #86 (line in Coconut source)
                print("  Warning: Directory {_coconut_format_0} not empty: {_coconut_format_1}".format(_coconut_format_0=(dir_name), _coconut_format_1=(remaining)))  #87 (line in Coconut source)
                return  #88 (line in Coconut source)

            os.rmdir(directory)  #90 (line in Coconut source)
            print("  Removed directory: {_coconut_format_0}".format(_coconut_format_0=(dir_name)))  #91 (line in Coconut source)
            return  #92 (line in Coconut source)
        except PermissionError:  #93 (line in Coconut source)
# On Windows, try using rmdir command as fallback
            if sys.platform == "win32" and attempt == max_retries // 2:  #95 (line in Coconut source)
                try:  #96 (line in Coconut source)
                    subprocess.run(["cmd", "/c", "rmdir", "/s", "/q", directory], check=True, capture_output=True)  #97 (line in Coconut source)
                    if not os.path.exists(directory):  #102 (line in Coconut source)
                        print("  Removed directory: {_coconut_format_0} (via rmdir)".format(_coconut_format_0=(dir_name)))  #103 (line in Coconut source)
                        return  #104 (line in Coconut source)
                except subprocess.CalledProcessError:  #105 (line in Coconut source)
                    pass  #106 (line in Coconut source)

            if attempt < max_retries - 1:  #108 (line in Coconut source)
                time.sleep(delay)  #109 (line in Coconut source)
                delay = min(delay * 1.5, 5.0)  # cap at 5 seconds  #110 (line in Coconut source)
            else:  #111 (line in Coconut source)
                print("  Warning: Could not remove {_coconut_format_0} - may be locked by OneDrive".format(_coconut_format_0=(dir_name)))  #112 (line in Coconut source)
        except OSError as e:  #113 (line in Coconut source)
            if attempt < max_retries - 1:  #114 (line in Coconut source)
                time.sleep(delay)  #115 (line in Coconut source)
                delay = min(delay * 1.5, 5.0)  #116 (line in Coconut source)
            else:  #117 (line in Coconut source)
                print("  Warning: Could not remove {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(dir_name), _coconut_format_1=(e)))  #118 (line in Coconut source)



@_coconut_tco  #121 (line in Coconut source)
def run_cmd(cmd, check=True, shell=False, get_output=False, quiet=False):  #121 (line in Coconut source)
    if not quiet:  #122 (line in Coconut source)
        print("> " + " ".join((str(x) for x in cmd)))  #123 (line in Coconut source)
    kwargs = _coconut.dict()  #124 (line in Coconut source)
    if get_output:  #125 (line in Coconut source)
        kwargs["stdout"] = kwargs["stderr"] = subprocess.PIPE  #126 (line in Coconut source)
    return _coconut_tail_call(subprocess.run, cmd, check=check, shell=shell, **kwargs)  #127 (line in Coconut source)



@_coconut_tco  #130 (line in Coconut source)
def run_high_priority(cmd, name=MODPACK_NAME):  #130 (line in Coconut source)
    if WINDOWS:  #131 (line in Coconut source)
        return _coconut_tail_call(run_cmd, ["START", name, "/WAIT"] + START_ARGS + cmd, shell=True)  #132 (line in Coconut source)
    else:  #133 (line in Coconut source)
        return _coconut_tail_call(run_cmd, cmd)  #134 (line in Coconut source)



def run_java(cmd):  #137 (line in Coconut source)
    with using_graal_java():  #138 (line in Coconut source)
        return run_high_priority(["java",] + cmd)  #139 (line in Coconut source)



def download_file(url, path):  #142 (line in Coconut source)
    dirname = os.path.dirname(path)  #143 (line in Coconut source)
    if not os.path.exists(dirname):  #144 (line in Coconut source)
        os.makedirs(dirname)  #145 (line in Coconut source)
    got = requests.get(url)  #146 (line in Coconut source)
    with open(path, "wb") as fobj:  #147 (line in Coconut source)
        fobj.write(got.content)  #148 (line in Coconut source)



def get_graal_bin_dir():  #151 (line in Coconut source)
    if not os.path.exists(GRAAL_ZIP_PATH):  #152 (line in Coconut source)
        print("Downloading Java GraalVM...")  #153 (line in Coconut source)
        download_file(GRAAL_URL, GRAAL_ZIP_PATH)  #154 (line in Coconut source)
        shutil.unpack_archive(GRAAL_ZIP_PATH, GRAAL_BASE_DIR)  #155 (line in Coconut source)

    graal_bin_dir = None  #157 (line in Coconut source)
    graal_bin_dir_time = 0  #158 (line in Coconut source)
    for entry in os.scandir(GRAAL_BASE_DIR):  #159 (line in Coconut source)
        if entry.is_dir():  #160 (line in Coconut source)
            modified_time = entry.stat().st_mtime  #161 (line in Coconut source)
            if modified_time > graal_bin_dir_time:  #162 (line in Coconut source)
                graal_bin_dir = os.path.join(entry.path, "bin")  #163 (line in Coconut source)
                graal_bin_dir_time = modified_time  #164 (line in Coconut source)

    return graal_bin_dir  #166 (line in Coconut source)



@contextmanager  #169 (line in Coconut source)
def using_graal_java():  #170 (line in Coconut source)
    if USE_GRAAL:  #171 (line in Coconut source)
        graal_bin_dir = get_graal_bin_dir()  #172 (line in Coconut source)

        print("(using GraalVM at: {_coconut_format_0!r})".format(_coconut_format_0=(graal_bin_dir)))  #174 (line in Coconut source)
        old_path = os.environ["PATH"]  #175 (line in Coconut source)
        os.environ["PATH"] = graal_bin_dir + ";" + os.environ["PATH"]  #176 (line in Coconut source)
        try:  #177 (line in Coconut source)
            yield  #178 (line in Coconut source)
        finally:  #179 (line in Coconut source)
            os.environ["PATH"] = old_path  #180 (line in Coconut source)
    else:  #181 (line in Coconut source)
        yield  #182 (line in Coconut source)



@_coconut_tco  #185 (line in Coconut source)
def get_cmd_output(cmd, quiet=True):  #185 (line in Coconut source)
    out = run_cmd(cmd, get_output=True, quiet=quiet)  #186 (line in Coconut source)
    return _coconut_tail_call((out.stdout.decode("utf-8") + "\n" + out.stderr.decode("utf-8")).strip)  #187 (line in Coconut source)



def install_forge_server():  #190 (line in Coconut source)
    print("Installing forge from installer {_coconut_format_0}...".format(_coconut_format_0=(FORGE_INSTALLER_JAR_PATH)))  #191 (line in Coconut source)
    run_java(["-jar", FORGE_INSTALLER_JAR_PATH, "--installServer"])  #192 (line in Coconut source)



def move_forge_installer():  #195 (line in Coconut source)
    if not os.path.exists(DOWNLOADED_INSTALLER_PATH):  #196 (line in Coconut source)
        return False  #197 (line in Coconut source)
    os.rename(DOWNLOADED_INSTALLER_PATH, FORGE_INSTALLER_JAR_PATH)  #198 (line in Coconut source)
    return True  #199 (line in Coconut source)



def ensure_forge_server():  #202 (line in Coconut source)
    if not os.path.exists(FORGE_INSTALLER_JAR_PATH):  #203 (line in Coconut source)
        print("Downloading forge installer {_coconut_format_0}...".format(_coconut_format_0=(FORGE_INSTALLER_JAR_PATH)))  #204 (line in Coconut source)
        if not move_forge_installer():  #205 (line in Coconut source)
            try:  #206 (line in Coconut source)
                urlretrieve(FORGE_INSTALLER_URL, FORGE_INSTALLER_JAR_PATH)  #207 (line in Coconut source)
            except HTTPError:  #208 (line in Coconut source)
                print("Automatic download failed; please download from: {_coconut_format_0}".format(_coconut_format_0=(FORGE_INSTALLER_URL)))  #209 (line in Coconut source)
                input("Press Enter to continue.")  #210 (line in Coconut source)
                assert move_forge_installer()  #211 (line in Coconut source)
        install_forge_server()  #212 (line in Coconut source)



def clean_forge_jars(dir_to_clean=SERVER_DIR):  #215 (line in Coconut source)
    for fname in os.listdir(dir_to_clean):  #216 (line in Coconut source)
        if OLD_JARS_REGEX.match(fname) is not None:  #217 (line in Coconut source)
            print("Removing old jar {_coconut_format_0}...".format(_coconut_format_0=(fname)))  #218 (line in Coconut source)
            os.remove(os.path.join(dir_to_clean, fname))  #219 (line in Coconut source)



def check_if_graal(java="java"):  #222 (line in Coconut source)
    try:  #223 (line in Coconut source)
        return "GraalVM" in get_cmd_output([java, "-version"])  #224 (line in Coconut source)
    except FileNotFoundError:  #225 (line in Coconut source)
        return None  #226 (line in Coconut source)



def get_java_args(client=False):  #229 (line in Coconut source)
    graal = check_if_graal()  #230 (line in Coconut source)
    if graal != USE_GRAAL:  #231 (line in Coconut source)
        print("WARNING: Should be using GraalVM={_coconut_format_0} but got GraalVM={_coconut_format_1}.".format(_coconut_format_0=(USE_GRAAL), _coconut_format_1=(graal)))  #232 (line in Coconut source)
    if client:  #233 (line in Coconut source)
        ram = CLIENT_RAM  #234 (line in Coconut source)
        gc = CLIENT_GC  #235 (line in Coconut source)
    else:  #236 (line in Coconut source)
        ram = SERVER_RAM  #237 (line in Coconut source)
        gc = SERVER_GC  #238 (line in Coconut source)
    java_args = (["-Xmx" + ram, "-Xms" + ram] + get_jvm_args(gc=gc, vm="graal" if graal else "java") + FML_ARGS)  #239 (line in Coconut source)
    print("\tUsing JVM args: {_coconut_format_0}".format(_coconut_format_0=(' '.join(java_args))))  #244 (line in Coconut source)
    return java_args  #245 (line in Coconut source)



def fix_run_bat():  #248 (line in Coconut source)
    with open(os.path.join(SERVER_DIR, "run.bat"), "r+") as run_bat:  #249 (line in Coconut source)
        content = run_bat.read()  #250 (line in Coconut source)
        run_bat.seek(0)  #251 (line in Coconut source)
        run_bat.truncate()  #252 (line in Coconut source)
        run_bat.write(content.replace("pause", "exit"))  #253 (line in Coconut source)



def write_jvm_args():  #256 (line in Coconut source)
    with open(JVM_ARGS_FILE, "w") as jvm_args_file:  #257 (line in Coconut source)
        jvm_args_file.write("\n".join(get_java_args()) + "\n")  #258 (line in Coconut source)



def clean_world_configs():  #261 (line in Coconut source)
    if os.path.exists(WORLD_CONFIG_DIR):  #262 (line in Coconut source)
        print("Deleting {_coconut_format_0!r}...".format(_coconut_format_0=(WORLD_CONFIG_DIR)))  #263 (line in Coconut source)
        remove_dir_if_exists(WORLD_CONFIG_DIR)  #264 (line in Coconut source)
    else:  #265 (line in Coconut source)
        print("WARNING: Couldn't find {_coconut_format_0!r}.".format(_coconut_format_0=(WORLD_CONFIG_DIR)))  #266 (line in Coconut source)



def copy_new_world_configs():  #269 (line in Coconut source)
    if os.path.exists(WORLD_CONFIG_DIR):  #270 (line in Coconut source)
        print("\nLooking for new configs...")  #271 (line in Coconut source)
        for fname in os.listdir(WORLD_CONFIG_DIR):  #272 (line in Coconut source)
            defaultconfigs_path = os.path.join(DEFAULTCONFIGS_DIR, fname)  #273 (line in Coconut source)
            if not os.path.exists(defaultconfigs_path):  #274 (line in Coconut source)
                world_path = os.path.join(WORLD_CONFIG_DIR, fname)  #275 (line in Coconut source)
                print("\tCopying {_coconut_format_0!r} to {_coconut_format_1!r}...".format(_coconut_format_0=(world_path), _coconut_format_1=(defaultconfigs_path)))  #276 (line in Coconut source)
                shutil.copy(world_path, defaultconfigs_path)  #277 (line in Coconut source)



def start_server(dry_run=False):  #280 (line in Coconut source)
    clean_forge_jars()  #281 (line in Coconut source)
    ensure_forge_server()  #282 (line in Coconut source)
    fix_run_bat()  #283 (line in Coconut source)
    if not dry_run:  #284 (line in Coconut source)
        clean_world_configs()  #285 (line in Coconut source)
        with using_graal_java():  #286 (line in Coconut source)
            write_jvm_args()  #287 (line in Coconut source)
            if os.path.exists(FORGE_JAR_PATH):  #288 (line in Coconut source)
                run_java(get_java_args() + [FORGE_JAR_PATH,] + FORGE_ARGS)  #289 (line in Coconut source)
            else:  #290 (line in Coconut source)
                run_high_priority(FORGE_LAUNCH_CMD + FORGE_ARGS)  #291 (line in Coconut source)
        copy_new_world_configs()  #292 (line in Coconut source)



@_coconut_tco  #295 (line in Coconut source)
def parse_args():  #295 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Launch the Minecraft server with optimized JVM settings.")  #296 (line in Coconut source)
    parser.add_argument("--dry-run", action="store_true", help="Prepare server files without actually launching the server")  #299 (line in Coconut source)
    return _coconut_tail_call(parser.parse_args)  #304 (line in Coconut source)



def main():  #307 (line in Coconut source)
    args = parse_args()  #308 (line in Coconut source)
    start_server(dry_run=args.dry_run)  #309 (line in Coconut source)



if __name__ == "__main__":  #312 (line in Coconut source)
    main()  #313 (line in Coconut source)
