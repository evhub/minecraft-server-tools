#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7832c083

# Compiled with Coconut version 3.1.1-post_dev1

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.1-post_dev1', '', True)
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
try:  #4 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #4 (line in Coconut source)
except _coconut.NameError:  #4 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #4 (line in Coconut source)
sys = _coconut_sys  #4 (line in Coconut source)
if sys.version_info >= (3,):  #4 (line in Coconut source)
    from urllib.request import urlretrieve  #4 (line in Coconut source)
else:  #4 (line in Coconut source)
    from urllib2 import urlretrieve  #4 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #4 (line in Coconut source)
    sys = _coconut_sys_0  #4 (line in Coconut source)
try:  #5 (line in Coconut source)
    _coconut_sys_1 = sys  # type: ignore  #5 (line in Coconut source)
except _coconut.NameError:  #5 (line in Coconut source)
    _coconut_sys_1 = _coconut_sentinel  #5 (line in Coconut source)
sys = _coconut_sys  #5 (line in Coconut source)
if sys.version_info >= (3,):  #5 (line in Coconut source)
    from urllib.error import HTTPError  #5 (line in Coconut source)
else:  #5 (line in Coconut source)
    from urllib2 import HTTPError  #5 (line in Coconut source)
if _coconut_sys_1 is not _coconut_sentinel:  #5 (line in Coconut source)
    sys = _coconut_sys_1  #5 (line in Coconut source)

from minecraft_server_tools.constants import WINDOWS  #7 (line in Coconut source)
from minecraft_server_tools.constants import JAVA_EXECUTABLE  #7 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_RAM  #7 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_ARGS  #7 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_INSTALLER_URL  #7 (line in Coconut source)
from minecraft_server_tools.constants import OLD_JARS_REGEX  #7 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_DIR  #7 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_JAR  #7 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_INSTALLER_JAR  #7 (line in Coconut source)
from minecraft_server_tools.constants import JVM_ARGS_FILE  #7 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_LAUNCH_CMD  #7 (line in Coconut source)
from minecraft_server_tools.constants import FML_ARGS  #7 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_RAM  #7 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_GC  #7 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_GC  #7 (line in Coconut source)
from minecraft_server_tools.constants import DOWNLOADS_PATH  #7 (line in Coconut source)
from minecraft_server_tools.constants import get_jvm_args  #7 (line in Coconut source)

FORGE_JAR_PATH = os.path.join(SERVER_DIR, FORGE_JAR)  #27 (line in Coconut source)
FORGE_INSTALLER_JAR_PATH = os.path.join(SERVER_DIR, FORGE_INSTALLER_JAR)  #28 (line in Coconut source)
DOWNLOADED_INSTALLER_PATH = os.path.join(DOWNLOADS_PATH, FORGE_INSTALLER_JAR)  #29 (line in Coconut source)


@_coconut_tco  #32 (line in Coconut source)
def run_cmd(cmd, check=True, shell=False, get_output=False, quiet=False):  #32 (line in Coconut source)
    if not quiet:  #33 (line in Coconut source)
        print("> " + " ".join((str(x) for x in cmd)))  #34 (line in Coconut source)
    kwargs = _coconut.dict()  #35 (line in Coconut source)
    if get_output:  #36 (line in Coconut source)
        kwargs["stdout"] = kwargs["stderr"] = subprocess.PIPE  #37 (line in Coconut source)
    return _coconut_tail_call(subprocess.run, cmd, check=check, shell=shell, **kwargs)  #38 (line in Coconut source)



@_coconut_tco  #41 (line in Coconut source)
def run_high_priority(cmd, name="Minecraft Server"):  #41 (line in Coconut source)
    if WINDOWS:  #42 (line in Coconut source)
        return _coconut_tail_call(run_cmd, ["START", name, "/B", "/I", "/WAIT", "/HIGH"] + cmd, shell=True)  #43 (line in Coconut source)
    else:  #44 (line in Coconut source)
        return _coconut_tail_call(run_cmd, cmd)  #45 (line in Coconut source)



@_coconut_tco  #48 (line in Coconut source)
def run_java(cmd):  #48 (line in Coconut source)
    return _coconut_tail_call(run_high_priority, [JAVA_EXECUTABLE,] + cmd)  #48 (line in Coconut source)



@_coconut_tco  #51 (line in Coconut source)
def get_cmd_output(cmd, quiet=True):  #51 (line in Coconut source)
    out = run_cmd(cmd, get_output=True, quiet=quiet)  #52 (line in Coconut source)
    return _coconut_tail_call((out.stdout.decode("utf-8") + "\n" + out.stderr.decode("utf-8")).strip)  #53 (line in Coconut source)



