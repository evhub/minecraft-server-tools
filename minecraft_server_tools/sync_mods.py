#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x954cde5e

# Compiled with Coconut version 3.1.0-post_dev15

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.0-post_dev15', '', True)
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
import shutil  #2 (line in Coconut source)

from minecraft_server_tools.constants import SERVER_DIR  #4 (line in Coconut source)
from minecraft_server_tools.constants import MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import BASE_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import EXTRA_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import REMOVED_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import CLIENT_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import BASE_CLIENT_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import EXTRA_CLIENT_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import REMOVED_CLIENT_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import BINARY_SEARCH_FILE  #4 (line in Coconut source)
from minecraft_server_tools.constants import load_json  #4 (line in Coconut source)

MODS_DIR = os.path.join(SERVER_DIR, MODS_NAME)  #18 (line in Coconut source)
BASE_MODS_DIR = os.path.join(SERVER_DIR, BASE_MODS_NAME)  #19 (line in Coconut source)
EXTRA_MODS_DIR = os.path.join(SERVER_DIR, EXTRA_MODS_NAME)  #20 (line in Coconut source)
REMOVED_MODS_DIR = os.path.join(SERVER_DIR, REMOVED_MODS_NAME)  #21 (line in Coconut source)
CLIENT_MODS_DIR = os.path.join(SERVER_DIR, CLIENT_MODS_NAME)  #22 (line in Coconut source)
BASE_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, BASE_CLIENT_MODS_NAME)  #23 (line in Coconut source)
EXTRA_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, EXTRA_CLIENT_MODS_NAME)  #24 (line in Coconut source)
REMOVED_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, REMOVED_CLIENT_MODS_NAME)  #25 (line in Coconut source)


def ensure_dirs():  #28 (line in Coconut source)
    for dirpath in [MODS_DIR, EXTRA_MODS_DIR, CLIENT_MODS_DIR, EXTRA_CLIENT_MODS_DIR]:  #29 (line in Coconut source)
        if not os.path.exists(dirpath):  #35 (line in Coconut source)
            os.mkdir(dirpath)  #36 (line in Coconut source)



def get_location_table_for(mods_dir):  #39 (line in Coconut source)
    mod_location_table = _coconut.dict()  #40 (line in Coconut source)
    if os.path.exists(mods_dir):  #41 (line in Coconut source)
        for name in os.listdir(mods_dir):  #42 (line in Coconut source)
            path = os.path.join(mods_dir, name)  #43 (line in Coconut source)
            if os.path.isfile(path):  #44 (line in Coconut source)
                assert name not in mod_location_table, "found duplicate mod file at both {_coconut_format_0!r} and {_coconut_format_1!r}".format(_coconut_format_0=(mod_location_table[name]), _coconut_format_1=(path))  #45 (line in Coconut source)
                mod_location_table[name] = path  #46 (line in Coconut source)
    return mod_location_table  #47 (line in Coconut source)



@_coconut_tco  #50 (line in Coconut source)
def display_mod_path(mod_path):  #50 (line in Coconut source)
    mod_dir, mod_name = os.path.split(mod_path)  #51 (line in Coconut source)
    _, mod_dir_name = os.path.split(mod_dir)  #52 (line in Coconut source)
    return _coconut_tail_call(os.path.join, mod_dir_name, mod_name)  #53 (line in Coconut source)



def rm_mod(path):  #56 (line in Coconut source)
    print("Removing {mod}...".format(mod=display_mod_path(path)))  #57 (line in Coconut source)
    os.remove(path)  #58 (line in Coconut source)



def remove_mods_in_from(remove_mod_location_table, current_mod_location_table):  #61 (line in Coconut source)
    for mod, cur_path in current_mod_location_table.items():  #62 (line in Coconut source)
        if mod in remove_mod_location_table and os.path.exists(cur_path):  #63 (line in Coconut source)
            rm_mod(cur_path)  #64 (line in Coconut source)



def add_mod(from_path, to_path):  #67 (line in Coconut source)
    print("Adding {mod} from {src}...".format(mod=display_mod_path(to_path), src=display_mod_path(from_path)))  #68 (line in Coconut source)
    os.makedirs(os.path.dirname(to_path), exist_ok=True)  #69 (line in Coconut source)
    shutil.copy(from_path, to_path)  #70 (line in Coconut source)



def set_mods_from_to(target_mod_location_table, current_mod_location_table, set_mods_dir):  #73 (line in Coconut source)
    for mod, cur_path in current_mod_location_table.items():  #74 (line in Coconut source)
        if mod not in target_mod_location_table and os.path.exists(cur_path):  #75 (line in Coconut source)
            print("Removing {mod}...".format(mod=display_mod_path(cur_path)))  #76 (line in Coconut source)
            os.remove(cur_path)  #77 (line in Coconut source)
    add_mods_from_to(target_mod_location_table, current_mod_location_table, set_mods_dir)  #78 (line in Coconut source)



