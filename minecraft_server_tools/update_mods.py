#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xcc0d8cfd

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
import sys  #2 (line in Coconut source)
import json  #3 (line in Coconut source)
import subprocess  #4 (line in Coconut source)
import traceback  #5 (line in Coconut source)
import datetime  #6 (line in Coconut source)
import time  #7 (line in Coconut source)
import argparse  #8 (line in Coconut source)
from pprint import pprint  #9 (line in Coconut source)
try:  #10 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #10 (line in Coconut source)
except _coconut.NameError:  #10 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #10 (line in Coconut source)
sys = _coconut_sys  #10 (line in Coconut source)
if sys.version_info >= (3,):  #10 (line in Coconut source)
    from urllib.parse import unquote  #10 (line in Coconut source)
else:  #10 (line in Coconut source)
    from urllib import unquote  #10 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #10 (line in Coconut source)
    sys = _coconut_sys_0  #10 (line in Coconut source)
from collections import defaultdict  #11 (line in Coconut source)

# Fix Windows console encoding for unicode characters
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':  #14 (line in Coconut source)
    sys.stdout.reconfigure(errors='replace')  #15 (line in Coconut source)
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':  #16 (line in Coconut source)
    sys.stderr.reconfigure(errors='replace')  #17 (line in Coconut source)

import requests  #19 (line in Coconut source)

from minecraft_server_tools import sync_mods  #21 (line in Coconut source)
from minecraft_server_tools import google_api  #21 (line in Coconut source)
from minecraft_server_tools.constants import COMMENT_JSON  #22 (line in Coconut source)
from minecraft_server_tools.constants import MC_VERSION  #22 (line in Coconut source)
from minecraft_server_tools.constants import COMPONENT_SEPS  #22 (line in Coconut source)
from minecraft_server_tools.constants import NON_NAME_COMPONENT_REGEX  #22 (line in Coconut source)
from minecraft_server_tools.constants import NAME_REGEXES_TO_SPACE  #22 (line in Coconut source)
from minecraft_server_tools.constants import GOOGLE_QUERY_TEMPLATE  #22 (line in Coconut source)
from minecraft_server_tools.constants import NON_CURSEFORGE_MODS  #22 (line in Coconut source)
from minecraft_server_tools.constants import MODLOADER  #22 (line in Coconut source)
from minecraft_server_tools.constants import WRONG_MODLOADERS  #22 (line in Coconut source)
from minecraft_server_tools.constants import MAYBE_WRONG_MODLOADERS  #22 (line in Coconut source)
from minecraft_server_tools.constants import MOD_PAGE_NAME_SUFFICES  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_NAMES_FILE  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_IDS_CACHE_FILE  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_FILE  #22 (line in Coconut source)
from minecraft_server_tools.constants import TIMESTAMP_FORMAT_REGEX  #22 (line in Coconut source)
from minecraft_server_tools.constants import UPDATED_MODS_DIR_SUFFIX  #22 (line in Coconut source)
from minecraft_server_tools.constants import OLD_MODS_DIR_SUFFIX  #22 (line in Coconut source)
from minecraft_server_tools.constants import PRINT_DEBUG  #22 (line in Coconut source)
from minecraft_server_tools.constants import MAX_DEBUG_RESULTS  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_NAME_ELEMS_TO_STRIP  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_QUERY_TEMPLATES  #22 (line in Coconut source)
from minecraft_server_tools.constants import ALWAYS_USE_LATEST_VERSION_FOR_MODS  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_RETRIES  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_RETRY_DELAY  #22 (line in Coconut source)
from minecraft_server_tools.constants import AVOID_FILES_PUBLISHED_WITHIN  #22 (line in Coconut source)
from minecraft_server_tools.constants import FIX_MOD_NAMES  #22 (line in Coconut source)
from minecraft_server_tools.constants import NO_COMPONENT_SPLIT_MODS  #22 (line in Coconut source)
from minecraft_server_tools.constants import USE_ALL_COMPONENTS_MODS  #22 (line in Coconut source)
from minecraft_server_tools.constants import ver_join  #22 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #22 (line in Coconut source)


UPDATE_MODS_DIRS = [sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR]  #56 (line in Coconut source)

BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #63 (line in Coconut source)


