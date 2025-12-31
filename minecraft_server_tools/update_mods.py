#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2d538d19

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
from minecraft_server_tools.constants import ver_join  #15 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #15 (line in Coconut source)


UPDATE_MODS_DIRS = [sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR]  #48 (line in Coconut source)

BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #55 (line in Coconut source)


@_coconut_tco  #58 (line in Coconut source)
def get_mod_name(jar_name, silent=None, do_component_splitting=True):  #58 (line in Coconut source)
    def _coconut_mock_0(jar_name, silent=_coconut_sentinel, do_component_splitting=_coconut_sentinel):  #59 (line in Coconut source)
        if silent is _coconut_sentinel: silent = _coconut_recursive_func_0._coconut_tco_func.__defaults__[0]  #59 (line in Coconut source)
        if do_component_splitting is _coconut_sentinel: do_component_splitting = _coconut_recursive_func_0._coconut_tco_func.__defaults__[1]  #59 (line in Coconut source)
        return (jar_name, silent, do_component_splitting,)  #59 (line in Coconut source)
    while True:  #59 (line in Coconut source)
        if silent is None:  #59 (line in Coconut source)
            silent = not PRINT_DEBUG  #60 (line in Coconut source)

        base_name = jar_name.removesuffix(".jar")  #62 (line in Coconut source)

        if do_component_splitting:  #64 (line in Coconut source)
            for sep, min_count in COMPONENT_SEPS:  #65 (line in Coconut source)
                components = base_name.split(sep)  #66 (line in Coconut source)
                if len(components) > min_count:  #67 (line in Coconut source)
                    break  #68 (line in Coconut source)
            else:  #69 (line in Coconut source)
                if not silent:  #70 (line in Coconut source)
                    print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #71 (line in Coconut source)
                components = [base_name,]  #72 (line in Coconut source)

            name_cmpnts = []  #74 (line in Coconut source)
            for cmpnt in components:  #75 (line in Coconut source)
                is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #76 (line in Coconut source)
                if is_name_cmpnt:  #77 (line in Coconut source)
                    name_cmpnts.append(cmpnt)  #78 (line in Coconut source)
                elif name_cmpnts:  #79 (line in Coconut source)
                    break  #80 (line in Coconut source)
            if not name_cmpnts:  #81 (line in Coconut source)
                if not silent:  #82 (line in Coconut source)
                    print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #83 (line in Coconut source)
                name_cmpnts = [components[0],]  #84 (line in Coconut source)
            mod_name = " ".join(name_cmpnts)  #85 (line in Coconut source)
        else:  #86 (line in Coconut source)
            mod_name = base_name  #87 (line in Coconut source)

        for to_space in NAME_REGEXES_TO_SPACE:  #89 (line in Coconut source)
            mod_name = to_space.sub(" ", mod_name)  #90 (line in Coconut source)

        if not mod_name:  #92 (line in Coconut source)
            if not silent:  #93 (line in Coconut source)
                print("Got empty mod name for jar {_coconut_format_0!r}; falling back to no component splitting.".format(_coconut_format_0=(jar_name)))  #94 (line in Coconut source)
            try:  #95 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #95 (line in Coconut source)
            except _coconut.NameError:  #95 (line in Coconut source)
                _coconut_tre_check_0 = False  #95 (line in Coconut source)
            if _coconut_tre_check_0:  #95 (line in Coconut source)
                (jar_name, silent, do_component_splitting,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #95 (line in Coconut source)
                continue  #95 (line in Coconut source)
            else:  #95 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #95 (line in Coconut source)


        camel_case_parts = [mod_name[0],]  #97 (line in Coconut source)
        prev_is_lower = mod_name[0].islower()  #98 (line in Coconut source)
        for c in mod_name[1:]:  #99 (line in Coconut source)
            if prev_is_lower and c.isupper():  #100 (line in Coconut source)
                camel_case_parts.append("")  #101 (line in Coconut source)
            camel_case_parts[-1] += c  #102 (line in Coconut source)
            prev_is_lower = c.islower()  #103 (line in Coconut source)

        mod_name = " ".join(camel_case_parts)  #105 (line in Coconut source)
        while "  " in mod_name:  #106 (line in Coconut source)
            mod_name = mod_name.replace("  ", " ")  #107 (line in Coconut source)

        mod_name = mod_name.strip().lower()  #109 (line in Coconut source)

        if mod_name in NO_COMPONENT_SPLIT_MODS:  #111 (line in Coconut source)
            if not silent:  #112 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as no component splitting; redoing without component splitting.".format(_coconut_format_0=(mod_name)))  #113 (line in Coconut source)
            try:  #114 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #114 (line in Coconut source)
            except _coconut.NameError:  #114 (line in Coconut source)
                _coconut_tre_check_0 = False  #114 (line in Coconut source)
            if _coconut_tre_check_0:  #114 (line in Coconut source)
                (jar_name, silent, do_component_splitting,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #114 (line in Coconut source)
                continue  #114 (line in Coconut source)
            else:  #114 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #114 (line in Coconut source)


        if not silent:  #116 (line in Coconut source)
            print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #117 (line in Coconut source)
        return mod_name  #120 (line in Coconut source)
    return None  #121 (line in Coconut source)

_coconut_recursive_func_0 = get_mod_name  #121 (line in Coconut source)

def get_curseforge_name(mod_name, jar_name, google=False):  #121 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #122 (line in Coconut source)
        return None  #123 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #124 (line in Coconut source)
    if not google:  #132 (line in Coconut source)
        raise KeyError("No Curseforge name for mod {_coconut_format_0!r}; expecting Claude to search for it and add it to curseforge_names.json (automated search query would have been {_coconut_format_1!r}).".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #133 (line in Coconut source)
    try:  #134 (line in Coconut source)
        while True:  #135 (line in Coconut source)
            search_json = google_api.google(query)  #136 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #137 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #138 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #139 (line in Coconut source)
                break  #140 (line in Coconut source)
            if "items" in search_json:  #141 (line in Coconut source)
                break  #142 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #143 (line in Coconut source)
            if "spelling" in search_json:  #144 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #145 (line in Coconut source)
                continue  #146 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #147 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #148 (line in Coconut source)
            break  #149 (line in Coconut source)
        items = search_json["items"]  #150 (line in Coconut source)
        curseforge_name = None  #151 (line in Coconut source)
        for result in items:  #152 (line in Coconut source)
            mod_page = result["title"]  #153 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #154 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #155 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #156 (line in Coconut source)
                    break  #157 (line in Coconut source)
            if curseforge_name is not None:  #158 (line in Coconut source)
                break  #159 (line in Coconut source)
            else:  #160 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #161 (line in Coconut source)
        if curseforge_name is None:  #162 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #163 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #164 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #165 (line in Coconut source)
        else:  #166 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #167 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #168 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #169 (line in Coconut source)
        if mod is None:  #170 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #171 (line in Coconut source)
        else:  #172 (line in Coconut source)
            return mod["name"]  #173 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #174 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #175 (line in Coconut source)
        pprint(search_json)  #176 (line in Coconut source)
        raise  #177 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #180 (line in Coconut source)
    old_curseforge_name = None  #181 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #182 (line in Coconut source)
        old_curseforge_name = curseforge_name  #183 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #184 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #185 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #186 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #187 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #188 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #189 (line in Coconut source)
    return curseforge_name  #190 (line in Coconut source)



@_coconut_tco  #193 (line in Coconut source)
def load_curseforge_names():  #193 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #194 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #195 (line in Coconut source)
            curseforge_names = COMMENT_JSON.load(ids_fobj)  #196 (line in Coconut source)
            if FIX_MOD_NAMES:  #197 (line in Coconut source)
                curseforge_names = _coconut.dict(((get_mod_name(mod_name)), (curseforge_name)) for mod_name, curseforge_name in curseforge_names.items())  #198 (line in Coconut source)
            return curseforge_names  #199 (line in Coconut source)
    else:  #200 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #201 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #204 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #205 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #206 (line in Coconut source)



@_coconut_tco  #209 (line in Coconut source)
def load_curseforge_ids_cache():  #209 (line in Coconut source)
    """Load the cached curseforge_name -> curseforge_id mappings."""  #210 (line in Coconut source)
    if os.path.exists(CURSEFORGE_IDS_CACHE_FILE):  #211 (line in Coconut source)
        with open(CURSEFORGE_IDS_CACHE_FILE, "r") as cache_fobj:  #212 (line in Coconut source)
            return json.load(cache_fobj)  #213 (line in Coconut source)
    else:  #214 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #215 (line in Coconut source)



def save_curseforge_ids_cache(curseforge_ids_cache):  #218 (line in Coconut source)
    """Save the curseforge_name -> curseforge_id cache."""  #219 (line in Coconut source)
    with open(CURSEFORGE_IDS_CACHE_FILE, "w") as cache_fobj:  #220 (line in Coconut source)
        json.dump(curseforge_ids_cache, cache_fobj, indent=4)  #221 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names, google=False):  #224 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #225 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #226 (line in Coconut source)
    try:  #227 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #228 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #229 (line in Coconut source)
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name], google=google)  #230 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #233 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #234 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #235 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #237 (line in Coconut source)
    finally:  #238 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #239 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #242 (line in Coconut source)
    nulled_mods = []  #243 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #244 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #245 (line in Coconut source)
        if curseforge_name is None:  #246 (line in Coconut source)
            nulled_mods.append(mod_name)  #247 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #248 (line in Coconut source)
        else:  #249 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #250 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #251 (line in Coconut source)



def get_jar_names(mods_dir):  #254 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #255 (line in Coconut source)
        if fname.endswith(".jar"):  #256 (line in Coconut source)
            yield fname  #257 (line in Coconut source)



def get_mod_names_to_all_jar_names(mods_dir, **kwargs):  #260 (line in Coconut source)
    mod_names_to_all_jar_names = defaultdict(list)  #261 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #262 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #263 (line in Coconut source)
        mod_names_to_all_jar_names[mod_name] += [jar_name,]  #264 (line in Coconut source)
    return mod_names_to_all_jar_names  #265 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, **kwargs):  #268 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #269 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #270 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #271 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #272 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #273 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #274 (line in Coconut source)
    return mod_names_to_jar_names  #275 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #278 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #279 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #280 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #281 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #282 (line in Coconut source)
        if cmd_result.stderr:  #283 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #284 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #285 (line in Coconut source)
        else:  #286 (line in Coconut source)
            break  #287 (line in Coconut source)
    else:  #288 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #289 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #290 (line in Coconut source)
    if not api_result:  #291 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #292 (line in Coconut source)
        return []  #293 (line in Coconut source)
    try:  #294 (line in Coconut source)
        return json.loads(api_result)  #295 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #296 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #297 (line in Coconut source)
        print(api_result)  #298 (line in Coconut source)
        raise  #299 (line in Coconut source)



def has_bad_modloader(name):  #302 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS)):  #303 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #304 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS:  #305 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #306 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #307 (line in Coconut source)
    return False  #308 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #310 (line in Coconut source)
    found_mod = None  #311 (line in Coconut source)
    valid_modloader_results = []  #312 (line in Coconut source)
    for mod in results:  #313 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #314 (line in Coconut source)
        if mod["name"] == curseforge_name:  #315 (line in Coconut source)
            if not valid_modloader:  #316 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #317 (line in Coconut source)
            found_mod = mod  #318 (line in Coconut source)
            break  #319 (line in Coconut source)
        if valid_modloader:  #320 (line in Coconut source)
            valid_modloader_results.append(mod)  #321 (line in Coconut source)
    if found_mod is None:  #322 (line in Coconut source)
        for mod in valid_modloader_results:  #323 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #324 (line in Coconut source)
                found_mod = mod  #325 (line in Coconut source)
                break  #326 (line in Coconut source)
    if found_mod is None:  #327 (line in Coconut source)
        for mod in valid_modloader_results:  #328 (line in Coconut source)
            if curseforge_name in mod["name"]:  #329 (line in Coconut source)
                found_mod = mod  #330 (line in Coconut source)
                break  #331 (line in Coconut source)
    if found_mod is None:  #332 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #333 (line in Coconut source)
        for mod in valid_modloader_results:  #334 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #335 (line in Coconut source)
                found_mod = mod  #336 (line in Coconut source)
                break  #337 (line in Coconut source)
    if found_mod is None:  #338 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #339 (line in Coconut source)
        if core_curseforge_name:  #340 (line in Coconut source)
            for mod in valid_modloader_results:  #341 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #342 (line in Coconut source)
                    found_mod = mod  #343 (line in Coconut source)
                    break  #344 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #345 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #346 (line in Coconut source)
    return found_mod  #347 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #350 (line in Coconut source)
    if verbose:  #351 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #352 (line in Coconut source)
    else:  #353 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #354 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #357 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #360 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #361 (line in Coconut source)

    seen_queries = set()  #363 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #364 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #365 (line in Coconut source)
        if query in seen_queries:  #370 (line in Coconut source)
            continue  #371 (line in Coconut source)
        seen_queries.add(query)  #372 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #374 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #375 (line in Coconut source)
        if mod is not None:  #376 (line in Coconut source)
            return mod  #377 (line in Coconut source)
        if PRINT_DEBUG:  #378 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #379 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #381 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #382 (line in Coconut source)
        if mod is not None:  #383 (line in Coconut source)
            return mod  #384 (line in Coconut source)
        if PRINT_DEBUG:  #385 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #386 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #388 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #389 (line in Coconut source)
        if mod is not None:  #390 (line in Coconut source)
            return mod  #391 (line in Coconut source)
        if PRINT_DEBUG:  #392 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #393 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #395 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #396 (line in Coconut source)
        if mod is not None:  #397 (line in Coconut source)
            return mod  #398 (line in Coconut source)
        if PRINT_DEBUG:  #399 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #400 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #402 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #403 (line in Coconut source)
        if mod is not None:  #404 (line in Coconut source)
            return mod  #405 (line in Coconut source)
        if PRINT_DEBUG:  #406 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #407 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #409 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #410 (line in Coconut source)
        if mod is not None:  #411 (line in Coconut source)
            return mod  #412 (line in Coconut source)
        if PRINT_DEBUG:  #413 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #414 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #416 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #419 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #420 (line in Coconut source)
    if mod is not None:  #421 (line in Coconut source)
        return mod["id"]  #422 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #425 (line in Coconut source)
    curseforge_ids_cache = load_curseforge_ids_cache()  #426 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #427 (line in Coconut source)
    missing_mods = []  #428 (line in Coconut source)
    try:  #429 (line in Coconut source)
        for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #430 (line in Coconut source)
# Check cache first
            if curseforge_name in curseforge_ids_cache:  #432 (line in Coconut source)
                curseforge_id = curseforge_ids_cache[curseforge_name]  #433 (line in Coconut source)
                print("\tUsing cached CurseForge ID for {_coconut_format_0!r}.".format(_coconut_format_0=(curseforge_name)))  #434 (line in Coconut source)
            else:  #435 (line in Coconut source)
                curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #436 (line in Coconut source)
                if curseforge_id is not None:  #437 (line in Coconut source)
                    curseforge_ids_cache[curseforge_name] = curseforge_id  #438 (line in Coconut source)

            if curseforge_id is None:  #440 (line in Coconut source)
                missing_mods.append(mod_name)  #441 (line in Coconut source)
            else:  #442 (line in Coconut source)
                mod_names_to_curseforge_ids[mod_name] = curseforge_id  #443 (line in Coconut source)
    finally:  #444 (line in Coconut source)
        save_curseforge_ids_cache(curseforge_ids_cache)  #445 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #446 (line in Coconut source)



@_coconut_tco  #449 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #449 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #450 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #453 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #454 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #455 (line in Coconut source)
    if match_results is None:  #456 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #457 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #458 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #459 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #464 (line in Coconut source)
    return parsed_time  #465 (line in Coconut source)



@_coconut_tco  #468 (line in Coconut source)
def timestamp_sort(curseforge_files):  #468 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #468 (line in Coconut source)



@_coconut_tco  #475 (line in Coconut source)
def get_max_version(versions):  #475 (line in Coconut source)
    ver_tuples = []  #476 (line in Coconut source)
    for ver_str in versions:  #477 (line in Coconut source)
        try:  #478 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #479 (line in Coconut source)
        except ValueError:  #480 (line in Coconut source)
            pass  #481 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #482 (line in Coconut source)



@_coconut_tco  #485 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #485 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #485 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #499 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #500 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #503 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #504 (line in Coconut source)
    if url is None:  #505 (line in Coconut source)
        return None  #506 (line in Coconut source)
    else:  #507 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #508 (line in Coconut source)



def correct_modloader(versions, jar_name):  #511 (line in Coconut source)
    versions = [v.lower() for v in versions]  #512 (line in Coconut source)

    if MODLOADER.lower() in versions:  #514 (line in Coconut source)
        return True  #515 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #516 (line in Coconut source)
        return False  #517 (line in Coconut source)

    jar_name = jar_name.lower()  #519 (line in Coconut source)
    if has_bad_modloader(jar_name):  #520 (line in Coconut source)
        return False  #521 (line in Coconut source)

    return True  #523 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #526 (line in Coconut source)
    for file_data in curseforge_files:  #527 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #528 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #529 (line in Coconut source)
            return file_data  #530 (line in Coconut source)
    return None  #531 (line in Coconut source)



@_coconut_tco  #534 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #534 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #535 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #537 (line in Coconut source)
    if old_curseforge_file is None:  #538 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #539 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #540 (line in Coconut source)

    curseforge_files_and_versions = []  #542 (line in Coconut source)
    for file_data in curseforge_files:  #543 (line in Coconut source)
        versions = file_data["gameVersions"]  #544 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #545 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #546 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #551 (line in Coconut source)

    correctly_versioned_files = []  #553 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #554 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #555 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #556 (line in Coconut source)
    if correctly_versioned_files:  #557 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #558 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #559 (line in Coconut source)

    compatibly_versioned_files = []  #561 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #562 (line in Coconut source)
        for raw_ver in versions:  #563 (line in Coconut source)
            try:  #564 (line in Coconut source)
                ver = ver_split(raw_ver)  #565 (line in Coconut source)
            except ValueError:  #566 (line in Coconut source)
                pass  #567 (line in Coconut source)
            else:  #568 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #569 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #570 (line in Coconut source)
    if compatibly_versioned_files:  #571 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #572 (line in Coconut source)

    maybe_compatible_files = []  #574 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #575 (line in Coconut source)
        for ver in versions:  #576 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #577 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #578 (line in Coconut source)
                break  #579 (line in Coconut source)
    if maybe_compatible_files:  #580 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #581 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #582 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #583 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #586 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #587 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #590 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #591 (line in Coconut source)
    missing_mods = []  #592 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #593 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #594 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #595 (line in Coconut source)
        if latest_version is None:  #596 (line in Coconut source)
            missing_mods.append(mod_name)  #597 (line in Coconut source)
        else:  #598 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #599 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #600 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #603 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #604 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #605 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #606 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #607 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #608 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #609 (line in Coconut source)
    return updated_mod_names_to_files  #610 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #613 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #614 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #615 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #616 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #617 (line in Coconut source)
    if os.path.exists(new_jar_path):  #618 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #619 (line in Coconut source)
    else:  #620 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #621 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #622 (line in Coconut source)
        if new_mod_name != mod_name:  #623 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #624 (line in Coconut source)
        result = requests.get(url)  #625 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #626 (line in Coconut source)
            jar_fobj.write(result.content)  #627 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #630 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #631 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #632 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #633 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #634 (line in Coconut source)
        if jar_name in seen_jar_names:  #635 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #636 (line in Coconut source)
        else:  #637 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #638 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #639 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #642 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #643 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #644 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #645 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #646 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #647 (line in Coconut source)



def make_dirs(*dirs):  #650 (line in Coconut source)
    for d in dirs:  #651 (line in Coconut source)
        if not os.path.exists(d):  #652 (line in Coconut source)
            os.mkdir(d)  #653 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None, google=False):  #656 (line in Coconut source)
    if interact is None and not PRINT_DEBUG:  #657 (line in Coconut source)
        interact = False  #658 (line in Coconut source)
    try:  #659 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #660 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names, google=google)  #661 (line in Coconut source)
        if not dry_run:  #662 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #663 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #664 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #665 (line in Coconut source)
            if updated_mod_names_to_files:  #666 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #667 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #668 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #669 (line in Coconut source)
        else:  #670 (line in Coconut source)
            missing_ids_mods = []  #671 (line in Coconut source)
            missing_files_mods = []  #672 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #673 (line in Coconut source)
    except Exception:  #674 (line in Coconut source)
        if interact is not False:  #675 (line in Coconut source)
            traceback.print_exc()  #676 (line in Coconut source)

            from coconut import embed  #678 (line in Coconut source)
            embed()  #679 (line in Coconut source)
        raise  #680 (line in Coconut source)
    if interact:  #681 (line in Coconut source)
        from coconut import embed  #682 (line in Coconut source)
        embed()  #683 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None, google=False):  #686 (line in Coconut source)
    couldnt_update = []  #687 (line in Coconut source)
    for mods_dir in mods_dirs:  #688 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #689 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #690 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact, google=google)  #691 (line in Coconut source)
    for mod_name in couldnt_update:  #692 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #693 (line in Coconut source)



@_coconut_tco  #696 (line in Coconut source)
def parse_args():  #696 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Update mods from CurseForge to their latest versions.")  #697 (line in Coconut source)
    parser.add_argument("--dry-run", action="store_true", help="Only check for missing CurseForge name mappings without downloading updates")  #700 (line in Coconut source)
    parser.add_argument("--google", action="store_true", help="Use Google search to find CurseForge names for unknown mods")  #705 (line in Coconut source)
    return _coconut_tail_call(parser.parse_args)  #710 (line in Coconut source)



def main():  #713 (line in Coconut source)
    args = parse_args()  #714 (line in Coconut source)

    sync_mods.main()  #716 (line in Coconut source)

    update_all(UPDATE_MODS_DIRS, dry_run=args.dry_run, google=args.google)  #718 (line in Coconut source)



if __name__ == "__main__":  #725 (line in Coconut source)
    main()  #726 (line in Coconut source)
