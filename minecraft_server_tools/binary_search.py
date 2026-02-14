#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xae6fb30a

# Compiled with Coconut version 3.2.0-post_dev15

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev15', '', True)
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

from minecraft_server_tools import sync_mods  #1 (line in Coconut source)
from minecraft_server_tools.constants import COMMENT_JSON  #2 (line in Coconut source)
from minecraft_server_tools.constants import BINARY_SEARCH_FILE  #2 (line in Coconut source)
from minecraft_server_tools.constants import YES_STRS  #2 (line in Coconut source)
from minecraft_server_tools.constants import NO_STRS  #2 (line in Coconut source)
from minecraft_server_tools.constants import UPDATED_MODS_DIR_SUFFIX  #2 (line in Coconut source)
from minecraft_server_tools.constants import OLD_MODS_DIR_SUFFIX  #2 (line in Coconut source)
from minecraft_server_tools.constants import BASE_MODS_NAME  #2 (line in Coconut source)
from minecraft_server_tools.constants import MODS_NAME  #2 (line in Coconut source)


def write_binary_search_file(binary_search):  #14 (line in Coconut source)
    COMMENT_JSON.dumpf(binary_search, BINARY_SEARCH_FILE)  #15 (line in Coconut source)



@_coconut_tco  #18 (line in Coconut source)
def get_num_mods_in(folder):  #18 (line in Coconut source)
    return _coconut_tail_call(len, sync_mods.get_location_table_for(folder))  #19 (line in Coconut source)



def init_binary_search(folder_a, folder_b, destination):  #22 (line in Coconut source)
    binary_search = _coconut.dict((("searching", True), ("folder_a", folder_a), ("folder_b", folder_b), ("destination", destination), ("results", [])))  #23 (line in Coconut source)

    num_mods_in_a = get_num_mods_in(sync_mods.get_binary_search_folder(binary_search, "folder_a"))  #31 (line in Coconut source)
    num_mods_in_b = get_num_mods_in(sync_mods.get_binary_search_folder(binary_search, "folder_b"))  #32 (line in Coconut source)
    assert num_mods_in_a == num_mods_in_b, "{_coconut_format_0} != {_coconut_format_1}".format(_coconut_format_0=(num_mods_in_a), _coconut_format_1=(num_mods_in_b))  #33 (line in Coconut source)

    binary_search["num_a"] = num_mods_in_a // 2  #35 (line in Coconut source)

    old_binary_search = sync_mods.load_binary_search_file()  #37 (line in Coconut source)
    if old_binary_search not in (binary_search, _coconut.dict((("searching", False),))):  #38 (line in Coconut source)
        binary_search["backup"] = old_binary_search  #39 (line in Coconut source)

    write_binary_search_file(binary_search)  #41 (line in Coconut source)
    return binary_search  #42 (line in Coconut source)



def get_binary_search_window(binary_search):  #45 (line in Coconut source)
    num_mods_in_a = get_num_mods_in(sync_mods.get_binary_search_folder(binary_search, "folder_a"))  #46 (line in Coconut source)

    window_min, window_max = 0, num_mods_in_a  #48 (line in Coconut source)
    prev_num_a = None  #49 (line in Coconut source)
    new_num_a = num_mods_in_a // 2  #50 (line in Coconut source)
    for r in binary_search["results"]:  #51 (line in Coconut source)
        prev_num_a = (window_min + window_max) // 2  #52 (line in Coconut source)
        if r:  #53 (line in Coconut source)
            window_min = prev_num_a  #54 (line in Coconut source)
        else:  #55 (line in Coconut source)
            window_max = prev_num_a  #56 (line in Coconut source)
        new_num_a = (window_min + window_max) // 2  #57 (line in Coconut source)
    return window_min, window_max, prev_num_a, new_num_a  #58 (line in Coconut source)



def binary_search_step(binary_search):  #61 (line in Coconut source)
    assert binary_search["results"], "can't binary_search_step if no results"  #62 (line in Coconut source)

    window_min, window_max, prev_num_a, new_num_a = get_binary_search_window(binary_search)  #64 (line in Coconut source)

    if new_num_a == prev_num_a:  #66 (line in Coconut source)
        return True, binary_search  #67 (line in Coconut source)

    assert binary_search["num_a"] is None or binary_search["num_a"] == prev_num_a, "{_coconut_format_0} != {_coconut_format_1}".format(_coconut_format_0=(binary_search['num_a']), _coconut_format_1=(num_a))  #69 (line in Coconut source)

    new_binary_search = binary_search.copy()  #71 (line in Coconut source)
    new_binary_search["num_a"] = new_num_a  #72 (line in Coconut source)
    write_binary_search_file(new_binary_search)  #73 (line in Coconut source)

    return False, new_binary_search  #75 (line in Coconut source)



def get_bool_input(message):  #78 (line in Coconut source)
    while True:  #79 (line in Coconut source)
        got = input(message + " ").lower()  #80 (line in Coconut source)
        if got in YES_STRS:  #81 (line in Coconut source)
            return True  #82 (line in Coconut source)
        elif got in NO_STRS:  #83 (line in Coconut source)
            return False  #84 (line in Coconut source)
        else:  #85 (line in Coconut source)
            print("Unrecognized input; try again.")  #86 (line in Coconut source)