class MissingCurseforgeNameError(KeyError):  #66 (line in Coconut source)
    """Exception raised when a CurseForge name mapping is missing."""  #67 (line in Coconut source)
    def __init__(self, mod_name, query):  #68 (line in Coconut source)
        self.mod_name = mod_name  #69 (line in Coconut source)
        self.query = query  #70 (line in Coconut source)
        __class__ = MissingCurseforgeNameError  #71 (line in Coconut source)

        super().__init__("No Curseforge name for mod {_coconut_format_0!r}; expecting Claude to search for it and add it to curseforge_names.json (suggested search query: {_coconut_format_1!r}).".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #71 (line in Coconut source)



_coconut_call_set_names(MissingCurseforgeNameError)  #74 (line in Coconut source)
@_coconut_tco  #74 (line in Coconut source)
def get_mod_name(jar_name, silent=None, do_component_splitting=True, use_all_components=False):  #74 (line in Coconut source)
    def _coconut_mock_0(jar_name, silent=_coconut_sentinel, do_component_splitting=_coconut_sentinel, use_all_components=_coconut_sentinel):  #75 (line in Coconut source)
        if silent is _coconut_sentinel: silent = _coconut_recursive_func_0._coconut_tco_func.__defaults__[0]  #75 (line in Coconut source)
        if do_component_splitting is _coconut_sentinel: do_component_splitting = _coconut_recursive_func_0._coconut_tco_func.__defaults__[1]  #75 (line in Coconut source)
        if use_all_components is _coconut_sentinel: use_all_components = _coconut_recursive_func_0._coconut_tco_func.__defaults__[2]  #75 (line in Coconut source)
        return (jar_name, silent, do_component_splitting, use_all_components,)  #75 (line in Coconut source)
    while True:  #75 (line in Coconut source)
        if silent is None:  #75 (line in Coconut source)
            silent = not PRINT_DEBUG  #76 (line in Coconut source)

        base_name = jar_name.removesuffix(".jar")  #78 (line in Coconut source)

        if do_component_splitting:  #80 (line in Coconut source)
            for sep, min_count in COMPONENT_SEPS:  #81 (line in Coconut source)
                components = base_name.split(sep)  #82 (line in Coconut source)
                if len(components) > min_count:  #83 (line in Coconut source)
                    break  #84 (line in Coconut source)
            else:  #85 (line in Coconut source)
                if not silent:  #86 (line in Coconut source)
                    print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #87 (line in Coconut source)
                components = [base_name,]  #88 (line in Coconut source)

            name_cmpnts = []  #90 (line in Coconut source)
            for cmpnt in components:  #91 (line in Coconut source)
                is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #92 (line in Coconut source)
                if is_name_cmpnt:  #93 (line in Coconut source)
                    name_cmpnts.append(cmpnt)  #94 (line in Coconut source)
                elif name_cmpnts and not use_all_components:  #95 (line in Coconut source)
                    break  #96 (line in Coconut source)
            if not name_cmpnts:  #97 (line in Coconut source)
                if not silent:  #98 (line in Coconut source)
                    print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #99 (line in Coconut source)
                name_cmpnts = [components[0],]  #100 (line in Coconut source)
            mod_name = " ".join(name_cmpnts)  #101 (line in Coconut source)
        else:  #102 (line in Coconut source)
            mod_name = base_name  #103 (line in Coconut source)

        for to_space in NAME_REGEXES_TO_SPACE:  #105 (line in Coconut source)
            mod_name = to_space.sub(" ", mod_name)  #106 (line in Coconut source)

        if not mod_name:  #108 (line in Coconut source)
            if not silent:  #109 (line in Coconut source)
                print("Got empty mod name for jar {_coconut_format_0!r}; falling back to no component splitting.".format(_coconut_format_0=(jar_name)))  #110 (line in Coconut source)
            try:  #111 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #111 (line in Coconut source)
            except _coconut.NameError:  #111 (line in Coconut source)
                _coconut_tre_check_0 = False  #111 (line in Coconut source)
            if _coconut_tre_check_0:  #111 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #111 (line in Coconut source)
                continue  #111 (line in Coconut source)
            else:  #111 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #111 (line in Coconut source)


        camel_case_parts = [mod_name[0],]  #113 (line in Coconut source)
        prev_is_lower = mod_name[0].islower()  #114 (line in Coconut source)
        for c in mod_name[1:]:  #115 (line in Coconut source)
            if prev_is_lower and c.isupper():  #116 (line in Coconut source)
                camel_case_parts.append("")  #117 (line in Coconut source)
            camel_case_parts[-1] += c  #118 (line in Coconut source)
            prev_is_lower = c.islower()  #119 (line in Coconut source)

        mod_name = " ".join(camel_case_parts)  #121 (line in Coconut source)
        while "  " in mod_name:  #122 (line in Coconut source)
            mod_name = mod_name.replace("  ", " ")  #123 (line in Coconut source)

        mod_name = mod_name.strip().lower()  #125 (line in Coconut source)

        if mod_name in NO_COMPONENT_SPLIT_MODS:  #127 (line in Coconut source)
            if not silent:  #128 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as no component splitting; redoing without component splitting.".format(_coconut_format_0=(mod_name)))  #129 (line in Coconut source)
            try:  #130 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #130 (line in Coconut source)
            except _coconut.NameError:  #130 (line in Coconut source)
                _coconut_tre_check_0 = False  #130 (line in Coconut source)
            if _coconut_tre_check_0:  #130 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #130 (line in Coconut source)
                continue  #130 (line in Coconut source)
            else:  #130 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #130 (line in Coconut source)


        if mod_name in USE_ALL_COMPONENTS_MODS and not use_all_components:  #132 (line in Coconut source)
            if not silent:  #133 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as use all components; redoing with all components.".format(_coconut_format_0=(mod_name)))  #134 (line in Coconut source)
            try:  #135 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #135 (line in Coconut source)
            except _coconut.NameError:  #135 (line in Coconut source)
                _coconut_tre_check_0 = False  #135 (line in Coconut source)
            if _coconut_tre_check_0:  #135 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components,) = _coconut_mock_0(jar_name, use_all_components=True)  #135 (line in Coconut source)
                continue  #135 (line in Coconut source)
            else:  #135 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, use_all_components=True)  #135 (line in Coconut source)


        if not silent:  #137 (line in Coconut source)
            print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #138 (line in Coconut source)
        return mod_name  #141 (line in Coconut source)
    return None  #142 (line in Coconut source)

_coconut_recursive_func_0 = get_mod_name  #142 (line in Coconut source)

def get_curseforge_name(mod_name, jar_name, google=False):  #142 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #143 (line in Coconut source)
        return None  #144 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #145 (line in Coconut source)
    if not google:  #153 (line in Coconut source)
        raise MissingCurseforgeNameError(mod_name, 'site:curseforge.com ' + query)  #154 (line in Coconut source)
    try:  #155 (line in Coconut source)
        while True:  #156 (line in Coconut source)
            search_json = google_api.google(query)  #157 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #158 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #159 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #160 (line in Coconut source)
                break  #161 (line in Coconut source)
            if "items" in search_json:  #162 (line in Coconut source)
                break  #163 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #164 (line in Coconut source)
            if "spelling" in search_json:  #165 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #166 (line in Coconut source)
                continue  #167 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #168 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #169 (line in Coconut source)
            break  #170 (line in Coconut source)
        items = search_json["items"]  #171 (line in Coconut source)
        curseforge_name = None  #172 (line in Coconut source)
        for result in items:  #173 (line in Coconut source)
            mod_page = result["title"]  #174 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #175 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #176 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #177 (line in Coconut source)
                    break  #178 (line in Coconut source)
            if curseforge_name is not None:  #179 (line in Coconut source)
                break  #180 (line in Coconut source)
            else:  #181 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #182 (line in Coconut source)
        if curseforge_name is None:  #183 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #184 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #185 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #186 (line in Coconut source)
        else:  #187 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #188 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #189 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #190 (line in Coconut source)
        if mod is None:  #191 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #192 (line in Coconut source)
        else:  #193 (line in Coconut source)
            return mod["name"]  #194 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #195 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #196 (line in Coconut source)
        pprint(search_json)  #197 (line in Coconut source)
        raise  #198 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #201 (line in Coconut source)
    old_curseforge_name = None  #202 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #203 (line in Coconut source)
        old_curseforge_name = curseforge_name  #204 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #205 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #206 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #207 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #208 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #209 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #210 (line in Coconut source)
    return curseforge_name  #211 (line in Coconut source)



@_coconut_tco  #214 (line in Coconut source)
def load_curseforge_names():  #214 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #215 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #216 (line in Coconut source)
            curseforge_names = COMMENT_JSON.load(ids_fobj)  #217 (line in Coconut source)
            if FIX_MOD_NAMES:  #218 (line in Coconut source)
                curseforge_names = _coconut.dict(((get_mod_name(mod_name)), (curseforge_name)) for mod_name, curseforge_name in curseforge_names.items())  #219 (line in Coconut source)
            return curseforge_names  #220 (line in Coconut source)
    else:  #221 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #222 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #225 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #226 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #227 (line in Coconut source)



@_coconut_tco  #230 (line in Coconut source)
def load_curseforge_ids_cache():  #230 (line in Coconut source)
    """Load the cached curseforge_name -> curseforge_id mappings."""  #231 (line in Coconut source)
    if os.path.exists(CURSEFORGE_IDS_CACHE_FILE):  #232 (line in Coconut source)
        with open(CURSEFORGE_IDS_CACHE_FILE, "r") as cache_fobj:  #233 (line in Coconut source)
            return json.load(cache_fobj)  #234 (line in Coconut source)
    else:  #235 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #236 (line in Coconut source)



def save_curseforge_ids_cache(curseforge_ids_cache):  #239 (line in Coconut source)
    """Save the curseforge_name -> curseforge_id cache."""  #240 (line in Coconut source)
    with open(CURSEFORGE_IDS_CACHE_FILE, "w") as cache_fobj:  #241 (line in Coconut source)
        json.dump(curseforge_ids_cache, cache_fobj, indent=4)  #242 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names, google=False):  #245 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #246 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #247 (line in Coconut source)
    missing_curseforge_names = []  # collect all missing names first  #248 (line in Coconut source)
    try:  #249 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #250 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #251 (line in Coconut source)
                try:  #252 (line in Coconut source)
                    curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name], google=google)  #253 (line in Coconut source)
                except MissingCurseforgeNameError as e:  #254 (line in Coconut source)
                    missing_curseforge_names.append((e.mod_name, e.query))  #255 (line in Coconut source)
                    continue  #256 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #259 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #260 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #261 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #263 (line in Coconut source)
    finally:  #264 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #265 (line in Coconut source)

