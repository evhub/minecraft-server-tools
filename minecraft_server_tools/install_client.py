#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb9896cb0

# Compiled with Coconut version 3.2.0-post_dev16

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev16', '', True)
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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning, _coconut_lazy_module, _coconut_type
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
import shutil  #2 (line in Coconut source)
import zipfile  #3 (line in Coconut source)
import tempfile  #4 (line in Coconut source)
import json  #5 (line in Coconut source)
import argparse  #6 (line in Coconut source)
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
from minecraft_server_tools.constants import BARREL_ROLL_MOD_PREFIX  #12 (line in Coconut source)
from minecraft_server_tools.constants import FORGE_PROFILE_NAME  #12 (line in Coconut source)
from minecraft_server_tools.constants import USE_GRAAL  #12 (line in Coconut source)
from minecraft_server_tools.constants import fixpath  #12 (line in Coconut source)

MINECRAFT_MODS_DIR = os.path.join(MINECRAFT_DIR, MODS_NAME)  #38 (line in Coconut source)


def sync_client_mods(source_dir, do_barrel_roll=True):  #41 (line in Coconut source)
    print("\nInstalling mods...")  #42 (line in Coconut source)
    all_client_mods = sync_mods.get_location_table_for(os.path.join(source_dir, MODS_NAME))  #43 (line in Coconut source)
    all_client_mods.update(sync_mods.get_location_table_for(os.path.join(source_dir, CLIENT_MODS_NAME)))  #44 (line in Coconut source)

    if do_barrel_roll is False:  #46 (line in Coconut source)
        barrel_roll_mods = (tuple)((filter)(_coconut.operator.methodcaller("startswith", BARREL_ROLL_MOD_PREFIX), all_client_mods))  #47 (line in Coconut source)
        for barrel_roll_mod_name in barrel_roll_mods:  #48 (line in Coconut source)
            print("\tSkipping {_coconut_format_0!r} (not doing a barrel roll)...".format(_coconut_format_0=(barrel_roll_mod_name)))  #49 (line in Coconut source)
            del all_client_mods[barrel_roll_mod_name]  #50 (line in Coconut source)

    current_client_mods = sync_mods.get_location_table_for(MINECRAFT_MODS_DIR)  #52 (line in Coconut source)

    sync_mods.set_mods_from_to(all_client_mods, current_client_mods, MINECRAFT_MODS_DIR)  #54 (line in Coconut source)