def add_result(binary_search, result):  #89 (line in Coconut source)
    new_binary_search = binary_search.copy()  #90 (line in Coconut source)
    new_binary_search["results"].append(result)  #91 (line in Coconut source)
    write_binary_search_file(new_binary_search)  #92 (line in Coconut source)
    return new_binary_search  #93 (line in Coconut source)



def show_search_delta(old_binary_search, new_binary_search):  #96 (line in Coconut source)
    assert old_binary_search["num_a"] != new_binary_search["num_a"], "{_coconut_format_0} != {_coconut_format_1}".format(_coconut_format_0=(old_binary_search['num_a']), _coconut_format_1=(new_binary_search['num_a']))  #97 (line in Coconut source)

    old_mods = sync_mods.get_binary_search_location_table(old_binary_search)  #99 (line in Coconut source)
    new_mods = sync_mods.get_binary_search_location_table(new_binary_search)  #100 (line in Coconut source)

    print("New binary search step:")  #102 (line in Coconut source)
    for mod in old_mods:  #103 (line in Coconut source)
        if mod not in new_mods:  #104 (line in Coconut source)
            print("\tout:", mod)  #105 (line in Coconut source)
    for mod in new_mods:  #106 (line in Coconut source)
        if mod not in old_mods:  #107 (line in Coconut source)
            print("\tin:", mod)  #108 (line in Coconut source)



def show_search_results(binary_search):  #111 (line in Coconut source)
    window_min, window_max, prev_num_a, new_num_a = get_binary_search_window(binary_search)  #112 (line in Coconut source)

    mods_a = sync_mods.get_sorted_location_table_items_for(sync_mods.get_binary_search_folder(binary_search, "folder_a"))  #114 (line in Coconut source)
    mods_b = sync_mods.get_sorted_location_table_items_for(sync_mods.get_binary_search_folder(binary_search, "folder_b"))  #115 (line in Coconut source)

    zipped_mods = list(zip(mods_a, mods_b))  #117 (line in Coconut source)
    clean_mods = zipped_mods[:window_min]  #118 (line in Coconut source)
    culprits = zipped_mods[window_min:window_max]  #119 (line in Coconut source)

    print("Clean mods:")  #121 (line in Coconut source)
    for (name_a, path_a), (name_b, path_b) in clean_mods:  #122 (line in Coconut source)
        print("- {_coconut_format_0} -> {_coconut_format_1}".format(_coconut_format_0=(name_a), _coconut_format_1=(name_b)))  #123 (line in Coconut source)

    print("Culprit mods:")  #125 (line in Coconut source)
    for (name_a, path_a), (name_b, path_b) in culprits:  #126 (line in Coconut source)
        print("- {_coconut_format_0} -> {_coconut_format_1}".format(_coconut_format_0=(name_a), _coconut_format_1=(name_b)))  #127 (line in Coconut source)



def run_binary_search(binary_search):  #130 (line in Coconut source)
    if binary_search["num_a"] is None:  #131 (line in Coconut source)
        done, binary_search = binary_search_step(binary_search)  #132 (line in Coconut source)
        assert done is False, done  #133 (line in Coconut source)

    fake_old_binary_search = binary_search.copy()  #135 (line in Coconut source)
    fake_old_binary_search["num_a"] = 0  #136 (line in Coconut source)
    show_search_delta(fake_old_binary_search, binary_search)  #137 (line in Coconut source)

    done = False  #139 (line in Coconut source)
    while not done:  #140 (line in Coconut source)
        done, new_binary_search = binary_search_step(add_result(binary_search, get_bool_input("Enter binary search result (did it work?):")))  #141 (line in Coconut source)

        show_search_results(new_binary_search)  #143 (line in Coconut source)
        if not done:  #144 (line in Coconut source)
            show_search_delta(binary_search, new_binary_search)  #145 (line in Coconut source)

        binary_search = new_binary_search  #147 (line in Coconut source)



def disable_binary_search(binary_search):  #150 (line in Coconut source)
    new_binary_search = binary_search.copy()  #151 (line in Coconut source)
    new_binary_search["searching"] = False  #152 (line in Coconut source)
    write_binary_search_file(new_binary_search)  #153 (line in Coconut source)



def main(folder_a, folder_b, destination):  #156 (line in Coconut source)
    binary_search = sync_mods.load_binary_search_file()  #157 (line in Coconut source)
    if binary_search["searching"]:  #158 (line in Coconut source)
        new = not get_bool_input("It looks like you already have a search in progress. Continue?")  #159 (line in Coconut source)
    else:  #160 (line in Coconut source)
        new = True  #161 (line in Coconut source)

    if new:  #163 (line in Coconut source)
        binary_search = init_binary_search(folder_a, folder_b, destination)  #164 (line in Coconut source)

    run_binary_search(binary_search)  #166 (line in Coconut source)
    disable_binary_search(binary_search)  #167 (line in Coconut source)




if __name__ == "__main__":  #171 (line in Coconut source)
    main(BASE_MODS_NAME + UPDATED_MODS_DIR_SUFFIX, BASE_MODS_NAME + OLD_MODS_DIR_SUFFIX, MODS_NAME)  #172 (line in Coconut source)
