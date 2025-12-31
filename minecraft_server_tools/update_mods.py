#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x95319162

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
import json  #2 (line in Coconut source)
import subprocess  #3 (line in Coconut source)
import traceback  #4 (line in Coconut source)
import datetime  #5 (line in Coconut source)
import time  #6 (line in Coconut source)
import argparse  #7 (line in Coconut source)
from pprint import pprint  #8 (line in Coconut source)
try:  #9 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #9 (line in Coconut source)
except _coconut.NameError:  #9 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #9 (line in Coconut source)
sys = _coconut_sys  #9 (line in Coconut source)
if sys.version_info >= (3,):  #9 (line in Coconut source)
    from urllib.parse import unquote  #9 (line in Coconut source)
else:  #9 (line in Coconut source)
    from urllib import unquote  #9 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #9 (line in Coconut source)
    sys = _coconut_sys_0  #9 (line in Coconut source)
from collections import defaultdict  #10 (line in Coconut source)

import requests  #12 (line in Coconut source)

from minecraft_server_tools import sync_mods  #14 (line in Coconut source)
from minecraft_server_tools import google_api  #14 (line in Coconut source)
from minecraft_server_tools.constants import COMMENT_JSON  #15 (line in Coconut source)
from minecraft_server_tools.constants import MC_VERSION  #15 (line in Coconut source)
from minecraft_server_tools.constants import COMPONENT_SEPS  #15 (line in Coconut source)
from minecraft_server_tools.constants import NON_NAME_COMPONENT_REGEX  #15 (line in Coconut source)
from minecraft_server_tools.constants import NAME_REGEXES_TO_SPACE  #15 (line in Coconut source)
from minecraft_server_tools.constants import GOOGLE_QUERY_TEMPLATE  #15 (line in Coconut source)
from minecraft_server_tools.constants import NON_CURSEFORGE_MODS  #15 (line in Coconut source)
from minecraft_server_tools.constants import MODLOADER  #15 (line in Coconut source)
from minecraft_server_tools.constants import WRONG_MODLOADERS  #15 (line in Coconut source)
from minecraft_server_tools.constants import MAYBE_WRONG_MODLOADERS  #15 (line in Coconut source)
from minecraft_server_tools.constants import MOD_PAGE_NAME_SUFFICES  #15 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_NAMES_FILE  #15 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_IDS_CACHE_FILE  #15 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_FILE  #15 (line in Coconut source)
from minecraft_server_tools.constants import TIMESTAMP_FORMAT_REGEX  #15 (line in Coconut source)
from minecraft_server_tools.constants import UPDATED_MODS_DIR_SUFFIX  #15 (line in Coconut source)
from minecraft_server_tools.constants import OLD_MODS_DIR_SUFFIX  #15 (line in Coconut source)
from minecraft_server_tools.constants import PRINT_DEBUG  #15 (line in Coconut source)
from minecraft_server_tools.constants import MAX_DEBUG_RESULTS  #15 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_NAME_ELEMS_TO_STRIP  #15 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_QUERY_TEMPLATES  #15 (line in Coconut source)
from minecraft_server_tools.constants import ALWAYS_USE_LATEST_VERSION_FOR_MODS  #15 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_RETRIES  #15 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_RETRY_DELAY  #15 (line in Coconut source)
from minecraft_server_tools.constants import AVOID_FILES_PUBLISHED_WITHIN  #15 (line in Coconut source)
from minecraft_server_tools.constants import FIX_MOD_NAMES  #15 (line in Coconut source)
from minecraft_server_tools.constants import NO_COMPONENT_SPLIT_MODS  #15 (line in Coconut source)
from minecraft_server_tools.constants import USE_ALL_COMPONENTS_MODS  #15 (line in Coconut source)
from minecraft_server_tools.constants import ver_join  #15 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #15 (line in Coconut source)


UPDATE_MODS_DIRS = [sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR]  #49 (line in Coconut source)

BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #56 (line in Coconut source)


@_coconut_tco  #59 (line in Coconut source)
def get_mod_name(jar_name, silent=None, do_component_splitting=True, use_all_components=False):  #59 (line in Coconut source)
    def _coconut_mock_0(jar_name, silent=_coconut_sentinel, do_component_splitting=_coconut_sentinel, use_all_components=_coconut_sentinel):  #60 (line in Coconut source)
        if silent is _coconut_sentinel: silent = _coconut_recursive_func_0._coconut_tco_func.__defaults__[0]  #60 (line in Coconut source)
        if do_component_splitting is _coconut_sentinel: do_component_splitting = _coconut_recursive_func_0._coconut_tco_func.__defaults__[1]  #60 (line in Coconut source)
        if use_all_components is _coconut_sentinel: use_all_components = _coconut_recursive_func_0._coconut_tco_func.__defaults__[2]  #60 (line in Coconut source)
        return (jar_name, silent, do_component_splitting, use_all_components,)  #60 (line in Coconut source)
    while True:  #60 (line in Coconut source)
        if silent is None:  #60 (line in Coconut source)
            silent = not PRINT_DEBUG  #61 (line in Coconut source)

        base_name = jar_name.removesuffix(".jar")  #63 (line in Coconut source)

        if do_component_splitting:  #65 (line in Coconut source)
            for sep, min_count in COMPONENT_SEPS:  #66 (line in Coconut source)
                components = base_name.split(sep)  #67 (line in Coconut source)
                if len(components) > min_count:  #68 (line in Coconut source)
                    break  #69 (line in Coconut source)
            else:  #70 (line in Coconut source)
                if not silent:  #71 (line in Coconut source)
                    print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #72 (line in Coconut source)
                components = [base_name,]  #73 (line in Coconut source)

            name_cmpnts = []  #75 (line in Coconut source)
            for cmpnt in components:  #76 (line in Coconut source)
                is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #77 (line in Coconut source)
                if is_name_cmpnt:  #78 (line in Coconut source)
                    name_cmpnts.append(cmpnt)  #79 (line in Coconut source)
                elif name_cmpnts and not use_all_components:  #80 (line in Coconut source)
                    break  #81 (line in Coconut source)
            if not name_cmpnts:  #82 (line in Coconut source)
                if not silent:  #83 (line in Coconut source)
                    print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #84 (line in Coconut source)
                name_cmpnts = [components[0],]  #85 (line in Coconut source)
            mod_name = " ".join(name_cmpnts)  #86 (line in Coconut source)
        else:  #87 (line in Coconut source)
            mod_name = base_name  #88 (line in Coconut source)

        for to_space in NAME_REGEXES_TO_SPACE:  #90 (line in Coconut source)
            mod_name = to_space.sub(" ", mod_name)  #91 (line in Coconut source)

        if not mod_name:  #93 (line in Coconut source)
            if not silent:  #94 (line in Coconut source)
                print("Got empty mod name for jar {_coconut_format_0!r}; falling back to no component splitting.".format(_coconut_format_0=(jar_name)))  #95 (line in Coconut source)
            try:  #96 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #96 (line in Coconut source)
            except _coconut.NameError:  #96 (line in Coconut source)
                _coconut_tre_check_0 = False  #96 (line in Coconut source)
            if _coconut_tre_check_0:  #96 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #96 (line in Coconut source)
                continue  #96 (line in Coconut source)
            else:  #96 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #96 (line in Coconut source)


        camel_case_parts = [mod_name[0],]  #98 (line in Coconut source)
        prev_is_lower = mod_name[0].islower()  #99 (line in Coconut source)
        for c in mod_name[1:]:  #100 (line in Coconut source)
            if prev_is_lower and c.isupper():  #101 (line in Coconut source)
                camel_case_parts.append("")  #102 (line in Coconut source)
            camel_case_parts[-1] += c  #103 (line in Coconut source)
            prev_is_lower = c.islower()  #104 (line in Coconut source)

        mod_name = " ".join(camel_case_parts)  #106 (line in Coconut source)
        while "  " in mod_name:  #107 (line in Coconut source)
            mod_name = mod_name.replace("  ", " ")  #108 (line in Coconut source)

        mod_name = mod_name.strip().lower()  #110 (line in Coconut source)

        if mod_name in NO_COMPONENT_SPLIT_MODS:  #112 (line in Coconut source)
            if not silent:  #113 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as no component splitting; redoing without component splitting.".format(_coconut_format_0=(mod_name)))  #114 (line in Coconut source)
            try:  #115 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #115 (line in Coconut source)
            except _coconut.NameError:  #115 (line in Coconut source)
                _coconut_tre_check_0 = False  #115 (line in Coconut source)
            if _coconut_tre_check_0:  #115 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #115 (line in Coconut source)
                continue  #115 (line in Coconut source)
            else:  #115 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #115 (line in Coconut source)


        if mod_name in USE_ALL_COMPONENTS_MODS and not use_all_components:  #117 (line in Coconut source)
            if not silent:  #118 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as use all components; redoing with all components.".format(_coconut_format_0=(mod_name)))  #119 (line in Coconut source)
            try:  #120 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #120 (line in Coconut source)
            except _coconut.NameError:  #120 (line in Coconut source)
                _coconut_tre_check_0 = False  #120 (line in Coconut source)
            if _coconut_tre_check_0:  #120 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components,) = _coconut_mock_0(jar_name, use_all_components=True)  #120 (line in Coconut source)
                continue  #120 (line in Coconut source)
            else:  #120 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, use_all_components=True)  #120 (line in Coconut source)


        if not silent:  #122 (line in Coconut source)
            print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #123 (line in Coconut source)
        return mod_name  #126 (line in Coconut source)
    return None  #127 (line in Coconut source)

