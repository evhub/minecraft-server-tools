#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2b4b8605

# Compiled with Coconut version 3.2.0-post_dev9

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev9', '', True)
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
import webbrowser  #2 (line in Coconut source)
try:  #3 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #3 (line in Coconut source)
except _coconut.NameError:  #3 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #3 (line in Coconut source)
sys = _coconut_sys  #3 (line in Coconut source)
if sys.version_info >= (3,):  #3 (line in Coconut source)
    import urllib.parse  #3 (line in Coconut source)
else:  #3 (line in Coconut source)
    import urllib as _coconut_import_0  #3 (line in Coconut source)
    try:  #3 (line in Coconut source)
        urllib  #3 (line in Coconut source)
    except:  #3 (line in Coconut source)
        urllib = _coconut.types.ModuleType(_coconut_py_str("urllib"))  #3 (line in Coconut source)
    else:  #3 (line in Coconut source)
        if not _coconut.isinstance(urllib, _coconut.types.ModuleType):  #3 (line in Coconut source)
            urllib = _coconut.types.ModuleType(_coconut_py_str("urllib"))  #3 (line in Coconut source)
    urllib.parse = _coconut_import_0  #3 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #3 (line in Coconut source)
    sys = _coconut_sys_0  #3 (line in Coconut source)

from minecraft_server_tools import update_mods  #5 (line in Coconut source)
from minecraft_server_tools.constants import SERVER_DIR  #6 (line in Coconut source)
from minecraft_server_tools.constants import DEDUPLICATE_MODS_NAME  #6 (line in Coconut source)
from minecraft_server_tools.constants import DEDUPLICATE_CLIENT_MODS_NAME  #6 (line in Coconut source)
from minecraft_server_tools.constants import MODLOADER  #6 (line in Coconut source)
from minecraft_server_tools.constants import MC_VERSION  #6 (line in Coconut source)
from minecraft_server_tools.constants import SEARCH_MODS_GOOGLE_TEMPLATE  #6 (line in Coconut source)
from minecraft_server_tools.constants import MAX_BROWSER_SEARCHES  #6 (line in Coconut source)
from minecraft_server_tools.constants import ver_join  #6 (line in Coconut source)


DEDUPLICATE_MODS_DIR = os.path.join(SERVER_DIR, DEDUPLICATE_MODS_NAME)  #18 (line in Coconut source)
DEDUPLICATE_CLIENT_MODS_DIR = os.path.join(SERVER_DIR, DEDUPLICATE_CLIENT_MODS_NAME)  #19 (line in Coconut source)


def get_search_url(mod_name):  #22 (line in Coconut source)
    query = SEARCH_MODS_GOOGLE_TEMPLATE.format(mod_name=mod_name, modloader=MODLOADER, mc_version_2=ver_join(MC_VERSION[:2]))  #23 (line in Coconut source)
    return "https://www.google.com/search?" + urllib.parse.urlencode(_coconut.dict((("q", query),)))  #28 (line in Coconut source)



@_coconut_tco  #31 (line in Coconut source)
def get_mods_in_dir(mods_dir):  #31 (line in Coconut source)
    """Get mod names to jar names dict for a directory, or empty dict if doesn't exist."""  #32 (line in Coconut source)
    if not os.path.exists(mods_dir):  #33 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #34 (line in Coconut source)
    return _coconut_tail_call(update_mods.get_mod_names_to_jar_names, mods_dir, silent=True)  #35 (line in Coconut source)



def search_mods(mod_names_to_jar_names, mods_dir, limit=MAX_BROWSER_SEARCHES):  #38 (line in Coconut source)
    """Open browser searches for mods, up to limit."""  #39 (line in Coconut source)
    if not mod_names_to_jar_names:  #40 (line in Coconut source)
        print("No mods found in: {_coconut_format_0}".format(_coconut_format_0=(mods_dir)))  #41 (line in Coconut source)
        return 0  #42 (line in Coconut source)

    items = list(mod_names_to_jar_names.items())[:limit]  #44 (line in Coconut source)
    total = len(mod_names_to_jar_names)  #45 (line in Coconut source)
    showing = len(items)  #46 (line in Coconut source)

    if showing < total:  #48 (line in Coconut source)
        print("\nOpening searches for first {_coconut_format_0} of {_coconut_format_1} mods in: {_coconut_format_2}".format(_coconut_format_0=(showing), _coconut_format_1=(total), _coconut_format_2=(mods_dir)))  #49 (line in Coconut source)
    else:  #50 (line in Coconut source)
        print("\nOpening searches for {_coconut_format_0} mods in: {_coconut_format_1}".format(_coconut_format_0=(showing), _coconut_format_1=(mods_dir)))  #51 (line in Coconut source)

    for mod_name, jar_name in items:  #53 (line in Coconut source)
        url = get_search_url(mod_name)  #54 (line in Coconut source)
        print("  Searching for: {_coconut_format_0} ({_coconut_format_1})".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #55 (line in Coconut source)
        webbrowser.open(url)  #56 (line in Coconut source)

    return showing  #58 (line in Coconut source)



def main():  #61 (line in Coconut source)
    print("Searching for mods in deduplicate directories...")  #62 (line in Coconut source)

# Try client mods first
    client_mods = get_mods_in_dir(DEDUPLICATE_CLIENT_MODS_DIR)  #65 (line in Coconut source)
    if client_mods:  #66 (line in Coconut source)
        search_mods(client_mods, DEDUPLICATE_CLIENT_MODS_DIR)  #67 (line in Coconut source)
    else:  #68 (line in Coconut source)
# Only search non-client mods if client mods is empty
        print("No client mods to deduplicate, checking server mods...")  #70 (line in Coconut source)
        server_mods = get_mods_in_dir(DEDUPLICATE_MODS_DIR)  #71 (line in Coconut source)
        search_mods(server_mods, DEDUPLICATE_MODS_DIR)  #72 (line in Coconut source)

    print("\nDone!")  #74 (line in Coconut source)



if __name__ == "__main__":  #77 (line in Coconut source)
    main()  #78 (line in Coconut source)
