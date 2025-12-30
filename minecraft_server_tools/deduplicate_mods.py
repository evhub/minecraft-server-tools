#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1a04522b

# Compiled with Coconut version 3.2.0

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0', '', True)
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

from minecraft_server_tools import sync_mods  #3 (line in Coconut source)
from minecraft_server_tools import update_mods  #3 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_DIR  #4 (line in Coconut source)
from minecraft_server_tools.constants import DEDUPLICATE_MODS_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import DEDUPLICATE_CLIENT_MODS_NAME  #4 (line in Coconut source)


DEDUPLICATE_MODS_DIR = os.path.join(SERVER_DIR, DEDUPLICATE_MODS_NAME)  #11 (line in Coconut source)
DEDUPLICATE_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, DEDUPLICATE_CLIENT_MODS_NAME)  #12 (line in Coconut source)

ALL_MODS_DIRS = (sync_mods.BASE_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.REMOVED_MODS_DIR, sync_mods.STAGING_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.REMOVED_CLIENT_MODS_DIR, sync_mods.STAGING_CLIENT_MODS_DIR)  #14 (line in Coconut source)


silent_mod_names_to_jar_names = _coconut_partial(update_mods.get_mod_names_to_jar_names, silent=True)  #26 (line in Coconut source)


def get_all_mod_names(mods_dirs):  #29 (line in Coconut source)
    all_mod_names = _coconut.dict()  #30 (line in Coconut source)
    for dirname in mods_dirs:  #31 (line in Coconut source)
        if os.path.exists(dirname):  #32 (line in Coconut source)
            for mod_name, jar_name in silent_mod_names_to_jar_names(dirname).items():  #33 (line in Coconut source)
                assert mod_name not in all_mod_names, "found multiple jars with same mod name {_coconut_format_0!r}: {_coconut_format_1!r}, {_coconut_format_2!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(all_mod_names[mod_name]), _coconut_format_2=(jar_name))  #34 (line in Coconut source)
                all_mod_names[mod_name] = jar_name  #35 (line in Coconut source)
    return all_mod_names  #36 (line in Coconut source)



def add_new_mods(new_mods_dir, to_mods_dir, all_mod_names):  #39 (line in Coconut source)
    to_mods_dir_mod_names = silent_mod_names_to_jar_names(to_mods_dir)  #40 (line in Coconut source)
    made_changes = False  #41 (line in Coconut source)
    if os.path.exists(new_mods_dir):  #42 (line in Coconut source)
        print("\nLooking for new mods in: {_coconut_format_0}".format(_coconut_format_0=(new_mods_dir)))  #43 (line in Coconut source)
        for mod_name, jar_name in silent_mod_names_to_jar_names(new_mods_dir).items():  #44 (line in Coconut source)
            from_path = os.path.join(new_mods_dir, jar_name)  #45 (line in Coconut source)
            if mod_name not in all_mod_names:  #46 (line in Coconut source)
                to_path = os.path.join(to_mods_dir, jar_name)  #47 (line in Coconut source)
                print("Adding new mod: {_coconut_format_0} (from {_coconut_format_1!r})".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #48 (line in Coconut source)
                os.rename(from_path, to_path)  #49 (line in Coconut source)
                made_changes = True  #50 (line in Coconut source)
            elif mod_name in to_mods_dir_mod_names:  #51 (line in Coconut source)
                sync_mods.rm_mod(from_path)  #52 (line in Coconut source)
        if made_changes:  #53 (line in Coconut source)
            sync_mods.main()  #54 (line in Coconut source)
        else:  #55 (line in Coconut source)
            print("Found no new mods in: {_coconut_format_0}\n".format(_coconut_format_0=(new_mods_dir)))  #56 (line in Coconut source)
    else:  #57 (line in Coconut source)
        print("\nSkipping adding new mods from: {_coconut_format_0}\n".format(_coconut_format_0=(new_mods_dir)))  #58 (line in Coconut source)
    return made_changes  #59 (line in Coconut source)



def deduplicate_mods(new_mods_dir, all_mod_names, warn_only=False):  #62 (line in Coconut source)
    if os.path.exists(new_mods_dir):  #63 (line in Coconut source)
        print("\nDeduplicating mods in: {_coconut_format_0}".format(_coconut_format_0=(new_mods_dir)))  #64 (line in Coconut source)
        for mod_name, all_jar_names in update_mods.get_mod_names_to_all_jar_names(new_mods_dir, silent=True).items():  #65 (line in Coconut source)
            for jar_name in all_jar_names:  #66 (line in Coconut source)
                from_path = os.path.join(new_mods_dir, jar_name)  #67 (line in Coconut source)
                if mod_name in all_mod_names:  #68 (line in Coconut source)
                    if warn_only:  #69 (line in Coconut source)
                        print("\tFound duplicate mod: {_coconut_format_0}".format(_coconut_format_0=(from_path)))  #70 (line in Coconut source)
                    else:  #71 (line in Coconut source)
                        sync_mods.rm_mod(from_path)  #72 (line in Coconut source)



def fix_deduplicate_mods():  #75 (line in Coconut source)
    sync_mods.main()  #76 (line in Coconut source)
    print("\nFixing to deduplicate mods...")  #77 (line in Coconut source)
    sync_mods.remove_mods_in_from(sync_mods.get_location_table_for(DEDUPLICATE_MODS_DIR), sync_mods.get_location_table_for(DEDUPLICATE_CLIENT_MODS_DIR))  #78 (line in Coconut source)



def warn_duplicate_mods():  #84 (line in Coconut source)
    for i, mods_dir in enumerate(ALL_MODS_DIRS):  #85 (line in Coconut source)
        other_mod_names = get_all_mod_names(ALL_MODS_DIRS[:i] + ALL_MODS_DIRS[i + 1:])  #86 (line in Coconut source)
        deduplicate_mods(mods_dir, other_mod_names, warn_only=True)  #87 (line in Coconut source)



def main():  #90 (line in Coconut source)
    fix_deduplicate_mods()  #91 (line in Coconut source)

    all_mod_names = get_all_mod_names([sync_mods.MODS_DIR, sync_mods.CLIENT_MODS_DIR, sync_mods.REMOVED_MODS_DIR, sync_mods.REMOVED_CLIENT_MODS_DIR, sync_mods.STAGING_MODS_DIR, sync_mods.STAGING_CLIENT_MODS_DIR])  #93 (line in Coconut source)
    deduplicate_mods(DEDUPLICATE_CLIENT_MODS_DIR, all_mod_names)  #101 (line in Coconut source)
    deduplicate_mods(DEDUPLICATE_MODS_DIR, all_mod_names)  #102 (line in Coconut source)



if __name__ == "__main__":  #105 (line in Coconut source)
    main()  #106 (line in Coconut source)