_coconut_recursive_func_0 = get_mod_name  #127 (line in Coconut source)

def get_curseforge_name(mod_name, jar_name, google=False):  #127 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #128 (line in Coconut source)
        return None  #129 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #130 (line in Coconut source)
    if not google:  #138 (line in Coconut source)
        raise KeyError("No Curseforge name for mod {_coconut_format_0!r}; expecting Claude to search for it and add it to curseforge_names.json (automated search query would have been {_coconut_format_1!r}).".format(_coconut_format_0=(mod_name), _coconut_format_1=('site:curseforge.com ' + query)))  #139 (line in Coconut source)
    try:  #140 (line in Coconut source)
        while True:  #141 (line in Coconut source)
            search_json = google_api.google(query)  #142 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #143 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #144 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #145 (line in Coconut source)
                break  #146 (line in Coconut source)
            if "items" in search_json:  #147 (line in Coconut source)
                break  #148 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #149 (line in Coconut source)
            if "spelling" in search_json:  #150 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #151 (line in Coconut source)
                continue  #152 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #153 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #154 (line in Coconut source)
            break  #155 (line in Coconut source)
        items = search_json["items"]  #156 (line in Coconut source)
        curseforge_name = None  #157 (line in Coconut source)
        for result in items:  #158 (line in Coconut source)
            mod_page = result["title"]  #159 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #160 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #161 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #162 (line in Coconut source)
                    break  #163 (line in Coconut source)
            if curseforge_name is not None:  #164 (line in Coconut source)
                break  #165 (line in Coconut source)
            else:  #166 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #167 (line in Coconut source)
        if curseforge_name is None:  #168 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #169 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #170 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #171 (line in Coconut source)
        else:  #172 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #173 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #174 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #175 (line in Coconut source)
        if mod is None:  #176 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #177 (line in Coconut source)
        else:  #178 (line in Coconut source)
            return mod["name"]  #179 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #180 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #181 (line in Coconut source)
        pprint(search_json)  #182 (line in Coconut source)
        raise  #183 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #186 (line in Coconut source)
    old_curseforge_name = None  #187 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #188 (line in Coconut source)
        old_curseforge_name = curseforge_name  #189 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #190 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #191 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #192 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #193 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #194 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #195 (line in Coconut source)
    return curseforge_name  #196 (line in Coconut source)



