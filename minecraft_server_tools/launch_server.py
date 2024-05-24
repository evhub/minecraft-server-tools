#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x126b3597

# Compiled with Coconut version 3.1.0-post_dev12

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.0-post_dev12', '', True)
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
import shutil  #3 (line in Coconut source)
import subprocess  #4 (line in Coconut source)
try:  #5 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #5 (line in Coconut source)
except _coconut.NameError:  #5 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #5 (line in Coconut source)
sys = _coconut_sys  #5 (line in Coconut source)
if sys.version_info >= (3,):  #5 (line in Coconut source)
    from urllib.request import urlretrieve  #5 (line in Coconut source)
else:  #5 (line in Coconut source)
    from urllib2 import urlretrieve  #5 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #5 (line in Coconut source)
    sys = _coconut_sys_0  #5 (line in Coconut source)
try:  #6 (line in Coconut source)
    _coconut_sys_1 = sys  # type: ignore  #6 (line in Coconut source)
except _coconut.NameError:  #6 (line in Coconut source)
    _coconut_sys_1 = _coconut_sentinel  #6 (line in Coconut source)
sys = _coconut_sys  #6 (line in Coconut source)
if sys.version_info >= (3,):  #6 (line in Coconut source)
    from urllib.error import HTTPError  #6 (line in Coconut source)
else:  #6 (line in Coconut source)
    from urllib2 import HTTPError  #6 (line in Coconut source)
if _coconut_sys_1 is not _coconut_sentinel:  #6 (line in Coconut source)
    sys = _coconut_sys_1  #6 (line in Coconut source)

from minecraft_server_tools.constants import WINDOWS  #8 (line in Coconut source)
from minecraft_server_tools.constants import JAVA_EXECUTABLE  #8 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_RAM  #8 (line in Coconut source)
from minecraft_server_tools.constants import BASE_JVM_ARGS  #8 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_ARGS  #8 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_INSTALLER_URL  #8 (line in Coconut source)
from minecraft_server_tools.constants import OLD_JARS_REGEX  #8 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_DIR  #8 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_JAR  #8 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_INSTALLER_JAR  #8 (line in Coconut source)
from minecraft_server_tools.constants import JVM_ARGS_FILE  #8 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_LAUNCH_CMD  #8 (line in Coconut source)
from minecraft_server_tools.constants import FML_ARGS  #8 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_RAM  #8 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_GC  #8 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_GC  #8 (line in Coconut source)
from minecraft_server_tools.constants import DOWNLOADS_PATH  #8 (line in Coconut source)
from minecraft_server_tools.constants import get_jvm_args_for_gc  #8 (line in Coconut source)

FORGE_JAR_PATH = os.path.join(SERVER_DIR, FORGE_JAR)  #29 (line in Coconut source)
FORGE_INSTALLER_JAR_PATH = os.path.join(SERVER_DIR, FORGE_INSTALLER_JAR)  #30 (line in Coconut source)
DOWNLOADED_INSTALLER_PATH = os.path.join(DOWNLOADS_PATH, FORGE_INSTALLER_JAR)  #31 (line in Coconut source)


@_coconut_tco  #34 (line in Coconut source)
def run_cmd(cmd, check=True, shell=False):  #34 (line in Coconut source)
    print("> " + " ".join((str(x) for x in cmd)))  #35 (line in Coconut source)
    return _coconut_tail_call(subprocess.run, cmd, check=check, shell=shell)  #36 (line in Coconut source)



@_coconut_tco  #39 (line in Coconut source)
def run_high_priority(cmd, name="Minecraft Server"):  #39 (line in Coconut source)
    if WINDOWS:  #40 (line in Coconut source)
        return _coconut_tail_call(run_cmd, ["START", name, "/B", "/I", "/WAIT", "/HIGH"] + cmd, shell=True)  #41 (line in Coconut source)
    else:  #42 (line in Coconut source)
        return _coconut_tail_call(run_cmd, cmd)  #43 (line in Coconut source)



@_coconut_tco  #46 (line in Coconut source)
def run_java(cmd):  #46 (line in Coconut source)
    return _coconut_tail_call(run_high_priority, [JAVA_EXECUTABLE,] + cmd)  #46 (line in Coconut source)



def install_forge_server():  #49 (line in Coconut source)
    print("Installing forge from installer {_coconut_format_0}...".format(_coconut_format_0=(FORGE_INSTALLER_JAR_PATH)))  #50 (line in Coconut source)
    run_java(["-jar", FORGE_INSTALLER_JAR_PATH, "--installServer"])  #51 (line in Coconut source)



