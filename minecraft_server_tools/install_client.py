#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x24b8c8a4

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
import zipfile  #4 (line in Coconut source)
import tempfile  #5 (line in Coconut source)
import json  #6 (line in Coconut source)
from contextlib import contextmanager  #7 (line in Coconut source)

from tqdm import tqdm  #9 (line in Coconut source)

from minecraft_server_tools import sync_mods  #11 (line in Coconut source)
from minecraft_server_tools import launch_server  #11 (line in Coconut source)
from minecraft_server_tools.constants import WINDOWS  #12 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_DIR  #12 (line in Coconut source)
from minecraft_server_tools.constants import MINECRAFT_DIR  #12 (line in Coconut source)
from minecraft_server_tools.constants import EXTRA_INSTALL_FOLDERS  #12 (line in Coconut source)
from minecraft_server_tools.constants import EXTRA_INSTALL_FILES  #12 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_INSTALLER_JAR  #12 (line in Coconut source)
from minecraft_server_tools.constants import README_FILE  #12 (line in Coconut source)
from minecraft_server_tools.constants import MOD_ZIP_PATH  #12 (line in Coconut source)
from minecraft_server_tools.constants import OPTIONAL_INSTALL_FILES  #12 (line in Coconut source)
from minecraft_server_tools.constants import OPTIONAL_INSTALL_FOLDERS  #12 (line in Coconut source)
from minecraft_server_tools.constants import MODS_NAME  #12 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_MODS_NAME  #12 (line in Coconut source)
from minecraft_server_tools.constants import YES_STRS  #12 (line in Coconut source)
from minecraft_server_tools.constants import PROFILES_FILE  #12 (line in Coconut source)

MINECRAFT_MODS_DIR = os.path.join(MINECRAFT_DIR, MODS_NAME)  #29 (line in Coconut source)


def sync_client_mods(source_dir):  #32 (line in Coconut source)
    print("\nInstalling mods...")  #33 (line in Coconut source)
    all_client_mods = sync_mods.get_location_table_for(os.path.join(source_dir, MODS_NAME))  #34 (line in Coconut source)
    all_client_mods.update(sync_mods.get_location_table_for(os.path.join(source_dir, CLIENT_MODS_NAME)))  #35 (line in Coconut source)

    current_client_mods = sync_mods.get_location_table_for(MINECRAFT_MODS_DIR)  #37 (line in Coconut source)

    sync_mods.set_mods_from_to(all_client_mods, current_client_mods, MINECRAFT_MODS_DIR)  #39 (line in Coconut source)



def install_extras(source_dir, do_optional=True, clean=True):  #42 (line in Coconut source)
    print("\nInstalling other files/folders...")  #43 (line in Coconut source)
    for install_dir in EXTRA_INSTALL_FOLDERS + (OPTIONAL_INSTALL_FOLDERS if do_optional else []):  #44 (line in Coconut source)
        from_dir = os.path.join(source_dir, install_dir)  #45 (line in Coconut source)
        to_dir = os.path.join(MINECRAFT_DIR, install_dir)  #46 (line in Coconut source)
        print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_dir)))  #47 (line in Coconut source)
        cleaned = False  #48 (line in Coconut source)
        if clean and os.path.exists(to_dir):  #49 (line in Coconut source)
            shutil.rmtree(to_dir)  #50 (line in Coconut source)
            cleaned = True  #51 (line in Coconut source)
        if os.path.exists(from_dir):  #52 (line in Coconut source)
            shutil.copytree(from_dir, to_dir, dirs_exist_ok=True)  #53 (line in Coconut source)
        elif cleaned:  #54 (line in Coconut source)
            print("\t\t(cleaned)")  #55 (line in Coconut source)
        else:  #56 (line in Coconut source)
            print("\t\t(skipped)")  #57 (line in Coconut source)

    for install_file in EXTRA_INSTALL_FILES + (OPTIONAL_INSTALL_FILES if do_optional else []):  #59 (line in Coconut source)
        from_path = os.path.join(source_dir, install_file)  #60 (line in Coconut source)
        to_path = os.path.join(MINECRAFT_DIR, install_file)  #61 (line in Coconut source)
        print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_file)))  #62 (line in Coconut source)
        if os.path.exists(from_path):  #63 (line in Coconut source)
            shutil.copy(from_path, to_path)  #64 (line in Coconut source)
        else:  #65 (line in Coconut source)
            print("\t\t(skipped)")  #66 (line in Coconut source)



def ensure_forge_client(source_dir):  #69 (line in Coconut source)
    if not os.path.exists(os.path.join(MINECRAFT_DIR, FORGE_INSTALLER_JAR)):  #70 (line in Coconut source)
        print("\nOpening forge installer; select 'Install client' and press 'Ok'.")  #71 (line in Coconut source)
        launch_server.run_java(["-jar", os.path.join(source_dir, FORGE_INSTALLER_JAR)])  #72 (line in Coconut source)



def get_paths_to_zip():  #75 (line in Coconut source)
    for install_fname in (EXTRA_INSTALL_FILES + OPTIONAL_INSTALL_FILES):  #76 (line in Coconut source)
        yield os.path.join(MINECRAFT_DIR, install_fname)  #80 (line in Coconut source)
    for install_dirname in (EXTRA_INSTALL_FOLDERS + OPTIONAL_INSTALL_FOLDERS + [MODS_NAME,]):  #81 (line in Coconut source)
        install_dirpath = os.path.join(MINECRAFT_DIR, install_dirname)  #86 (line in Coconut source)
        for dirpath, dirnames, filenames in os.walk(install_dirpath):  #87 (line in Coconut source)
            yield dirpath  #88 (line in Coconut source)
            for fname in filenames:  #89 (line in Coconut source)
                yield os.path.join(dirpath, fname)  #90 (line in Coconut source)