@_coconut_tco  #199 (line in Coconut source)
def load_curseforge_names():  #199 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #200 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #201 (line in Coconut source)
            curseforge_names = COMMENT_JSON.load(ids_fobj)  #202 (line in Coconut source)
            if FIX_MOD_NAMES:  #203 (line in Coconut source)
                curseforge_names = _coconut.dict(((get_mod_name(mod_name)), (curseforge_name)) for mod_name, curseforge_name in curseforge_names.items())  #204 (line in Coconut source)
            return curseforge_names  #205 (line in Coconut source)
    else:  #206 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #207 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #210 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #211 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #212 (line in Coconut source)



@_coconut_tco  #215 (line in Coconut source)
def load_curseforge_ids_cache():  #215 (line in Coconut source)
    """Load the cached curseforge_name -> curseforge_id mappings."""  #216 (line in Coconut source)
    if os.path.exists(CURSEFORGE_IDS_CACHE_FILE):  #217 (line in Coconut source)
        with open(CURSEFORGE_IDS_CACHE_FILE, "r") as cache_fobj:  #218 (line in Coconut source)
            return json.load(cache_fobj)  #219 (line in Coconut source)
    else:  #220 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #221 (line in Coconut source)



def save_curseforge_ids_cache(curseforge_ids_cache):  #224 (line in Coconut source)
    """Save the curseforge_name -> curseforge_id cache."""  #225 (line in Coconut source)
    with open(CURSEFORGE_IDS_CACHE_FILE, "w") as cache_fobj:  #226 (line in Coconut source)
        json.dump(curseforge_ids_cache, cache_fobj, indent=4)  #227 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names, google=False):  #230 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #231 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #232 (line in Coconut source)
    try:  #233 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #234 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #235 (line in Coconut source)
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name], google=google)  #236 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #239 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #240 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #241 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #243 (line in Coconut source)
    finally:  #244 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #245 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #248 (line in Coconut source)
    nulled_mods = []  #249 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #250 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #251 (line in Coconut source)
        if curseforge_name is None:  #252 (line in Coconut source)
            nulled_mods.append(mod_name)  #253 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #254 (line in Coconut source)
        else:  #255 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #256 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #257 (line in Coconut source)



def get_jar_names(mods_dir):  #260 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #261 (line in Coconut source)
        if fname.endswith(".jar"):  #262 (line in Coconut source)
            yield fname  #263 (line in Coconut source)



def get_mod_names_to_all_jar_names(mods_dir, **kwargs):  #266 (line in Coconut source)
    mod_names_to_all_jar_names = defaultdict(list)  #267 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #268 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #269 (line in Coconut source)
        mod_names_to_all_jar_names[mod_name] += [jar_name,]  #270 (line in Coconut source)
    return mod_names_to_all_jar_names  #271 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, **kwargs):  #274 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #275 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #276 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #277 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #278 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #279 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #280 (line in Coconut source)
    return mod_names_to_jar_names  #281 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #284 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #285 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #286 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #287 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #288 (line in Coconut source)
        if cmd_result.stderr:  #289 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #290 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #291 (line in Coconut source)
        else:  #292 (line in Coconut source)
            break  #293 (line in Coconut source)
    else:  #294 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #295 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #296 (line in Coconut source)
    if not api_result:  #297 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #298 (line in Coconut source)
        return []  #299 (line in Coconut source)
    try:  #300 (line in Coconut source)
        return json.loads(api_result)  #301 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #302 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #303 (line in Coconut source)
        print(api_result)  #304 (line in Coconut source)
        raise  #305 (line in Coconut source)