def add_mods_from_to(target_mod_location_table, current_mod_location_table, set_mods_dir):  #81 (line in Coconut source)
    for mod, tar_path in target_mod_location_table.items():  #82 (line in Coconut source)
        if mod not in current_mod_location_table:  #83 (line in Coconut source)
            new_path = os.path.join(set_mods_dir, mod)  #84 (line in Coconut source)
            add_mod(tar_path, new_path)  #85 (line in Coconut source)



@_coconut_tco  #88 (line in Coconut source)
def get_binary_search_folder(binary_search, folder_name):  #88 (line in Coconut source)
    return _coconut_tail_call(os.path.join, SERVER_DIR, binary_search[folder_name])  #89 (line in Coconut source)



def load_binary_search_file():  #92 (line in Coconut source)
    binary_search = load_json(BINARY_SEARCH_FILE, _coconut.dict((("searching", False),)))  #93 (line in Coconut source)
    if binary_search.get("num_a") == "all":  #96 (line in Coconut source)
        binary_search["num_a"] = len(get_location_table_for(get_binary_search_folder(binary_search, "folder_a")))  #97 (line in Coconut source)
    return binary_search  #98 (line in Coconut source)



@_coconut_tco  #101 (line in Coconut source)
def get_sorted_location_table_items_for(folder):  #101 (line in Coconut source)
    return _coconut_tail_call(list, sorted(get_location_table_for(folder).items()))  #102 (line in Coconut source)



def get_binary_search_location_table(binary_search):  #105 (line in Coconut source)
    folder_a = get_binary_search_folder(binary_search, "folder_a")  #106 (line in Coconut source)
    folder_b = get_binary_search_folder(binary_search, "folder_b")  #107 (line in Coconut source)

    mods_a = get_sorted_location_table_items_for(folder_a)  #109 (line in Coconut source)
    mods_b = get_sorted_location_table_items_for(folder_b)  #110 (line in Coconut source)
    assert len(mods_a) == len(mods_b), "{_coconut_format_0} != {_coconut_format_1} ({_coconut_format_2}, {_coconut_format_3})".format(_coconut_format_0=(len(mods_a)), _coconut_format_1=(len(mods_b)), _coconut_format_2=(folder_a), _coconut_format_3=(folder_b))  #111 (line in Coconut source)

    num_a = binary_search["num_a"]  #113 (line in Coconut source)
    assert 0 <= num_a <= len(mods_a), "invalid num_a: {_coconut_format_0} (must be in [0, {_coconut_format_1}])".format(_coconut_format_0=(num_a), _coconut_format_1=(len(mods_a)))  #114 (line in Coconut source)

    new_mods = dict(mods_a[:num_a] + mods_b[num_a:])  #116 (line in Coconut source)
    assert len(new_mods) == len(mods_a), "{_coconut_format_0} != {_coconut_format_1}".format(_coconut_format_0=(len(new_mods)), _coconut_format_1=(len(mods_a)))  #117 (line in Coconut source)

    force_include = binary_search.get("force_include", [])  #119 (line in Coconut source)
    if force_include:  #120 (line in Coconut source)
        for force_mod in force_include:  #121 (line in Coconut source)
            force_path = kill_name = None  #122 (line in Coconut source)

            if force_mod in dict(mods_a):  #124 (line in Coconut source)
                pos_a = list((name for name, path in mods_a)).index(force_mod)  #125 (line in Coconut source)
                if pos_a + 1 > num_a:  #126 (line in Coconut source)
                    kill_name, path_b = mods_b[pos_a]  #127 (line in Coconut source)
                    name_a, force_path = mods_a[pos_a]  #128 (line in Coconut source)
                    assert name_a == force_mod, "{_coconut_format_0} != {_coconut_format_1}".format(_coconut_format_0=(name_a), _coconut_format_1=(force_mod))  #129 (line in Coconut source)

            else:  #131 (line in Coconut source)
                pos_b = list((name for name, path in mods_b)).index(force_mod)  #132 (line in Coconut source)
                if pos_b + 1 <= num_a:  #133 (line in Coconut source)
                    kill_name, path_a = mods_a[pos_b]  #134 (line in Coconut source)
                    name_b, force_path = mods_b[pos_b]  #135 (line in Coconut source)
                    assert name_b == force_mod, "{_coconut_format_0} != {_coconut_format_1}".format(_coconut_format_0=(name_b), _coconut_format_1=(force_mod))  #136 (line in Coconut source)

            if force_path is None:  #138 (line in Coconut source)
                assert force_mod in new_mods, "{_coconut_format_0} not in {_coconut_format_1}".format(_coconut_format_0=(force_mod), _coconut_format_1=(new_mods.keys()))  #139 (line in Coconut source)
            else:  #140 (line in Coconut source)
                assert kill_name in new_mods, "{_coconut_format_0} not in {_coconut_format_1}".format(_coconut_format_0=(kill_name), _coconut_format_1=(new_mods.keys()))  #141 (line in Coconut source)
                print("(forcing {_coconut_format_0} instead of {_coconut_format_1})".format(_coconut_format_0=(force_path), _coconut_format_1=(new_mods[kill_name])))  #142 (line in Coconut source)
                del new_mods[kill_name]  #143 (line in Coconut source)
                new_mods[force_mod] = force_path  #144 (line in Coconut source)

    return new_mods  #146 (line in Coconut source)



