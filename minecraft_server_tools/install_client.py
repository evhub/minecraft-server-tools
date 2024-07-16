#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x62e1e9d8

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
from minecraft_server_tools.constants import ALT_MOD_ZIP_PATH  #12 (line in Coconut source)
from minecraft_server_tools.constants import OPTIONAL_INSTALL_FILES  #12 (line in Coconut source)
from minecraft_server_tools.constants import OPTIONAL_INSTALL_FOLDERS  #12 (line in Coconut source)
from minecraft_server_tools.constants import MODS_NAME  #12 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_MODS_NAME  #12 (line in Coconut source)
from minecraft_server_tools.constants import YES_STRS  #12 (line in Coconut source)
from minecraft_server_tools.constants import NO_STRS  #12 (line in Coconut source)
from minecraft_server_tools.constants import PROFILES_FILE  #12 (line in Coconut source)
from minecraft_server_tools.constants import MODPACK_NAME  #12 (line in Coconut source)
from minecraft_server_tools.constants import START_ARGS  #12 (line in Coconut source)
from minecraft_server_tools.constants import LAUNCHER_FILE  #12 (line in Coconut source)

MINECRAFT_MODS_DIR = os.path.join(MINECRAFT_DIR, MODS_NAME)  #34 (line in Coconut source)


def sync_client_mods(source_dir):  #37 (line in Coconut source)
    print("\nInstalling mods...")  #38 (line in Coconut source)
    all_client_mods = sync_mods.get_location_table_for(os.path.join(source_dir, MODS_NAME))  #39 (line in Coconut source)
    all_client_mods.update(sync_mods.get_location_table_for(os.path.join(source_dir, CLIENT_MODS_NAME)))  #40 (line in Coconut source)

    current_client_mods = sync_mods.get_location_table_for(MINECRAFT_MODS_DIR)  #42 (line in Coconut source)

    sync_mods.set_mods_from_to(all_client_mods, current_client_mods, MINECRAFT_MODS_DIR)  #44 (line in Coconut source)



def install_extras(source_dir, do_optional=True, clean=True):  #47 (line in Coconut source)
    print("\nInstalling other files/folders...")  #48 (line in Coconut source)
    for install_dir in EXTRA_INSTALL_FOLDERS + (OPTIONAL_INSTALL_FOLDERS if do_optional else []):  #49 (line in Coconut source)
        from_dir = os.path.join(source_dir, install_dir)  #50 (line in Coconut source)
        to_dir = os.path.join(MINECRAFT_DIR, install_dir)  #51 (line in Coconut source)
        print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_dir)))  #52 (line in Coconut source)
        cleaned = False  #53 (line in Coconut source)
        if clean and os.path.exists(to_dir):  #54 (line in Coconut source)
            shutil.rmtree(to_dir)  #55 (line in Coconut source)
            cleaned = True  #56 (line in Coconut source)
        if os.path.exists(from_dir):  #57 (line in Coconut source)
            shutil.copytree(from_dir, to_dir, dirs_exist_ok=True)  #58 (line in Coconut source)
        elif cleaned:  #59 (line in Coconut source)
            print("\t\t(cleaned)")  #60 (line in Coconut source)
        else:  #61 (line in Coconut source)
            print("\t\t(skipped)")  #62 (line in Coconut source)

    for install_file in EXTRA_INSTALL_FILES + (OPTIONAL_INSTALL_FILES if do_optional else []):  #64 (line in Coconut source)
        from_path = os.path.join(source_dir, install_file)  #65 (line in Coconut source)
        to_path = os.path.join(MINECRAFT_DIR, install_file)  #66 (line in Coconut source)
        print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_file)))  #67 (line in Coconut source)
        if os.path.exists(from_path):  #68 (line in Coconut source)
            shutil.copy(from_path, to_path)  #69 (line in Coconut source)
        else:  #70 (line in Coconut source)
            print("\t\t(skipped)")  #71 (line in Coconut source)