def has_bad_modloader(name):  #308 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS)):  #309 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #310 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS:  #311 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #312 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #313 (line in Coconut source)
    return False  #314 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #316 (line in Coconut source)
    found_mod = None  #317 (line in Coconut source)
    valid_modloader_results = []  #318 (line in Coconut source)
    for mod in results:  #319 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #320 (line in Coconut source)
        if mod["name"] == curseforge_name:  #321 (line in Coconut source)
            if not valid_modloader:  #322 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #323 (line in Coconut source)
            found_mod = mod  #324 (line in Coconut source)
            break  #325 (line in Coconut source)
        if valid_modloader:  #326 (line in Coconut source)
            valid_modloader_results.append(mod)  #327 (line in Coconut source)
    if found_mod is None:  #328 (line in Coconut source)
        for mod in valid_modloader_results:  #329 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #330 (line in Coconut source)
                found_mod = mod  #331 (line in Coconut source)
                break  #332 (line in Coconut source)
    if found_mod is None:  #333 (line in Coconut source)
        for mod in valid_modloader_results:  #334 (line in Coconut source)
            if curseforge_name in mod["name"]:  #335 (line in Coconut source)
                found_mod = mod  #336 (line in Coconut source)
                break  #337 (line in Coconut source)
    if found_mod is None:  #338 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #339 (line in Coconut source)
        for mod in valid_modloader_results:  #340 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #341 (line in Coconut source)
                found_mod = mod  #342 (line in Coconut source)
                break  #343 (line in Coconut source)
    if found_mod is None:  #344 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #345 (line in Coconut source)
        if core_curseforge_name:  #346 (line in Coconut source)
            for mod in valid_modloader_results:  #347 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #348 (line in Coconut source)
                    found_mod = mod  #349 (line in Coconut source)
                    break  #350 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #351 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #352 (line in Coconut source)
    return found_mod  #353 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #356 (line in Coconut source)
    if verbose:  #357 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #358 (line in Coconut source)
    else:  #359 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #360 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #363 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #366 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #367 (line in Coconut source)

    seen_queries = set()  #369 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #370 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #371 (line in Coconut source)
        if query in seen_queries:  #376 (line in Coconut source)
            continue  #377 (line in Coconut source)
        seen_queries.add(query)  #378 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #380 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #381 (line in Coconut source)
        if mod is not None:  #382 (line in Coconut source)
            return mod  #383 (line in Coconut source)
        if PRINT_DEBUG:  #384 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #385 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #387 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #388 (line in Coconut source)
        if mod is not None:  #389 (line in Coconut source)
            return mod  #390 (line in Coconut source)
        if PRINT_DEBUG:  #391 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #392 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #394 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #395 (line in Coconut source)
        if mod is not None:  #396 (line in Coconut source)
            return mod  #397 (line in Coconut source)
        if PRINT_DEBUG:  #398 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #399 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #401 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #402 (line in Coconut source)
        if mod is not None:  #403 (line in Coconut source)
            return mod  #404 (line in Coconut source)
        if PRINT_DEBUG:  #405 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #406 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #408 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #409 (line in Coconut source)
        if mod is not None:  #410 (line in Coconut source)
            return mod  #411 (line in Coconut source)
        if PRINT_DEBUG:  #412 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #413 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #415 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #416 (line in Coconut source)
        if mod is not None:  #417 (line in Coconut source)
            return mod  #418 (line in Coconut source)
        if PRINT_DEBUG:  #419 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #420 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #422 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #425 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #426 (line in Coconut source)
    if mod is not None:  #427 (line in Coconut source)
        return mod["id"]  #428 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #431 (line in Coconut source)
    curseforge_ids_cache = load_curseforge_ids_cache()  #432 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #433 (line in Coconut source)
    missing_mods = []  #434 (line in Coconut source)
    try:  #435 (line in Coconut source)
        for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #436 (line in Coconut source)