# raise error with all missing names at once
    if missing_curseforge_names:  #268 (line in Coconut source)
        print("\n{_coconut_format_0}".format(_coconut_format_0=('=' * 60)))  #269 (line in Coconut source)
        print("MISSING CURSEFORGE NAME MAPPINGS:")  #270 (line in Coconut source)
        print("{_coconut_format_0}\n".format(_coconut_format_0=('=' * 60)))  #271 (line in Coconut source)
        for mod_name, query in missing_curseforge_names:  #272 (line in Coconut source)
            print("{_coconut_format_0!r}".format(_coconut_format_0=(mod_name)))  #273 (line in Coconut source)
            print("\tSuggested search query: {_coconut_format_0!r}\n".format(_coconut_format_0=(query)))  #274 (line in Coconut source)
        print("{_coconut_format_0}\n".format(_coconut_format_0=('=' * 60)))  #275 (line in Coconut source)
        raise KeyError("Missing {_coconut_format_0} Curseforge name mappings; expecting Claude to search for them and add them to curseforge_names.json.".format(_coconut_format_0=(len(missing_curseforge_names))))  #276 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #279 (line in Coconut source)
    nulled_mods = []  #280 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #281 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #282 (line in Coconut source)
        if curseforge_name is None:  #283 (line in Coconut source)
            nulled_mods.append(mod_name)  #284 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #285 (line in Coconut source)
        else:  #286 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #287 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #288 (line in Coconut source)