def install_extras(source_dir, do_optional=True, clean=True):  #57 (line in Coconut source)
    print("\nInstalling other files/folders...")  #58 (line in Coconut source)

    if not do_optional:  #60 (line in Coconut source)
        optional_rel_paths = _coconut.set((p.replace("\\", "/") for p in OPTIONAL_INSTALL_FOLDERS + OPTIONAL_INSTALL_FILES))  #61 (line in Coconut source)
        def ignore_optional(directory, contents):  #62 (line in Coconut source)
            ignored = set()  #63 (line in Coconut source)
            for name in contents:  #64 (line in Coconut source)
                rel_path = os.path.relpath(os.path.join(directory, name), source_dir).replace("\\", "/")  #65 (line in Coconut source)
                if rel_path in optional_rel_paths:  #66 (line in Coconut source)
                    print("\t\tskipping optional {_coconut_format_0}".format(_coconut_format_0=(rel_path)))  #67 (line in Coconut source)
                    ignored.add(name)  #68 (line in Coconut source)
            return ignored  #69 (line in Coconut source)

    else:  #70 (line in Coconut source)
        optional_rel_paths = set()  #71 (line in Coconut source)
        ignore_optional = None  #72 (line in Coconut source)

    for install_dir in EXTRA_INSTALL_FOLDERS:  #74 (line in Coconut source)
        from_dir = os.path.join(source_dir, install_dir)  #75 (line in Coconut source)
        to_dir = os.path.join(MINECRAFT_DIR, install_dir)  #76 (line in Coconut source)
        print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_dir)))  #77 (line in Coconut source)
        cleaned = False  #78 (line in Coconut source)
        if clean and os.path.exists(to_dir):  #79 (line in Coconut source)
            launch_server.remove_dir_if_exists(to_dir)  #80 (line in Coconut source)
            cleaned = True  #81 (line in Coconut source)
        if os.path.exists(from_dir):  #82 (line in Coconut source)
            shutil.copytree(from_dir, to_dir, dirs_exist_ok=True, ignore=ignore_optional)  #83 (line in Coconut source)
        elif cleaned:  #84 (line in Coconut source)
            print("\t\t(cleaned)")  #85 (line in Coconut source)
        else:  #86 (line in Coconut source)
            print("\t\t(skipped)")  #87 (line in Coconut source)

    for install_dir in OPTIONAL_INSTALL_FOLDERS:  #89 (line in Coconut source)
        from_dir = os.path.join(source_dir, install_dir)  #90 (line in Coconut source)
        to_dir = os.path.join(MINECRAFT_DIR, install_dir)  #91 (line in Coconut source)
        if do_optional:  #92 (line in Coconut source)
            print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_dir)))  #93 (line in Coconut source)
            cleaned = False  #94 (line in Coconut source)
            if clean and os.path.exists(to_dir):  #95 (line in Coconut source)
                launch_server.remove_dir_if_exists(to_dir)  #96 (line in Coconut source)
                cleaned = True  #97 (line in Coconut source)
            if os.path.exists(from_dir):  #98 (line in Coconut source)
                shutil.copytree(from_dir, to_dir, dirs_exist_ok=True)  #99 (line in Coconut source)
            elif cleaned:  #100 (line in Coconut source)
                print("\t\t(cleaned)")  #101 (line in Coconut source)
            else:  #102 (line in Coconut source)
                print("\t\t(skipped)")  #103 (line in Coconut source)
        elif not os.path.exists(to_dir):  #104 (line in Coconut source)
            print("\t{_coconut_format_0} (missing, installing)...".format(_coconut_format_0=(install_dir)))  #105 (line in Coconut source)
            if os.path.exists(from_dir):  #106 (line in Coconut source)
                shutil.copytree(from_dir, to_dir, dirs_exist_ok=True)  #107 (line in Coconut source)
            else:  #108 (line in Coconut source)
                print("\t\t(skipped)")  #109 (line in Coconut source)

    for install_file in EXTRA_INSTALL_FILES:  #111 (line in Coconut source)
        from_path = os.path.join(source_dir, install_file)  #112 (line in Coconut source)
        to_path = os.path.join(MINECRAFT_DIR, install_file)  #113 (line in Coconut source)
        if install_file.replace("\\", "/") in optional_rel_paths:  #114 (line in Coconut source)
            print("\t{_coconut_format_0} skipped as optional".format(_coconut_format_0=(install_file)))  #115 (line in Coconut source)
            continue  #116 (line in Coconut source)
        print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_file)))  #117 (line in Coconut source)
        if os.path.exists(from_path):  #118 (line in Coconut source)
            shutil.copy(from_path, to_path)  #119 (line in Coconut source)
        else:  #120 (line in Coconut source)
            print("\t\t(skipped)")  #121 (line in Coconut source)

    for install_file in OPTIONAL_INSTALL_FILES:  #123 (line in Coconut source)
        from_path = os.path.join(source_dir, install_file)  #124 (line in Coconut source)
        to_path = os.path.join(MINECRAFT_DIR, install_file)  #125 (line in Coconut source)
        if do_optional or not os.path.exists(to_path):  #126 (line in Coconut source)
            if not do_optional:  #127 (line in Coconut source)
                print("\t{_coconut_format_0} (missing, installing)...".format(_coconut_format_0=(install_file)))  #128 (line in Coconut source)
            else:  #129 (line in Coconut source)
                print("\t{_coconut_format_0}...".format(_coconut_format_0=(install_file)))  #130 (line in Coconut source)
            if os.path.exists(from_path):  #131 (line in Coconut source)
                shutil.copy(from_path, to_path)  #132 (line in Coconut source)
            else:  #133 (line in Coconut source)
                print("\t\t(skipped)")  #134 (line in Coconut source)