def install_forge_server():  #56 (line in Coconut source)
    print("Installing forge from installer {_coconut_format_0}...".format(_coconut_format_0=(FORGE_INSTALLER_JAR_PATH)))  #57 (line in Coconut source)
    run_java(["-jar", FORGE_INSTALLER_JAR_PATH, "--installServer"])  #58 (line in Coconut source)



def move_forge_installer():  #61 (line in Coconut source)
    if not os.path.exists(DOWNLOADED_INSTALLER_PATH):  #62 (line in Coconut source)
        return False  #63 (line in Coconut source)
    os.rename(DOWNLOADED_INSTALLER_PATH, FORGE_INSTALLER_JAR_PATH)  #64 (line in Coconut source)
    return True  #65 (line in Coconut source)



def ensure_forge_server():  #68 (line in Coconut source)
    if not os.path.exists(FORGE_INSTALLER_JAR_PATH):  #69 (line in Coconut source)
        print("Downloading forge installer {_coconut_format_0}...".format(_coconut_format_0=(FORGE_INSTALLER_JAR_PATH)))  #70 (line in Coconut source)
        if not move_forge_installer():  #71 (line in Coconut source)
            try:  #72 (line in Coconut source)
                urlretrieve(FORGE_INSTALLER_URL, FORGE_INSTALLER_JAR_PATH)  #73 (line in Coconut source)
            except HTTPError:  #74 (line in Coconut source)
                print("Automatic download failed; please download from: {_coconut_format_0}".format(_coconut_format_0=(FORGE_INSTALLER_URL)))  #75 (line in Coconut source)
                input("Press Enter to continue.")  #76 (line in Coconut source)
                assert move_forge_installer()  #77 (line in Coconut source)
        install_forge_server()  #78 (line in Coconut source)



def clean_forge_jars(dir_to_clean=SERVER_DIR):  #81 (line in Coconut source)
    for fname in os.listdir(dir_to_clean):  #82 (line in Coconut source)
        if OLD_JARS_REGEX.match(fname) is not None:  #83 (line in Coconut source)
            print("Removing old jar {_coconut_format_0}...".format(_coconut_format_0=(fname)))  #84 (line in Coconut source)
            os.remove(os.path.join(dir_to_clean, fname))  #85 (line in Coconut source)



def check_if_graal(java="java"):  #88 (line in Coconut source)
    try:  #89 (line in Coconut source)
        return "GraalVM" in get_cmd_output([java, "-version"])  #90 (line in Coconut source)
    except FileNotFoundError:  #91 (line in Coconut source)
        return None  #92 (line in Coconut source)



def get_java_args(client=False):  #95 (line in Coconut source)
    if client:  #96 (line in Coconut source)
        ram = CLIENT_RAM  #97 (line in Coconut source)
        gc = CLIENT_GC  #98 (line in Coconut source)
    else:  #99 (line in Coconut source)
        ram = SERVER_RAM  #100 (line in Coconut source)
        gc = SERVER_GC  #101 (line in Coconut source)
    return (["-Xmx" + ram, "-Xms" + ram] + get_jvm_args(gc=gc, vm="graal" if check_if_graal() else "java") + FML_ARGS)  #102 (line in Coconut source)



def fix_run_bat():  #109 (line in Coconut source)
    with open(os.path.join(SERVER_DIR, "run.bat"), "r+") as run_bat:  #110 (line in Coconut source)
        content = run_bat.read()  #111 (line in Coconut source)
        run_bat.seek(0)  #112 (line in Coconut source)
        run_bat.truncate()  #113 (line in Coconut source)
        run_bat.write(content.replace("pause", "exit"))  #114 (line in Coconut source)



def write_jvm_args():  #117 (line in Coconut source)
    with open(JVM_ARGS_FILE, "w") as jvm_args_file:  #118 (line in Coconut source)
        jvm_args_file.write("\n".join(get_java_args()) + "\n")  #119 (line in Coconut source)



def start_server(dry_run=False):  #122 (line in Coconut source)
    clean_forge_jars()  #123 (line in Coconut source)
    ensure_forge_server()  #124 (line in Coconut source)
    fix_run_bat()  #125 (line in Coconut source)
    write_jvm_args()  #126 (line in Coconut source)
    if not dry_run:  #127 (line in Coconut source)
        if os.path.exists(FORGE_JAR_PATH):  #128 (line in Coconut source)
            run_java(get_java_args() + [FORGE_JAR_PATH,] + FORGE_ARGS)  #129 (line in Coconut source)
        else:  #130 (line in Coconut source)
            run_high_priority(FORGE_LAUNCH_CMD + FORGE_ARGS)  #131 (line in Coconut source)



def main():  #134 (line in Coconut source)
    start_server(dry_run="--dry-run" in sys.argv)  #135 (line in Coconut source)



if __name__ == "__main__":  #138 (line in Coconut source)
    main()  #139 (line in Coconut source)