def ensure_forge_client(source_dir, force=False):  #74 (line in Coconut source)
    if force or not os.path.exists(os.path.join(MINECRAFT_DIR, FORGE_INSTALLER_JAR)):  #75 (line in Coconut source)
        print("\nOpening forge installer; select 'Install client' and press 'Ok'.")  #76 (line in Coconut source)
        launch_server.run_java(["-jar", os.path.join(source_dir, FORGE_INSTALLER_JAR)])  #77 (line in Coconut source)



def get_paths_to_zip():  #80 (line in Coconut source)
    for install_fname in (EXTRA_INSTALL_FILES + OPTIONAL_INSTALL_FILES):  #81 (line in Coconut source)
        fpath = os.path.join(MINECRAFT_DIR, install_fname)  #85 (line in Coconut source)
        if os.path.exists(fpath):  #86 (line in Coconut source)
            yield fpath  #87 (line in Coconut source)
        else:  #88 (line in Coconut source)
            print("\tSkipped {_coconut_format_0!r}...".format(_coconut_format_0=(fpath)))  #89 (line in Coconut source)
    for install_dirname in (EXTRA_INSTALL_FOLDERS + OPTIONAL_INSTALL_FOLDERS + [MODS_NAME,]):  #90 (line in Coconut source)
        install_dirpath = os.path.join(MINECRAFT_DIR, install_dirname)  #95 (line in Coconut source)
        for dirpath, dirnames, filenames in os.walk(install_dirpath):  #96 (line in Coconut source)
            yield dirpath  #97 (line in Coconut source)
            for fname in filenames:  #98 (line in Coconut source)
                yield os.path.join(dirpath, fname)  #99 (line in Coconut source)