def copy_forge_installer():  #54 (line in Coconut source)
    if not os.path.exists(DOWNLOADED_INSTALLER_PATH):  #55 (line in Coconut source)
        return False  #56 (line in Coconut source)
    shutil.copy(DOWNLOADED_INSTALLER_PATH, FORGE_INSTALLER_JAR_PATH)  #57 (line in Coconut source)
    return True  #58 (line in Coconut source)



def ensure_forge_server():  #61 (line in Coconut source)
    if not os.path.exists(FORGE_INSTALLER_JAR_PATH):  #62 (line in Coconut source)
        print("Downloading forge installer {_coconut_format_0}...".format(_coconut_format_0=(FORGE_INSTALLER_JAR_PATH)))  #63 (line in Coconut source)
        if not copy_forge_installer():  #64 (line in Coconut source)
            try:  #65 (line in Coconut source)
                urlretrieve(FORGE_INSTALLER_URL, FORGE_INSTALLER_JAR_PATH)  #66 (line in Coconut source)
            except HTTPError:  #67 (line in Coconut source)
                print("Automatic download failed; please download from: {_coconut_format_0}".format(_coconut_format_0=(FORGE_INSTALLER_URL)))  #68 (line in Coconut source)
                input("Press Enter to continue.")  #69 (line in Coconut source)
                assert copy_forge_installer()  #70 (line in Coconut source)
        install_forge_server()  #71 (line in Coconut source)



def clean_forge_jars(dir_to_clean=SERVER_DIR):  #74 (line in Coconut source)
    for fname in os.listdir(dir_to_clean):  #75 (line in Coconut source)
        if OLD_JARS_REGEX.match(fname) is not None:  #76 (line in Coconut source)
            print("Removing old jar {_coconut_format_0}...".format(_coconut_format_0=(fname)))  #77 (line in Coconut source)
            os.remove(os.path.join(dir_to_clean, fname))  #78 (line in Coconut source)



def get_java_args(client=False):  #81 (line in Coconut source)
    if client:  #82 (line in Coconut source)
        ram = CLIENT_RAM  #83 (line in Coconut source)
        gc = CLIENT_GC  #84 (line in Coconut source)
    else:  #85 (line in Coconut source)
        ram = SERVER_RAM  #86 (line in Coconut source)
        gc = SERVER_GC  #87 (line in Coconut source)
    args = (["-Xmx" + ram, "-Xms" + ram] + BASE_JVM_ARGS + get_jvm_args_for_gc(gc))  #88 (line in Coconut source)
    if not client:  #93 (line in Coconut source)
        args += FML_ARGS  #94 (line in Coconut source)
    return args  #95 (line in Coconut source)



def fix_run_bat():  #98 (line in Coconut source)
    with open(os.path.join(SERVER_DIR, "run.bat"), "r+") as run_bat:  #99 (line in Coconut source)
        content = run_bat.read()  #100 (line in Coconut source)
        run_bat.seek(0)  #101 (line in Coconut source)
        run_bat.truncate()  #102 (line in Coconut source)
        run_bat.write(content.replace("pause", "exit"))  #103 (line in Coconut source)



def write_jvm_args():  #106 (line in Coconut source)
    with open(JVM_ARGS_FILE, "w") as jvm_args_file:  #107 (line in Coconut source)
        jvm_args_file.write("\n".join(get_java_args()) + "\n")  #108 (line in Coconut source)



def start_server(dry_run=False):  #111 (line in Coconut source)
    clean_forge_jars()  #112 (line in Coconut source)
    ensure_forge_server()  #113 (line in Coconut source)
    fix_run_bat()  #114 (line in Coconut source)
    write_jvm_args()  #115 (line in Coconut source)
    if not dry_run:  #116 (line in Coconut source)
        if os.path.exists(FORGE_JAR_PATH):  #117 (line in Coconut source)
            run_java(get_java_args() + [FORGE_JAR_PATH,] + FORGE_ARGS)  #118 (line in Coconut source)
        else:  #119 (line in Coconut source)
            run_high_priority(FORGE_LAUNCH_CMD + FORGE_ARGS)  #120 (line in Coconut source)



def main():  #123 (line in Coconut source)
    start_server(dry_run="--dry-run" in sys.argv)  #124 (line in Coconut source)



if __name__ == "__main__":  #127 (line in Coconut source)
    main()  #128 (line in Coconut source)