def get_jar_names(mods_dir):  #291 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #292 (line in Coconut source)
        if fname.endswith(".jar"):  #293 (line in Coconut source)
            yield fname  #294 (line in Coconut source)



def get_mod_names_to_all_jar_names(mods_dir, **kwargs):  #297 (line in Coconut source)
    mod_names_to_all_jar_names = defaultdict(list)  #298 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #299 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #300 (line in Coconut source)
        mod_names_to_all_jar_names[mod_name] += [jar_name,]  #301 (line in Coconut source)
    return mod_names_to_all_jar_names  #302 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, **kwargs):  #305 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #306 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #307 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #308 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #309 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #310 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #311 (line in Coconut source)
    return mod_names_to_jar_names  #312 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #315 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #316 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #317 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #318 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #319 (line in Coconut source)
        if cmd_result.stderr:  #320 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #321 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #322 (line in Coconut source)
        else:  #323 (line in Coconut source)
            break  #324 (line in Coconut source)
    else:  #325 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #326 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #327 (line in Coconut source)
    if not api_result:  #328 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #329 (line in Coconut source)
        return []  #330 (line in Coconut source)
    try:  #331 (line in Coconut source)
        return json.loads(api_result)  #332 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #333 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #334 (line in Coconut source)
        print(api_result)  #335 (line in Coconut source)
        raise  #336 (line in Coconut source)



