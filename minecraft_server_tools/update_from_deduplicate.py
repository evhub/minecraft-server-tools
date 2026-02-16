#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7c4b0758

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

from minecraft_server_tools import sync_mods  #3 (line in Coconut source)
from minecraft_server_tools import update_mods  #3 (line in Coconut source)
from minecraft_server_tools import deduplicate_mods  #3 (line in Coconut source)
from minecraft_server_tools.constants import UPDATED_MODS_DIR_SUFFIX  #8 (line in Coconut source)
from minecraft_server_tools.constants import OLD_MODS_DIR_SUFFIX  #8 (line in Coconut source)


def update_mods_from(update_from_dir, mods_dir):  #14 (line in Coconut source)
    names_to_jars_mods = update_mods.get_mod_names_to_jar_names(mods_dir, silent=True)  #15 (line in Coconut source)
    names_to_jars_update_from = update_mods.get_mod_names_to_jar_names(update_from_dir, silent=True)  #16 (line in Coconut source)

    updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #18 (line in Coconut source)
    old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #19 (line in Coconut source)

    print("\nUpdating {_coconut_format_0!r}...".format(_coconut_format_0=(mods_dir)))  #21 (line in Coconut source)
    made_dirs = False  #22 (line in Coconut source)
    for name, mods_jar in names_to_jars_mods.items():  #23 (line in Coconut source)
        update_jar = names_to_jars_update_from.get(name)  #24 (line in Coconut source)
        if update_jar is not None and mods_jar != update_jar:  #25 (line in Coconut source)
            if not made_dirs:  #26 (line in Coconut source)
                update_mods.make_dirs(updated_mods_dir, old_mods_dir)  #27 (line in Coconut source)
                made_dirs = True  #28 (line in Coconut source)

            print("\t{_coconut_format_0} -> {_coconut_format_1}".format(_coconut_format_0=(mods_jar), _coconut_format_1=(update_jar)))  #30 (line in Coconut source)
            current_jar_path = os.path.join(mods_dir, mods_jar)  #31 (line in Coconut source)
            old_jar_path = os.path.join(old_mods_dir, mods_jar)  #32 (line in Coconut source)
            os.rename(current_jar_path, old_jar_path)  #33 (line in Coconut source)

            update_from_jar_path = os.path.join(update_from_dir, update_jar)  #35 (line in Coconut source)
            updates_jar_path = os.path.join(updated_mods_dir, update_jar)  #36 (line in Coconut source)
            os.rename(update_from_jar_path, updates_jar_path)  #37 (line in Coconut source)



def main():  #40 (line in Coconut source)
    deduplicate_mods.fix_deduplicate_mods()  #41 (line in Coconut source)

    removed_mod_names = deduplicate_mods.get_all_mod_names([sync_mods.REMOVED_MODS_DIR, sync_mods.REMOVED_CLIENT_MODS_DIR, sync_mods.STAGING_MODS_DIR, sync_mods.STAGING_CLIENT_MODS_DIR])  #43 (line in Coconut source)
    deduplicate_mods.deduplicate_mods(deduplicate_mods.DEDUPLICATE_CLIENT_MODS_DIR, removed_mod_names)  #49 (line in Coconut source)
    deduplicate_mods.deduplicate_mods(deduplicate_mods.DEDUPLICATE_MODS_DIR, removed_mod_names)  #50 (line in Coconut source)

    update_mods_from(deduplicate_mods.DEDUPLICATE_CLIENT_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR)  #52 (line in Coconut source)
    update_mods_from(deduplicate_mods.DEDUPLICATE_CLIENT_MODS_DIR, sync_mods.EXTRA_CLIENT_MODS_DIR)  #53 (line in Coconut source)

    update_mods_from(deduplicate_mods.DEDUPLICATE_MODS_DIR, sync_mods.BASE_MODS_DIR)  #55 (line in Coconut source)
    update_mods_from(deduplicate_mods.DEDUPLICATE_MODS_DIR, sync_mods.EXTRA_MODS_DIR)  #56 (line in Coconut source)

    update_mods_from(deduplicate_mods.DEDUPLICATE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR)  #58 (line in Coconut source)
    update_mods_from(deduplicate_mods.DEDUPLICATE_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR)  #59 (line in Coconut source)

    update_mods_from(deduplicate_mods.DEDUPLICATE_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR)  #61 (line in Coconut source)
    update_mods_from(deduplicate_mods.DEDUPLICATE_MODS_DIR, sync_mods.EXTRA_CLIENT_MODS_DIR)  #62 (line in Coconut source)



if __name__ == "__main__":  #65 (line in Coconut source)
    main()  #66 (line in Coconut source)