def zip_mods():  #93 (line in Coconut source)
    print("\nZipping mod files to {_coconut_format_0}...".format(_coconut_format_0=(MOD_ZIP_PATH)))  #94 (line in Coconut source)
    with zipfile.ZipFile(MOD_ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:  #95 (line in Coconut source)
        for install_path in tqdm(list(get_paths_to_zip())):  #96 (line in Coconut source)
            zf.write(install_path, os.path.relpath(install_path, MINECRAFT_DIR))  #97 (line in Coconut source)



def set_jvm_args():  #100 (line in Coconut source)
    print("\nSetting JVM arguments...")  #101 (line in Coconut source)
    java_args = " ".join(launch_server.get_java_args(client=True))  #102 (line in Coconut source)
    with open(PROFILES_FILE, "r+") as profiles_file:  #103 (line in Coconut source)
        top_level_json = json.load(profiles_file)  #104 (line in Coconut source)
        top_level_json["profiles"]["forge"]["javaArgs"] = java_args  #105 (line in Coconut source)

        profiles_file.seek(0)  #107 (line in Coconut source)
        profiles_file.truncate()  #108 (line in Coconut source)
        json.dump(top_level_json, profiles_file, indent=2)  #109 (line in Coconut source)
    print("\tto: {_coconut_format_0}".format(_coconut_format_0=(java_args)))  #110 (line in Coconut source)



def open_readme():  #113 (line in Coconut source)
    installed_readme = os.path.join(MINECRAFT_DIR, README_FILE)  #114 (line in Coconut source)
    print("\nOpening {_coconut_format_0}...".format(_coconut_format_0=(installed_readme)))  #115 (line in Coconut source)
    if WINDOWS:  #116 (line in Coconut source)
        launch_server.run_cmd(["explorer", installed_readme], check=False)  #117 (line in Coconut source)
    else:  #118 (line in Coconut source)
        launch_server.run_cmd(["xdg-open", installed_readme], check=False)  #119 (line in Coconut source)



@contextmanager  #122 (line in Coconut source)
def unzipped_mods():  #123 (line in Coconut source)
    with tempfile.TemporaryDirectory() as temp_dir:  #124 (line in Coconut source)
        print("\nUnzipping mods from {_coconut_format_0!r} to temporary directory {_coconut_format_1!r}...".format(_coconut_format_0=(MOD_ZIP_PATH), _coconut_format_1=(temp_dir)))  #125 (line in Coconut source)
        shutil.unpack_archive(MOD_ZIP_PATH, temp_dir)  #126 (line in Coconut source)
        yield temp_dir  #127 (line in Coconut source)



def install_from_dir(source_dir, do_optional=False):  #130 (line in Coconut source)
    launch_server.clean_forge_jars(MINECRAFT_DIR)  #131 (line in Coconut source)

    ensure_forge_client(source_dir)  #133 (line in Coconut source)
    sync_client_mods(source_dir)  #134 (line in Coconut source)
    install_extras(source_dir, do_optional)  #135 (line in Coconut source)

    set_jvm_args()  #137 (line in Coconut source)



def install_from_server():  #140 (line in Coconut source)
    """Install from server and return whether or not to install optional files."""  #141 (line in Coconut source)
    sync_mods.main()  #142 (line in Coconut source)
    launch_server.start_server(dry_run=True)  #143 (line in Coconut source)

    install_from_dir(SERVER_DIR, do_optional=True)  #145 (line in Coconut source)

    if "--no-zip" not in sys.argv:  #147 (line in Coconut source)
        zip_mods()  #148 (line in Coconut source)
    return True  #149 (line in Coconut source)



def install_from_zip():  #152 (line in Coconut source)
    """Install from zip and return whether or not to install optional files."""  #153 (line in Coconut source)
    if "--yes-optional" in sys.argv:  #154 (line in Coconut source)
        do_optional = True  #155 (line in Coconut source)
    elif "--no-optional" in sys.argv:  #156 (line in Coconut source)
        do_optional = False  #157 (line in Coconut source)
    else:  #158 (line in Coconut source)
        do_optional = input("\nInstall optional files {_coconut_format_0}? [y/N] ".format(_coconut_format_0=(OPTIONAL_INSTALL_FILES + OPTIONAL_INSTALL_FOLDERS))).lower() in YES_STRS  #159 (line in Coconut source)
    if do_optional:  #160 (line in Coconut source)
        print("Will install optional files.")  #161 (line in Coconut source)
    else:  #162 (line in Coconut source)
        print("Will NOT install optional files.")  #163 (line in Coconut source)
    with unzipped_mods() as temp_dir:  #164 (line in Coconut source)
        install_from_dir(temp_dir, do_optional)  #165 (line in Coconut source)
    return do_optional  #166 (line in Coconut source)



@_coconut_tco  #169 (line in Coconut source)
def main():  #169 (line in Coconut source)
    if os.path.exists(SERVER_DIR):  #170 (line in Coconut source)
        print("\nInstalling from server...")  #171 (line in Coconut source)
        return _coconut_tail_call(install_from_server)  #172 (line in Coconut source)
    elif os.path.exists(MOD_ZIP_PATH):  #173 (line in Coconut source)
        print("\nInstalling from zipfile...")  #174 (line in Coconut source)
        return _coconut_tail_call(install_from_zip)  #175 (line in Coconut source)
    else:  #176 (line in Coconut source)
        raise IOError("Could not find files for install.")  #177 (line in Coconut source)



if __name__ == "__main__":  #180 (line in Coconut source)
    main()  #181 (line in Coconut source)