def has_bad_modloader(name):  #339 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS)):  #340 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #341 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS:  #342 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #343 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #344 (line in Coconut source)
    return False  #345 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #347 (line in Coconut source)
    found_mod = None  #348 (line in Coconut source)
    valid_modloader_results = []  #349 (line in Coconut source)
    for mod in results:  #350 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #351 (line in Coconut source)
        if mod["name"] == curseforge_name:  #352 (line in Coconut source)
            if not valid_modloader:  #353 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #354 (line in Coconut source)
            found_mod = mod  #355 (line in Coconut source)
            break  #356 (line in Coconut source)
        if valid_modloader:  #357 (line in Coconut source)
            valid_modloader_results.append(mod)  #358 (line in Coconut source)
    if found_mod is None:  #359 (line in Coconut source)
        for mod in valid_modloader_results:  #360 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #361 (line in Coconut source)
                found_mod = mod  #362 (line in Coconut source)
                break  #363 (line in Coconut source)
    if found_mod is None:  #364 (line in Coconut source)
        for mod in valid_modloader_results:  #365 (line in Coconut source)
            if curseforge_name in mod["name"]:  #366 (line in Coconut source)
                found_mod = mod  #367 (line in Coconut source)
                break  #368 (line in Coconut source)
    if found_mod is None:  #369 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #370 (line in Coconut source)
        for mod in valid_modloader_results:  #371 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #372 (line in Coconut source)
                found_mod = mod  #373 (line in Coconut source)
                break  #374 (line in Coconut source)
    if found_mod is None:  #375 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #376 (line in Coconut source)
        if core_curseforge_name:  #377 (line in Coconut source)
            for mod in valid_modloader_results:  #378 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #379 (line in Coconut source)
                    found_mod = mod  #380 (line in Coconut source)
                    break  #381 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #382 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #383 (line in Coconut source)
    return found_mod  #384 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #387 (line in Coconut source)
    if verbose:  #388 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #389 (line in Coconut source)
    else:  #390 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #391 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #394 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #397 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #398 (line in Coconut source)

    seen_queries = set()  #400 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #401 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #402 (line in Coconut source)
        if query in seen_queries:  #407 (line in Coconut source)
            continue  #408 (line in Coconut source)
        seen_queries.add(query)  #409 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #411 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #412 (line in Coconut source)
        if mod is not None:  #413 (line in Coconut source)
            return mod  #414 (line in Coconut source)
        if PRINT_DEBUG:  #415 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #416 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #418 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #419 (line in Coconut source)
        if mod is not None:  #420 (line in Coconut source)
            return mod  #421 (line in Coconut source)
        if PRINT_DEBUG:  #422 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #423 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #425 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #426 (line in Coconut source)
        if mod is not None:  #427 (line in Coconut source)
            return mod  #428 (line in Coconut source)
        if PRINT_DEBUG:  #429 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #430 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #432 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #433 (line in Coconut source)
        if mod is not None:  #434 (line in Coconut source)
            return mod  #435 (line in Coconut source)
        if PRINT_DEBUG:  #436 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #437 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #439 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #440 (line in Coconut source)
        if mod is not None:  #441 (line in Coconut source)
            return mod  #442 (line in Coconut source)
        if PRINT_DEBUG:  #443 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #444 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #446 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #447 (line in Coconut source)
        if mod is not None:  #448 (line in Coconut source)
            return mod  #449 (line in Coconut source)
        if PRINT_DEBUG:  #450 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #451 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #453 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #456 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #457 (line in Coconut source)
    if mod is not None:  #458 (line in Coconut source)
        return mod["id"]  #459 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #462 (line in Coconut source)
    curseforge_ids_cache = load_curseforge_ids_cache()  #463 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #464 (line in Coconut source)
    missing_mods = []  #465 (line in Coconut source)
    try:  #466 (line in Coconut source)
        for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #467 (line in Coconut source)