def ensure_forge_client(source_dir, force=False):  #137 (line in Coconut source)
    if force or not os.path.exists(os.path.join(MINECRAFT_DIR, FORGE_INSTALLER_JAR)):  #138 (line in Coconut source)
        launch_server.ensure_graal()  #139 (line in Coconut source)
        print("\nOpening forge installer; select 'Install client' and press 'Proceed'.")  #140 (line in Coconut source)
        launch_server.run_java(["-jar", os.path.join(source_dir, FORGE_INSTALLER_JAR)])  #141 (line in Coconut source)



def get_paths_to_zip():  #144 (line in Coconut source)
    seen = set()  # type: set  #145 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #145 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #145 (line in Coconut source)
    __annotations__["seen"] = 'set'  #145 (line in Coconut source)
    for install_fname in (EXTRA_INSTALL_FILES + OPTIONAL_INSTALL_FILES):  #146 (line in Coconut source)
        fpath = os.path.join(MINECRAFT_DIR, install_fname)  #150 (line in Coconut source)
        if os.path.exists(fpath):  #151 (line in Coconut source)
            seen.add(os.path.normpath(fpath))  #152 (line in Coconut source)
            yield fpath  #153 (line in Coconut source)
        else:  #154 (line in Coconut source)
            print("\tSkipped {_coconut_format_0!r}...".format(_coconut_format_0=(fpath)))  #155 (line in Coconut source)
    for install_dirname in (EXTRA_INSTALL_FOLDERS + OPTIONAL_INSTALL_FOLDERS + [MODS_NAME,]):  #156 (line in Coconut source)
        install_dirpath = os.path.join(MINECRAFT_DIR, install_dirname)  #161 (line in Coconut source)
        for dirpath, dirnames, filenames in os.walk(install_dirpath):  #162 (line in Coconut source)
            norm_dirpath = os.path.normpath(dirpath)  #163 (line in Coconut source)
            if norm_dirpath not in seen:  #164 (line in Coconut source)
                seen.add(norm_dirpath)  #165 (line in Coconut source)
                yield dirpath  #166 (line in Coconut source)
            for fname in filenames:  #167 (line in Coconut source)
                fpath = os.path.join(dirpath, fname)  #168 (line in Coconut source)
                norm_fpath = os.path.normpath(fpath)  #169 (line in Coconut source)
                if norm_fpath not in seen:  #170 (line in Coconut source)
                    seen.add(norm_fpath)  #171 (line in Coconut source)
                    yield fpath  #172 (line in Coconut source)