# Check cache first
            if curseforge_name in curseforge_ids_cache:  #438 (line in Coconut source)
                curseforge_id = curseforge_ids_cache[curseforge_name]  #439 (line in Coconut source)
                print("\tUsing cached CurseForge ID for {_coconut_format_0!r}.".format(_coconut_format_0=(curseforge_name)))  #440 (line in Coconut source)
            else:  #441 (line in Coconut source)
                curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #442 (line in Coconut source)
                if curseforge_id is not None:  #443 (line in Coconut source)
                    curseforge_ids_cache[curseforge_name] = curseforge_id  #444 (line in Coconut source)

            if curseforge_id is None:  #446 (line in Coconut source)
                missing_mods.append(mod_name)  #447 (line in Coconut source)
            else:  #448 (line in Coconut source)
                mod_names_to_curseforge_ids[mod_name] = curseforge_id  #449 (line in Coconut source)
    finally:  #450 (line in Coconut source)
        save_curseforge_ids_cache(curseforge_ids_cache)  #451 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #452 (line in Coconut source)



@_coconut_tco  #455 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #455 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #456 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #459 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #460 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #461 (line in Coconut source)
    if match_results is None:  #462 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #463 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #464 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #465 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #470 (line in Coconut source)
    return parsed_time  #471 (line in Coconut source)



@_coconut_tco  #474 (line in Coconut source)
def timestamp_sort(curseforge_files):  #474 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #474 (line in Coconut source)



@_coconut_tco  #481 (line in Coconut source)
def get_max_version(versions):  #481 (line in Coconut source)
    ver_tuples = []  #482 (line in Coconut source)
    for ver_str in versions:  #483 (line in Coconut source)
        try:  #484 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #485 (line in Coconut source)
        except ValueError:  #486 (line in Coconut source)
            pass  #487 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #488 (line in Coconut source)



@_coconut_tco  #491 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #491 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #491 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #505 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #506 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #509 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #510 (line in Coconut source)
    if url is None:  #511 (line in Coconut source)
        return None  #512 (line in Coconut source)
    else:  #513 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #514 (line in Coconut source)



def correct_modloader(versions, jar_name):  #517 (line in Coconut source)
    versions = [v.lower() for v in versions]  #518 (line in Coconut source)

    if MODLOADER.lower() in versions:  #520 (line in Coconut source)
        return True  #521 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #522 (line in Coconut source)
        return False  #523 (line in Coconut source)

    jar_name = jar_name.lower()  #525 (line in Coconut source)
    if has_bad_modloader(jar_name):  #526 (line in Coconut source)
        return False  #527 (line in Coconut source)

    return True  #529 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #532 (line in Coconut source)
    for file_data in curseforge_files:  #533 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #534 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #535 (line in Coconut source)
            return file_data  #536 (line in Coconut source)
    return None  #537 (line in Coconut source)