# Check cache first
            if curseforge_name in curseforge_ids_cache:  #469 (line in Coconut source)
                curseforge_id = curseforge_ids_cache[curseforge_name]  #470 (line in Coconut source)
                print("\tUsing cached CurseForge ID for {_coconut_format_0!r}.".format(_coconut_format_0=(curseforge_name)))  #471 (line in Coconut source)
            else:  #472 (line in Coconut source)
                curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #473 (line in Coconut source)
                if curseforge_id is not None:  #474 (line in Coconut source)
                    curseforge_ids_cache[curseforge_name] = curseforge_id  #475 (line in Coconut source)

            if curseforge_id is None:  #477 (line in Coconut source)
                missing_mods.append(mod_name)  #478 (line in Coconut source)
            else:  #479 (line in Coconut source)
                mod_names_to_curseforge_ids[mod_name] = curseforge_id  #480 (line in Coconut source)
    finally:  #481 (line in Coconut source)
        save_curseforge_ids_cache(curseforge_ids_cache)  #482 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #483 (line in Coconut source)



@_coconut_tco  #486 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #486 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #487 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #490 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #491 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #492 (line in Coconut source)
    if match_results is None:  #493 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #494 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #495 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #496 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #501 (line in Coconut source)
    return parsed_time  #502 (line in Coconut source)



@_coconut_tco  #505 (line in Coconut source)
def timestamp_sort(curseforge_files):  #505 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #505 (line in Coconut source)



@_coconut_tco  #512 (line in Coconut source)
def get_max_version(versions):  #512 (line in Coconut source)
    ver_tuples = []  #513 (line in Coconut source)
    for ver_str in versions:  #514 (line in Coconut source)
        try:  #515 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #516 (line in Coconut source)
        except ValueError:  #517 (line in Coconut source)
            pass  #518 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #519 (line in Coconut source)



@_coconut_tco  #522 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #522 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #522 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #536 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #537 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #540 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #541 (line in Coconut source)
    if url is None:  #542 (line in Coconut source)
        return None  #543 (line in Coconut source)
    else:  #544 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #545 (line in Coconut source)



def correct_modloader(versions, jar_name):  #548 (line in Coconut source)
    versions = [v.lower() for v in versions]  #549 (line in Coconut source)

    if MODLOADER.lower() in versions:  #551 (line in Coconut source)
        return True  #552 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #553 (line in Coconut source)
        return False  #554 (line in Coconut source)

    jar_name = jar_name.lower()  #556 (line in Coconut source)
    if has_bad_modloader(jar_name):  #557 (line in Coconut source)
        return False  #558 (line in Coconut source)

    return True  #560 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #563 (line in Coconut source)
    for file_data in curseforge_files:  #564 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #565 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #566 (line in Coconut source)
            return file_data  #567 (line in Coconut source)
    return None  #568 (line in Coconut source)