def zip_mods():  #175 (line in Coconut source)
    print("\nZipping mod files to {_coconut_format_0}...".format(_coconut_format_0=(MOD_ZIP_PATH)))  #176 (line in Coconut source)
    with zipfile.ZipFile(MOD_ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:  #177 (line in Coconut source)
        for install_path in tqdm(list(get_paths_to_zip())):  #178 (line in Coconut source)
            zf.write(install_path, os.path.relpath(install_path, MINECRAFT_DIR))  #179 (line in Coconut source)
    if ALT_MOD_ZIP_PATH is not None:  #180 (line in Coconut source)
        print("\tCopying {_coconut_format_0!r} to {_coconut_format_1!r}...".format(_coconut_format_0=(MOD_ZIP_PATH), _coconut_format_1=(ALT_MOD_ZIP_PATH)))  #181 (line in Coconut source)
        shutil.copy(MOD_ZIP_PATH, ALT_MOD_ZIP_PATH)  #182 (line in Coconut source)



@_coconut_tco  #185 (line in Coconut source)
def get_javaw_path():  #185 (line in Coconut source)
    if USE_GRAAL:  #186 (line in Coconut source)
        graal_bin_dir = launch_server.get_graal_bin_dir()  #187 (line in Coconut source)
        javaw_path = os.path.join(graal_bin_dir, "javaw.exe" if WINDOWS else "javaw")  #188 (line in Coconut source)
        if os.path.exists(javaw_path):  #189 (line in Coconut source)
            return javaw_path  #190 (line in Coconut source)
    for where_cmd in ("which", "where"):  #191 (line in Coconut source)
        try:  #192 (line in Coconut source)
            paths = launch_server.get_cmd_output([where_cmd, "javaw"])  #193 (line in Coconut source)
        except FileNotFoundError:  #194 (line in Coconut source)
            pass  #195 (line in Coconut source)
        else:  #196 (line in Coconut source)
            break  #197 (line in Coconut source)
    else:  #198 (line in Coconut source)
        return None  #199 (line in Coconut source)
    path = ((_coconut_iter_getitem(((paths).splitlines()), (0))).strip())  #200 (line in Coconut source)
    if WINDOWS and not path.endswith(".exe"):  #206 (line in Coconut source)
        path += ".exe"  #207 (line in Coconut source)
        if path.startswith("/c/"):  #208 (line in Coconut source)
            path = "C:" + path[2:]  #209 (line in Coconut source)
        elif path.startswith("c/"):  #210 (line in Coconut source)
            path = "C:" + path[1:]  #211 (line in Coconut source)
    return _coconut_tail_call(fixpath, path)  #212 (line in Coconut source)



def set_jvm_args():  #215 (line in Coconut source)
    print("\nSetting JVM arguments...")  #216 (line in Coconut source)
    with launch_server.using_graal_java():  #217 (line in Coconut source)
        java_args = " ".join(launch_server.get_java_args(client=True))  #218 (line in Coconut source)
        java_path = get_javaw_path()  #219 (line in Coconut source)
        with open(PROFILES_FILE, "r+") as profiles_file:  #220 (line in Coconut source)
            top_level_json = json.load(profiles_file)  #221 (line in Coconut source)
            profiles = top_level_json["profiles"]  #222 (line in Coconut source)
            if FORGE_PROFILE_NAME not in profiles:  #223 (line in Coconut source)
                return False  #224 (line in Coconut source)
            forge_profile = profiles[FORGE_PROFILE_NAME]  #225 (line in Coconut source)
            forge_profile["name"] = MODPACK_NAME  #226 (line in Coconut source)
            forge_profile["javaArgs"] = java_args  #227 (line in Coconut source)
            if java_path:  #228 (line in Coconut source)
                print("\t(using java at: {_coconut_format_0!r})".format(_coconut_format_0=(java_path)))  #229 (line in Coconut source)
                forge_profile["javaDir"] = java_path  #230 (line in Coconut source)
            else:  #231 (line in Coconut source)
                print("\t(failed to locate java)")  #232 (line in Coconut source)

            profiles_file.seek(0)  #234 (line in Coconut source)
            profiles_file.truncate()  #235 (line in Coconut source)
            json.dump(top_level_json, profiles_file, indent=2)  #236 (line in Coconut source)
    return True  #237 (line in Coconut source)



def open_readme():  #240 (line in Coconut source)
    installed_readme = os.path.join(MINECRAFT_DIR, README_FILE)  #241 (line in Coconut source)
    print("\nOpening {_coconut_format_0}...".format(_coconut_format_0=(installed_readme)))  #242 (line in Coconut source)
    if WINDOWS:  #243 (line in Coconut source)
        launch_server.run_cmd(["explorer", installed_readme], check=False)  #244 (line in Coconut source)
    else:  #245 (line in Coconut source)
        launch_server.run_cmd(["xdg-open", installed_readme], check=False)  #246 (line in Coconut source)



@contextmanager  #249 (line in Coconut source)
def unzipped_mods():  #250 (line in Coconut source)
    with tempfile.TemporaryDirectory() as temp_dir:  #251 (line in Coconut source)
        print("\nUnzipping mods from {_coconut_format_0!r} to temporary directory {_coconut_format_1!r}...".format(_coconut_format_0=(MOD_ZIP_PATH), _coconut_format_1=(temp_dir)))  #252 (line in Coconut source)
        shutil.unpack_archive(MOD_ZIP_PATH, temp_dir)  #253 (line in Coconut source)
        yield temp_dir  #254 (line in Coconut source)



def install_from_dir(source_dir, do_optional=False, do_barrel_roll=True, no_mods=False, no_files=False):  #257 (line in Coconut source)
    launch_server.clean_forge_jars(MINECRAFT_DIR)  #258 (line in Coconut source)

    ensure_forge_client(source_dir)  #260 (line in Coconut source)
    success = set_jvm_args()  #261 (line in Coconut source)
    if not success:  #262 (line in Coconut source)
        ensure_forge_client(source_dir, force=True)  #263 (line in Coconut source)
        if not set_jvm_args():  #264 (line in Coconut source)
            raise OSError("Failed to automatically install forge; you'll need to run {_coconut_format_0} manually.".format(_coconut_format_0=(FORGE_INSTALLER_JAR)))  #265 (line in Coconut source)

    if not no_mods:  #267 (line in Coconut source)
        sync_client_mods(source_dir, do_barrel_roll)  #268 (line in Coconut source)
    if not no_files:  #269 (line in Coconut source)
        install_extras(source_dir, do_optional)  #270 (line in Coconut source)



def install_from_server(no_mods=False, no_files=False, no_zip=False):  #273 (line in Coconut source)
    """Install from server and return whether or not to install optional files."""  #274 (line in Coconut source)
    sync_mods.main()  #275 (line in Coconut source)
    launch_server.start_server(dry_run=True)  #276 (line in Coconut source)

    install_from_dir(SERVER_DIR, do_optional=True, no_mods=no_mods, no_files=no_files)  #278 (line in Coconut source)

    if not (no_zip or no_mods or no_files):  #280 (line in Coconut source)
        zip_mods()  #281 (line in Coconut source)
    return True, True  #282 (line in Coconut source)



def ask_question(text, default):  #285 (line in Coconut source)
    got = input(text).lower()  #286 (line in Coconut source)
    if got in YES_STRS:  #287 (line in Coconut source)
        return True  #288 (line in Coconut source)
    elif got in NO_STRS:  #289 (line in Coconut source)
        return False  #290 (line in Coconut source)
    else:  #291 (line in Coconut source)
        return default  #292 (line in Coconut source)



def install_from_zip(optional=None, barrel_roll=None, no_mods=False, no_files=False):  #295 (line in Coconut source)
    """Install from zip and return whether or not to install optional files."""  #296 (line in Coconut source)
    if optional is True:  #297 (line in Coconut source)
        do_optional = True  #298 (line in Coconut source)
    elif optional is False:  #299 (line in Coconut source)
        do_optional = False  #300 (line in Coconut source)
    else:  #301 (line in Coconut source)
        do_optional = ask_question("\nOverwrite optional files {_coconut_format_0}? [Y/n] ".format(_coconut_format_0=(OPTIONAL_INSTALL_FILES + OPTIONAL_INSTALL_FOLDERS)), True)  #302 (line in Coconut source)
    if do_optional:  #303 (line in Coconut source)
        print("Will overwrite optional files.")  #304 (line in Coconut source)
    else:  #305 (line in Coconut source)
        print("Will NOT overwrite optional files.")  #306 (line in Coconut source)

    if BARREL_ROLL_MOD_PREFIX is None:  #308 (line in Coconut source)
        do_barrel_roll = None  #309 (line in Coconut source)
    elif barrel_roll is True:  #310 (line in Coconut source)
        do_barrel_roll = True  #311 (line in Coconut source)
    elif barrel_roll is False:  #312 (line in Coconut source)
        do_barrel_roll = False  #313 (line in Coconut source)
    else:  #314 (line in Coconut source)
        do_barrel_roll = ask_question("\nDo a barrel roll? [Y/n] ", True)  #315 (line in Coconut source)
    if do_barrel_roll:  #316 (line in Coconut source)
        print("Will do a barrel roll.")  #317 (line in Coconut source)
    else:  #318 (line in Coconut source)
        print("Will NOT do a barrel roll.")  #319 (line in Coconut source)

    with unzipped_mods() as temp_dir:  #321 (line in Coconut source)
        install_from_dir(temp_dir, do_optional=do_optional, do_barrel_roll=do_barrel_roll, no_mods=no_mods, no_files=no_files)  #322 (line in Coconut source)
    return do_optional, do_barrel_roll  #323 (line in Coconut source)



def launch_minecraft():  #326 (line in Coconut source)
    print("\nLaunching Minecraft at {_coconut_format_0!r}...".format(_coconut_format_0=(LAUNCHER_FILE)))  #327 (line in Coconut source)
    if not os.path.exists(LAUNCHER_FILE):  #328 (line in Coconut source)
        raise OSError("Could not find Minecraft Launcher file!\n\nMod files have still been installed, but you'll need to launch Minecraft manually.")  #329 (line in Coconut source)
    if WINDOWS:  #330 (line in Coconut source)
        launch_server.run_cmd(["START", MODPACK_NAME] + START_ARGS + [LAUNCHER_FILE,], shell=True)  #331 (line in Coconut source)
    else:  #332 (line in Coconut source)
        launch_server.run_cmd(["open", LAUNCHER_FILE])  #333 (line in Coconut source)



@_coconut_tco  #336 (line in Coconut source)
def parse_args():  #336 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Install Minecraft client with mods and configuration files.")  #337 (line in Coconut source)
    parser.add_argument("--launch", action="store_true", help="Launch Minecraft after installation")  #340 (line in Coconut source)
    parser.add_argument("--no-mods", action="store_true", help="Skip installing mods")  #345 (line in Coconut source)
    parser.add_argument("--no-files", action="store_true", help="Skip installing extra files and folders")  #350 (line in Coconut source)
    parser.add_argument("--no-zip", action="store_true", help="Skip zipping mods after server install")  #355 (line in Coconut source)

    optional_group = parser.add_mutually_exclusive_group()  #361 (line in Coconut source)
    optional_group.add_argument("--yes-optional", action="store_true", help="Overwrite optional files without prompting")  #362 (line in Coconut source)
    optional_group.add_argument("--no-optional", action="store_true", help="Skip optional files without prompting")  #367 (line in Coconut source)

    barrel_roll_group = parser.add_mutually_exclusive_group()  #373 (line in Coconut source)
    barrel_roll_group.add_argument("--yes-barrel-roll", action="store_true", help="Install barrel roll mod without prompting")  #374 (line in Coconut source)
    barrel_roll_group.add_argument("--no-barrel-roll", action="store_true", help="Skip barrel roll mod without prompting")  #379 (line in Coconut source)

    return _coconut_tail_call(parser.parse_args)  #385 (line in Coconut source)



def main():  #388 (line in Coconut source)
    args = parse_args()  #389 (line in Coconut source)

# Convert mutually exclusive groups to tri-state values
    optional = True if args.yes_optional else (False if args.no_optional else None)  #392 (line in Coconut source)
    barrel_roll = True if args.yes_barrel_roll else (False if args.no_barrel_roll else None)  #393 (line in Coconut source)

    if os.path.exists(SERVER_DIR):  #395 (line in Coconut source)
        print("\nInstalling from server...")  #396 (line in Coconut source)
        do_optional, do_barrel_roll = install_from_server(no_mods=args.no_mods, no_files=args.no_files, no_zip=args.no_zip)  #397 (line in Coconut source)
    elif os.path.exists(MOD_ZIP_PATH):  #402 (line in Coconut source)
        if "downloads" in MOD_ZIP_PATH.lower():  #403 (line in Coconut source)
            print("WARNING: Using downloaded Minecraft Mods.zip instead of synchronized version; you will not get updates automatically.")  #404 (line in Coconut source)
        print("\nInstalling from zipfile...")  #405 (line in Coconut source)
        do_optional, do_barrel_roll = install_from_zip(optional=optional, barrel_roll=barrel_roll, no_mods=args.no_mods, no_files=args.no_files)  #406 (line in Coconut source)
    else:  #412 (line in Coconut source)
        raise IOError("Could not find files for install (make sure you have the 'Minecraft Mods' folder in your OneDrive/Dropbox).")  #413 (line in Coconut source)

    if args.launch:  #415 (line in Coconut source)
        launch_minecraft()  #416 (line in Coconut source)
    return do_optional, do_barrel_roll  #417 (line in Coconut source)



if __name__ == "__main__":  #420 (line in Coconut source)
    main()  #421 (line in Coconut source)