def zip_mods():  #102 (line in Coconut source)
    print("\nZipping mod files to {_coconut_format_0}...".format(_coconut_format_0=(MOD_ZIP_PATH)))  #103 (line in Coconut source)
    with zipfile.ZipFile(MOD_ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:  #104 (line in Coconut source)
        for install_path in tqdm(list(get_paths_to_zip())):  #105 (line in Coconut source)
            zf.write(install_path, os.path.relpath(install_path, MINECRAFT_DIR))  #106 (line in Coconut source)
    if ALT_MOD_ZIP_PATH is not None:  #107 (line in Coconut source)
        print("\tCopying {_coconut_format_0!r} to {_coconut_format_1!r}...".format(_coconut_format_0=(MOD_ZIP_PATH), _coconut_format_1=(ALT_MOD_ZIP_PATH)))  #108 (line in Coconut source)
        shutil.copy(MOD_ZIP_PATH, ALT_MOD_ZIP_PATH)  #109 (line in Coconut source)



@_coconut_tco  #112 (line in Coconut source)
def get_javaw_path():  #112 (line in Coconut source)
    for where_cmd in ("which", "where"):  #113 (line in Coconut source)
        try:  #114 (line in Coconut source)
            paths = launch_server.get_cmd_output([where_cmd, "javaw"])  #115 (line in Coconut source)
        except FileNotFoundError:  #116 (line in Coconut source)
            pass  #117 (line in Coconut source)
        else:  #118 (line in Coconut source)
            break  #119 (line in Coconut source)
    else:  #120 (line in Coconut source)
        return None  #121 (line in Coconut source)
    return _coconut_tail_call((_coconut_iter_getitem(((paths).splitlines()), (0))).strip)  #122 (line in Coconut source)



def set_jvm_args():  #130 (line in Coconut source)
    print("\nSetting JVM arguments...")  #131 (line in Coconut source)
    with launch_server.using_graal_java():  #132 (line in Coconut source)
        java_args = " ".join(launch_server.get_java_args(client=True))  #133 (line in Coconut source)
        java_path = get_javaw_path()  #134 (line in Coconut source)
        with open(PROFILES_FILE, "r+") as profiles_file:  #135 (line in Coconut source)
            top_level_json = json.load(profiles_file)  #136 (line in Coconut source)
            profiles = top_level_json["profiles"]  #137 (line in Coconut source)
            if "forge" not in profiles:  #138 (line in Coconut source)
                return False  #139 (line in Coconut source)
            forge_profile = profiles["forge"]  #140 (line in Coconut source)
            forge_profile["name"] = MODPACK_NAME  #141 (line in Coconut source)
            forge_profile["javaArgs"] = java_args  #142 (line in Coconut source)
            if java_path:  #143 (line in Coconut source)
                print("\t(using java at: {_coconut_format_0!r})".format(_coconut_format_0=(java_path)))  #144 (line in Coconut source)
                forge_profile["javaDir"] = java_path  #145 (line in Coconut source)
            else:  #146 (line in Coconut source)
                print("\t(failed to locate java)")  #147 (line in Coconut source)

            profiles_file.seek(0)  #149 (line in Coconut source)
            profiles_file.truncate()  #150 (line in Coconut source)
            json.dump(top_level_json, profiles_file, indent=2)  #151 (line in Coconut source)
    print("\tSet JVM args to: {_coconut_format_0}".format(_coconut_format_0=(java_args)))  #152 (line in Coconut source)
    return True  #153 (line in Coconut source)



def open_readme():  #156 (line in Coconut source)
    installed_readme = os.path.join(MINECRAFT_DIR, README_FILE)  #157 (line in Coconut source)
    print("\nOpening {_coconut_format_0}...".format(_coconut_format_0=(installed_readme)))  #158 (line in Coconut source)
    if WINDOWS:  #159 (line in Coconut source)
        launch_server.run_cmd(["explorer", installed_readme], check=False)  #160 (line in Coconut source)
    else:  #161 (line in Coconut source)
        launch_server.run_cmd(["xdg-open", installed_readme], check=False)  #162 (line in Coconut source)



@contextmanager  #165 (line in Coconut source)
def unzipped_mods():  #166 (line in Coconut source)
    with tempfile.TemporaryDirectory() as temp_dir:  #167 (line in Coconut source)
        print("\nUnzipping mods from {_coconut_format_0!r} to temporary directory {_coconut_format_1!r}...".format(_coconut_format_0=(MOD_ZIP_PATH), _coconut_format_1=(temp_dir)))  #168 (line in Coconut source)
        shutil.unpack_archive(MOD_ZIP_PATH, temp_dir)  #169 (line in Coconut source)
        yield temp_dir  #170 (line in Coconut source)



def install_from_dir(source_dir, do_optional=False):  #173 (line in Coconut source)
    launch_server.clean_forge_jars(MINECRAFT_DIR)  #174 (line in Coconut source)

    ensure_forge_client(source_dir)  #176 (line in Coconut source)
    success = set_jvm_args()  #177 (line in Coconut source)
    if not success:  #178 (line in Coconut source)
        ensure_forge_client(source_dir, force=True)  #179 (line in Coconut source)
        if not set_jvm_args():  #180 (line in Coconut source)
            raise OSError("Failed to automatically install forge; you'll need to run {_coconut_format_0} manually.".format(_coconut_format_0=(FORGE_INSTALLER_JAR)))  #181 (line in Coconut source)

    sync_client_mods(source_dir)  #183 (line in Coconut source)
    if "--only-mods" not in sys.argv:  #184 (line in Coconut source)
        install_extras(source_dir, do_optional)  #185 (line in Coconut source)



def install_from_server():  #188 (line in Coconut source)
    """Install from server and return whether or not to install optional files."""  #189 (line in Coconut source)
    sync_mods.main()  #190 (line in Coconut source)
    launch_server.start_server(dry_run=True)  #191 (line in Coconut source)

    install_from_dir(SERVER_DIR, do_optional=True)  #193 (line in Coconut source)

    if "--only-mods" not in sys.argv and "--no-zip" not in sys.argv:  #195 (line in Coconut source)
        zip_mods()  #196 (line in Coconut source)
    return True  #197 (line in Coconut source)



def ask_question(text, default):  #200 (line in Coconut source)
    got = input(text).lower()  #201 (line in Coconut source)
    if got in YES_STRS:  #202 (line in Coconut source)
        return True  #203 (line in Coconut source)
    elif got in NO_STRS:  #204 (line in Coconut source)
        return False  #205 (line in Coconut source)
    else:  #206 (line in Coconut source)
        return default  #207 (line in Coconut source)



def install_from_zip():  #210 (line in Coconut source)
    """Install from zip and return whether or not to install optional files."""  #211 (line in Coconut source)
    if "--yes-optional" in sys.argv:  #212 (line in Coconut source)
        do_optional = True  #213 (line in Coconut source)
    elif "--no-optional" in sys.argv:  #214 (line in Coconut source)
        do_optional = False  #215 (line in Coconut source)
    else:  #216 (line in Coconut source)
        do_optional = ask_question("\nInstall optional files {_coconut_format_0}? [Y/n] ".format(_coconut_format_0=(OPTIONAL_INSTALL_FILES + OPTIONAL_INSTALL_FOLDERS)), True)  #217 (line in Coconut source)
    if do_optional:  #218 (line in Coconut source)
        print("Will install optional files.")  #219 (line in Coconut source)
    else:  #220 (line in Coconut source)
        print("Will NOT install optional files.")  #221 (line in Coconut source)
    with unzipped_mods() as temp_dir:  #222 (line in Coconut source)
        install_from_dir(temp_dir, do_optional)  #223 (line in Coconut source)
    return do_optional  #224 (line in Coconut source)



def launch_minecraft():  #227 (line in Coconut source)
    print("\nLaunching Minecraft at {_coconut_format_0!r}...".format(_coconut_format_0=(LAUNCHER_FILE)))  #228 (line in Coconut source)
    if not os.path.exists(LAUNCHER_FILE):  #229 (line in Coconut source)
        raise OSError("Could not find Minecraft Launcher file!\n\nMod files have still been installed, but you'll need to launch Minecraft manually.")  #230 (line in Coconut source)
    if WINDOWS:  #231 (line in Coconut source)
        launch_server.run_cmd(["START", MODPACK_NAME] + START_ARGS + [LAUNCHER_FILE,], shell=True)  #232 (line in Coconut source)
    else:  #233 (line in Coconut source)
        launch_server.run_cmd(["open", LAUNCHER_FILE])  #234 (line in Coconut source)



def main():  #237 (line in Coconut source)
    if os.path.exists(SERVER_DIR):  #238 (line in Coconut source)
        print("\nInstalling from server...")  #239 (line in Coconut source)
        do_optional = install_from_server()  #240 (line in Coconut source)
    elif os.path.exists(MOD_ZIP_PATH):  #241 (line in Coconut source)
        if "downloads" in MOD_ZIP_PATH.lower():  #242 (line in Coconut source)
            print("WARNING: Using downloaded Minecraft Mods.zip instead of synchronized version; you will not get updates automatically.")  #243 (line in Coconut source)
        print("\nInstalling from zipfile...")  #244 (line in Coconut source)
        do_optional = install_from_zip()  #245 (line in Coconut source)
    else:  #246 (line in Coconut source)
        raise IOError("Could not find files for install (make sure you have the 'Minecraft Mods' folder in your OneDrive).")  #247 (line in Coconut source)
    if "--launch" in sys.argv:  #248 (line in Coconut source)
        launch_minecraft()  #249 (line in Coconut source)
    return do_optional  #250 (line in Coconut source)



if __name__ == "__main__":  #253 (line in Coconut source)
    main()  #254 (line in Coconut source)