@_coconut_tco  #540 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #540 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #541 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #543 (line in Coconut source)
    if old_curseforge_file is None:  #544 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #545 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #546 (line in Coconut source)

    curseforge_files_and_versions = []  #548 (line in Coconut source)
    for file_data in curseforge_files:  #549 (line in Coconut source)
        versions = file_data["gameVersions"]  #550 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #551 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #552 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #557 (line in Coconut source)

    correctly_versioned_files = []  #559 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #560 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #561 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #562 (line in Coconut source)
    if correctly_versioned_files:  #563 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #564 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #565 (line in Coconut source)

    compatibly_versioned_files = []  #567 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #568 (line in Coconut source)
        for raw_ver in versions:  #569 (line in Coconut source)
            try:  #570 (line in Coconut source)
                ver = ver_split(raw_ver)  #571 (line in Coconut source)
            except ValueError:  #572 (line in Coconut source)
                pass  #573 (line in Coconut source)
            else:  #574 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #575 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #576 (line in Coconut source)
    if compatibly_versioned_files:  #577 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #578 (line in Coconut source)

    maybe_compatible_files = []  #580 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #581 (line in Coconut source)
        for ver in versions:  #582 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #583 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #584 (line in Coconut source)
                break  #585 (line in Coconut source)
    if maybe_compatible_files:  #586 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #587 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #588 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #589 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #592 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #593 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #596 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #597 (line in Coconut source)
    missing_mods = []  #598 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #599 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #600 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #601 (line in Coconut source)
        if latest_version is None:  #602 (line in Coconut source)
            missing_mods.append(mod_name)  #603 (line in Coconut source)
        else:  #604 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #605 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #606 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #609 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #610 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #611 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #612 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #613 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #614 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #615 (line in Coconut source)
    return updated_mod_names_to_files  #616 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #619 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #620 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #621 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #622 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #623 (line in Coconut source)
    if os.path.exists(new_jar_path):  #624 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #625 (line in Coconut source)
    else:  #626 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #627 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #628 (line in Coconut source)
        if new_mod_name != mod_name:  #629 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #630 (line in Coconut source)
        result = requests.get(url)  #631 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #632 (line in Coconut source)
            jar_fobj.write(result.content)  #633 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #636 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #637 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #638 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #639 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #640 (line in Coconut source)
        if jar_name in seen_jar_names:  #641 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #642 (line in Coconut source)
        else:  #643 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #644 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #645 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #648 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #649 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #650 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #651 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #652 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #653 (line in Coconut source)



def make_dirs(*dirs):  #656 (line in Coconut source)
    for d in dirs:  #657 (line in Coconut source)
        if not os.path.exists(d):  #658 (line in Coconut source)
            os.mkdir(d)  #659 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None, google=False):  #662 (line in Coconut source)
    if interact is None and not PRINT_DEBUG:  #663 (line in Coconut source)
        interact = False  #664 (line in Coconut source)
    try:  #665 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #666 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names, google=google)  #667 (line in Coconut source)
        if not dry_run:  #668 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #669 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #670 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #671 (line in Coconut source)
            if updated_mod_names_to_files:  #672 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #673 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #674 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #675 (line in Coconut source)
        else:  #676 (line in Coconut source)
            missing_ids_mods = []  #677 (line in Coconut source)
            missing_files_mods = []  #678 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #679 (line in Coconut source)
    except Exception:  #680 (line in Coconut source)
        if interact is not False:  #681 (line in Coconut source)
            traceback.print_exc()  #682 (line in Coconut source)

            from coconut import embed  #684 (line in Coconut source)
            embed()  #685 (line in Coconut source)
        raise  #686 (line in Coconut source)
    if interact:  #687 (line in Coconut source)
        from coconut import embed  #688 (line in Coconut source)
        embed()  #689 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None, google=False):  #692 (line in Coconut source)
    couldnt_update = []  #693 (line in Coconut source)
    for mods_dir in mods_dirs:  #694 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #695 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #696 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact, google=google)  #697 (line in Coconut source)
    for mod_name in couldnt_update:  #698 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #699 (line in Coconut source)



@_coconut_tco  #702 (line in Coconut source)
def parse_args():  #702 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Update mods from CurseForge to their latest versions.")  #703 (line in Coconut source)
    parser.add_argument("--dry-run", action="store_true", help="Only check for missing CurseForge name mappings without downloading updates")  #706 (line in Coconut source)
    parser.add_argument("--google", action="store_true", help="Use Google search to find CurseForge names for unknown mods")  #711 (line in Coconut source)
    return _coconut_tail_call(parser.parse_args)  #716 (line in Coconut source)



def main():  #719 (line in Coconut source)
    args = parse_args()  #720 (line in Coconut source)

    sync_mods.main()  #722 (line in Coconut source)

    update_all(UPDATE_MODS_DIRS, dry_run=args.dry_run, google=args.google)  #724 (line in Coconut source)



if __name__ == "__main__":  #731 (line in Coconut source)
    main()  #732 (line in Coconut source)