def main():  #149 (line in Coconut source)
    ensure_dirs()  #150 (line in Coconut source)

    print("\nFixing client only mods...")  #152 (line in Coconut source)
    extra_server_mods = get_location_table_for(EXTRA_MODS_DIR)  #153 (line in Coconut source)
    extra_client_only_mods = get_location_table_for(EXTRA_CLIENT_MODS_DIR)  #154 (line in Coconut source)

    remove_mods_in_from(extra_server_mods, extra_client_only_mods)  #156 (line in Coconut source)

    base_server_mods = get_location_table_for(BASE_MODS_DIR)  #158 (line in Coconut source)
    base_client_only_mods = get_location_table_for(BASE_CLIENT_MODS_DIR)  #159 (line in Coconut source)

    remove_mods_in_from(base_server_mods, base_client_only_mods)  #161 (line in Coconut source)


    print("\nFixing main mods...")  #164 (line in Coconut source)
    all_base_mods = get_location_table_for(BASE_MODS_DIR)  #165 (line in Coconut source)
    all_base_mods.update(get_location_table_for(BASE_CLIENT_MODS_DIR))  #166 (line in Coconut source)

    extra_server_mods = get_location_table_for(EXTRA_MODS_DIR)  #168 (line in Coconut source)
    extra_client_only_mods = get_location_table_for(EXTRA_CLIENT_MODS_DIR)  #169 (line in Coconut source)

    remove_mods_in_from(all_base_mods, extra_server_mods)  #171 (line in Coconut source)
    remove_mods_in_from(all_base_mods, extra_client_only_mods)  #172 (line in Coconut source)

    remove_mods_in_from(extra_server_mods, extra_client_only_mods)  #174 (line in Coconut source)


    print("\nMerging server mods...")  #177 (line in Coconut source)
    all_server_mods = get_location_table_for(BASE_MODS_DIR)  #178 (line in Coconut source)
    all_server_mods.update(get_location_table_for(EXTRA_MODS_DIR))  #179 (line in Coconut source)

    current_server_mods = get_location_table_for(MODS_DIR)  #181 (line in Coconut source)

    set_mods_from_to(all_server_mods, current_server_mods, MODS_DIR)  #183 (line in Coconut source)


    print("\nMerging client only mods...")  #186 (line in Coconut source)
    all_client_only_mods = get_location_table_for(BASE_CLIENT_MODS_DIR)  #187 (line in Coconut source)
    all_client_only_mods.update(get_location_table_for(EXTRA_CLIENT_MODS_DIR))  #188 (line in Coconut source)

    current_client_only_mods = get_location_table_for(CLIENT_MODS_DIR)  #190 (line in Coconut source)

    set_mods_from_to(all_client_only_mods, current_client_only_mods, CLIENT_MODS_DIR)  #192 (line in Coconut source)


    print("\nFixing removed mods...")  #195 (line in Coconut source)
    removed_server_mods = get_location_table_for(REMOVED_MODS_DIR)  #196 (line in Coconut source)
    remove_mods_in_from(all_server_mods, removed_server_mods)  #197 (line in Coconut source)

    removed_client_mods = get_location_table_for(REMOVED_CLIENT_MODS_DIR)  #199 (line in Coconut source)
    remove_mods_in_from(removed_server_mods, removed_client_mods)  #200 (line in Coconut source)
    remove_mods_in_from(all_server_mods, removed_client_mods)  #201 (line in Coconut source)
    remove_mods_in_from(all_client_only_mods, removed_client_mods)  #202 (line in Coconut source)


    binary_search = load_binary_search_file()  #205 (line in Coconut source)
    if binary_search["searching"]:  #206 (line in Coconut source)

        print("\nAdding mods from binary search...")  #208 (line in Coconut source)
        binary_search_mods = get_binary_search_location_table(binary_search)  #209 (line in Coconut source)

        destination_dir = binary_search["destination"]  #211 (line in Coconut source)
        destination_mods = get_location_table_for(destination_dir)  #212 (line in Coconut source)

        add_mods_from_to(binary_search_mods, destination_mods, destination_dir)  #214 (line in Coconut source)




if __name__ == "__main__":  #218 (line in Coconut source)
    main()  #219 (line in Coconut source)