@_coconut_tco  #571 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #571 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #572 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #574 (line in Coconut source)
    if old_curseforge_file is None:  #575 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #576 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #577 (line in Coconut source)

    curseforge_files_and_versions = []  #579 (line in Coconut source)
    for file_data in curseforge_files:  #580 (line in Coconut source)
        versions = file_data["gameVersions"]  #581 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #582 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #583 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #588 (line in Coconut source)

    correctly_versioned_files = []  #590 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #591 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #592 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #593 (line in Coconut source)
    if correctly_versioned_files:  #594 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #595 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #596 (line in Coconut source)

    compatibly_versioned_files = []  #598 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #599 (line in Coconut source)
        for raw_ver in versions:  #600 (line in Coconut source)
            try:  #601 (line in Coconut source)
                ver = ver_split(raw_ver)  #602 (line in Coconut source)
            except ValueError:  #603 (line in Coconut source)
                pass  #604 (line in Coconut source)
            else:  #605 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #606 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #607 (line in Coconut source)
    if compatibly_versioned_files:  #608 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #609 (line in Coconut source)

    maybe_compatible_files = []  #611 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #612 (line in Coconut source)
        for ver in versions:  #613 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #614 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #615 (line in Coconut source)
                break  #616 (line in Coconut source)
    if maybe_compatible_files:  #617 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #618 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #619 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #620 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #623 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #624 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #627 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #628 (line in Coconut source)
    missing_mods = []  #629 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #630 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #631 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #632 (line in Coconut source)
        if latest_version is None:  #633 (line in Coconut source)
            missing_mods.append(mod_name)  #634 (line in Coconut source)
        else:  #635 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #636 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #637 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #640 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #641 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #642 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #643 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #644 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #645 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #646 (line in Coconut source)
    return updated_mod_names_to_files  #647 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #650 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #651 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #652 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #653 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #654 (line in Coconut source)
    if os.path.exists(new_jar_path):  #655 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #656 (line in Coconut source)
    else:  #657 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #658 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #659 (line in Coconut source)
        if new_mod_name != mod_name:  #660 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #661 (line in Coconut source)
        result = requests.get(url)  #662 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #663 (line in Coconut source)
            jar_fobj.write(result.content)  #664 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #667 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #668 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #669 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #670 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #671 (line in Coconut source)
        if jar_name in seen_jar_names:  #672 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #673 (line in Coconut source)
        else:  #674 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #675 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #676 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #679 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #680 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #681 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #682 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #683 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #684 (line in Coconut source)



def make_dirs(*dirs):  #687 (line in Coconut source)
    for d in dirs:  #688 (line in Coconut source)
        if not os.path.exists(d):  #689 (line in Coconut source)
            os.mkdir(d)  #690 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None, google=False):  #693 (line in Coconut source)
    if interact is None and not PRINT_DEBUG:  #694 (line in Coconut source)
        interact = False  #695 (line in Coconut source)
    try:  #696 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #697 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names, google=google)  #698 (line in Coconut source)
        if not dry_run:  #699 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #700 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #701 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #702 (line in Coconut source)
            if updated_mod_names_to_files:  #703 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #704 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #705 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #706 (line in Coconut source)
        else:  #707 (line in Coconut source)
            missing_ids_mods = []  #708 (line in Coconut source)
            missing_files_mods = []  #709 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #710 (line in Coconut source)
    except Exception:  #711 (line in Coconut source)
        if interact is not False:  #712 (line in Coconut source)
            traceback.print_exc()  #713 (line in Coconut source)

            from coconut import embed  #715 (line in Coconut source)
            embed()  #716 (line in Coconut source)
        raise  #717 (line in Coconut source)
    if interact:  #718 (line in Coconut source)
        from coconut import embed  #719 (line in Coconut source)
        embed()  #720 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None, google=False):  #723 (line in Coconut source)
    couldnt_update = []  #724 (line in Coconut source)
    for mods_dir in mods_dirs:  #725 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #726 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #727 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact, google=google)  #728 (line in Coconut source)
    for mod_name in couldnt_update:  #729 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #730 (line in Coconut source)



@_coconut_tco  #733 (line in Coconut source)
def parse_args():  #733 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Update mods from CurseForge to their latest versions.")  #734 (line in Coconut source)
    parser.add_argument("--dry-run", action="store_true", help="Only check for missing CurseForge name mappings without downloading updates")  #737 (line in Coconut source)
    parser.add_argument("--google", action="store_true", help="Use Google search to find CurseForge names for unknown mods")  #742 (line in Coconut source)
    return _coconut_tail_call(parser.parse_args)  #747 (line in Coconut source)



def main():  #750 (line in Coconut source)
    args = parse_args()  #751 (line in Coconut source)

    sync_mods.main()  #753 (line in Coconut source)

    update_all(UPDATE_MODS_DIRS, dry_run=args.dry_run, google=args.google)  #755 (line in Coconut source)



if __name__ == "__main__":  #762 (line in Coconut source)
    main()  #763 (line in Coconut source)
