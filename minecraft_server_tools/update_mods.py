#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4b7fa121

# Compiled with Coconut version 3.1.1-post_dev3

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.1-post_dev3', '', True)
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


BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #47 (line in Coconut source)


@_coconut_tco  #50 (line in Coconut source)
def get_mod_name(jar_name, silent=None, do_component_splitting=True):  #50 (line in Coconut source)
    def _coconut_mock_0(jar_name, silent=_coconut_sentinel, do_component_splitting=_coconut_sentinel):  #51 (line in Coconut source)
        if silent is _coconut_sentinel: silent = _coconut_recursive_func_0._coconut_tco_func.__defaults__[0]  #51 (line in Coconut source)
        if do_component_splitting is _coconut_sentinel: do_component_splitting = _coconut_recursive_func_0._coconut_tco_func.__defaults__[1]  #51 (line in Coconut source)
        return (jar_name, silent, do_component_splitting,)  #51 (line in Coconut source)
    while True:  #51 (line in Coconut source)
        if silent is None:  #51 (line in Coconut source)
            silent = not PRINT_DEBUG  #52 (line in Coconut source)

        base_name = jar_name.removesuffix(".jar")  #54 (line in Coconut source)

        if do_component_splitting:  #56 (line in Coconut source)
            for sep, min_count in COMPONENT_SEPS:  #57 (line in Coconut source)
                components = base_name.split(sep)  #58 (line in Coconut source)
                if len(components) > min_count:  #59 (line in Coconut source)
                    break  #60 (line in Coconut source)
            else:  #61 (line in Coconut source)
                if not silent:  #62 (line in Coconut source)
                    print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #63 (line in Coconut source)
                components = [base_name,]  #64 (line in Coconut source)

            name_cmpnts = []  #66 (line in Coconut source)
            for cmpnt in components:  #67 (line in Coconut source)
                is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #68 (line in Coconut source)
                if is_name_cmpnt:  #69 (line in Coconut source)
                    name_cmpnts.append(cmpnt)  #70 (line in Coconut source)
                elif name_cmpnts:  #71 (line in Coconut source)
                    break  #72 (line in Coconut source)
            if not name_cmpnts:  #73 (line in Coconut source)
                if not silent:  #74 (line in Coconut source)
                    print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #75 (line in Coconut source)
                name_cmpnts = [components[0],]  #76 (line in Coconut source)
            mod_name = " ".join(name_cmpnts)  #77 (line in Coconut source)
        else:  #78 (line in Coconut source)
            mod_name = base_name  #79 (line in Coconut source)

        for to_space in NAME_REGEXES_TO_SPACE:  #81 (line in Coconut source)
            mod_name = to_space.sub(" ", mod_name)  #82 (line in Coconut source)

        if not mod_name:  #84 (line in Coconut source)
            if not silent:  #85 (line in Coconut source)
                print("Got empty mod name for jar {_coconut_format_0!r}; falling back to no component splitting.".format(_coconut_format_0=(jar_name)))  #86 (line in Coconut source)
            try:  #87 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #87 (line in Coconut source)
            except _coconut.NameError:  #87 (line in Coconut source)
                _coconut_tre_check_0 = False  #87 (line in Coconut source)
            if _coconut_tre_check_0:  #87 (line in Coconut source)
                (jar_name, silent, do_component_splitting,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #87 (line in Coconut source)
                continue  #87 (line in Coconut source)
            else:  #87 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #87 (line in Coconut source)


        camel_case_parts = [mod_name[0],]  #89 (line in Coconut source)
        prev_is_lower = mod_name[0].islower()  #90 (line in Coconut source)
        for c in mod_name[1:]:  #91 (line in Coconut source)
            if prev_is_lower and c.isupper():  #92 (line in Coconut source)
                camel_case_parts.append("")  #93 (line in Coconut source)
            camel_case_parts[-1] += c  #94 (line in Coconut source)
            prev_is_lower = c.islower()  #95 (line in Coconut source)

        mod_name = " ".join(camel_case_parts)  #97 (line in Coconut source)
        while "  " in mod_name:  #98 (line in Coconut source)
            mod_name = mod_name.replace("  ", " ")  #99 (line in Coconut source)

        mod_name = mod_name.strip().lower()  #101 (line in Coconut source)

        if mod_name in NO_COMPONENT_SPLIT_MODS:  #103 (line in Coconut source)
            if not silent:  #104 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as no component splitting; redoing without component splitting.".format(_coconut_format_0=(mod_name)))  #105 (line in Coconut source)
            try:  #106 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #106 (line in Coconut source)
            except _coconut.NameError:  #106 (line in Coconut source)
                _coconut_tre_check_0 = False  #106 (line in Coconut source)
            if _coconut_tre_check_0:  #106 (line in Coconut source)
                (jar_name, silent, do_component_splitting,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #106 (line in Coconut source)
                continue  #106 (line in Coconut source)
            else:  #106 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #106 (line in Coconut source)


        if not silent:  #108 (line in Coconut source)
            print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #109 (line in Coconut source)
        return mod_name  #112 (line in Coconut source)
    return None  #113 (line in Coconut source)

_coconut_recursive_func_0 = get_mod_name  #113 (line in Coconut source)

def get_curseforge_name(mod_name, jar_name):  #113 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #114 (line in Coconut source)
        return None  #115 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #116 (line in Coconut source)
    try:  #124 (line in Coconut source)
        while True:  #125 (line in Coconut source)
            search_json = google_api.google(query)  #126 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #127 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #128 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #129 (line in Coconut source)
                break  #130 (line in Coconut source)
            if "items" in search_json:  #131 (line in Coconut source)
                break  #132 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #133 (line in Coconut source)
            if "spelling" in search_json:  #134 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #135 (line in Coconut source)
                continue  #136 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #137 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #138 (line in Coconut source)
            break  #139 (line in Coconut source)
        items = search_json["items"]  #140 (line in Coconut source)
        curseforge_name = None  #141 (line in Coconut source)
        for result in items:  #142 (line in Coconut source)
            mod_page = result["title"]  #143 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #144 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #145 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #146 (line in Coconut source)
                    break  #147 (line in Coconut source)
            if curseforge_name is not None:  #148 (line in Coconut source)
                break  #149 (line in Coconut source)
            else:  #150 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #151 (line in Coconut source)
        if curseforge_name is None:  #152 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #153 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #154 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #155 (line in Coconut source)
        else:  #156 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #157 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #158 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #159 (line in Coconut source)
        if mod is None:  #160 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #161 (line in Coconut source)
        else:  #162 (line in Coconut source)
            return mod["name"]  #163 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #164 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #165 (line in Coconut source)
        pprint(search_json)  #166 (line in Coconut source)
        raise  #167 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #170 (line in Coconut source)
    old_curseforge_name = None  #171 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #172 (line in Coconut source)
        old_curseforge_name = curseforge_name  #173 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #174 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #175 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #176 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #177 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #178 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #179 (line in Coconut source)
    return curseforge_name  #180 (line in Coconut source)



@_coconut_tco  #183 (line in Coconut source)
def load_curseforge_names():  #183 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #184 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #185 (line in Coconut source)
            curseforge_names = COMMENT_JSON.load(ids_fobj)  #186 (line in Coconut source)
            if FIX_MOD_NAMES:  #187 (line in Coconut source)
                curseforge_names = _coconut.dict(((get_mod_name(mod_name)), (curseforge_name)) for mod_name, curseforge_name in curseforge_names.items())  #188 (line in Coconut source)
            return curseforge_names  #189 (line in Coconut source)
    else:  #190 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #191 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #194 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #195 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #196 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names):  #199 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #200 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #201 (line in Coconut source)
    try:  #202 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #203 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #204 (line in Coconut source)
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name])  #205 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #208 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #209 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #210 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #212 (line in Coconut source)
    finally:  #213 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #214 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #217 (line in Coconut source)
    nulled_mods = []  #218 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #219 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #220 (line in Coconut source)
        if curseforge_name is None:  #221 (line in Coconut source)
            nulled_mods.append(mod_name)  #222 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #223 (line in Coconut source)
        else:  #224 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #225 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #226 (line in Coconut source)



def get_jar_names(mods_dir):  #229 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #230 (line in Coconut source)
        if fname.endswith(".jar"):  #231 (line in Coconut source)
            yield fname  #232 (line in Coconut source)



def get_mod_names_to_all_jar_names(mods_dir, **kwargs):  #235 (line in Coconut source)
    mod_names_to_all_jar_names = defaultdict(list)  #236 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #237 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #238 (line in Coconut source)
        mod_names_to_all_jar_names[mod_name] += [jar_name,]  #239 (line in Coconut source)
    return mod_names_to_all_jar_names  #240 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, **kwargs):  #243 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #244 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #245 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #246 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #247 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #248 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #249 (line in Coconut source)
    return mod_names_to_jar_names  #250 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #253 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #254 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #255 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #256 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #257 (line in Coconut source)
        if cmd_result.stderr:  #258 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #259 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #260 (line in Coconut source)
        else:  #261 (line in Coconut source)
            break  #262 (line in Coconut source)
    else:  #263 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #264 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #265 (line in Coconut source)
    if not api_result:  #266 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #267 (line in Coconut source)
        return []  #268 (line in Coconut source)
    try:  #269 (line in Coconut source)
        return json.loads(api_result)  #270 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #271 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #272 (line in Coconut source)
        print(api_result)  #273 (line in Coconut source)
        raise  #274 (line in Coconut source)



def has_bad_modloader(name):  #277 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS)):  #278 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #279 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS:  #280 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #281 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #282 (line in Coconut source)
    return False  #283 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #285 (line in Coconut source)
    found_mod = None  #286 (line in Coconut source)
    valid_modloader_results = []  #287 (line in Coconut source)
    for mod in results:  #288 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #289 (line in Coconut source)
        if mod["name"] == curseforge_name:  #290 (line in Coconut source)
            if not valid_modloader:  #291 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #292 (line in Coconut source)
            found_mod = mod  #293 (line in Coconut source)
            break  #294 (line in Coconut source)
        if valid_modloader:  #295 (line in Coconut source)
            valid_modloader_results.append(mod)  #296 (line in Coconut source)
    if found_mod is None:  #297 (line in Coconut source)
        for mod in valid_modloader_results:  #298 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #299 (line in Coconut source)
                found_mod = mod  #300 (line in Coconut source)
                break  #301 (line in Coconut source)
    if found_mod is None:  #302 (line in Coconut source)
        for mod in valid_modloader_results:  #303 (line in Coconut source)
            if curseforge_name in mod["name"]:  #304 (line in Coconut source)
                found_mod = mod  #305 (line in Coconut source)
                break  #306 (line in Coconut source)
    if found_mod is None:  #307 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #308 (line in Coconut source)
        for mod in valid_modloader_results:  #309 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #310 (line in Coconut source)
                found_mod = mod  #311 (line in Coconut source)
                break  #312 (line in Coconut source)
    if found_mod is None:  #313 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #314 (line in Coconut source)
        if core_curseforge_name:  #315 (line in Coconut source)
            for mod in valid_modloader_results:  #316 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #317 (line in Coconut source)
                    found_mod = mod  #318 (line in Coconut source)
                    break  #319 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #320 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #321 (line in Coconut source)
    return found_mod  #322 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #325 (line in Coconut source)
    if verbose:  #326 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #327 (line in Coconut source)
    else:  #328 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #329 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #332 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #335 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #336 (line in Coconut source)

    seen_queries = set()  #338 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #339 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #340 (line in Coconut source)
        if query in seen_queries:  #345 (line in Coconut source)
            continue  #346 (line in Coconut source)
        seen_queries.add(query)  #347 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #349 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #350 (line in Coconut source)
        if mod is not None:  #351 (line in Coconut source)
            return mod  #352 (line in Coconut source)
        if PRINT_DEBUG:  #353 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #354 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #356 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #357 (line in Coconut source)
        if mod is not None:  #358 (line in Coconut source)
            return mod  #359 (line in Coconut source)
        if PRINT_DEBUG:  #360 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #361 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #363 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #364 (line in Coconut source)
        if mod is not None:  #365 (line in Coconut source)
            return mod  #366 (line in Coconut source)
        if PRINT_DEBUG:  #367 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #368 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #370 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #371 (line in Coconut source)
        if mod is not None:  #372 (line in Coconut source)
            return mod  #373 (line in Coconut source)
        if PRINT_DEBUG:  #374 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #375 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #377 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #378 (line in Coconut source)
        if mod is not None:  #379 (line in Coconut source)
            return mod  #380 (line in Coconut source)
        if PRINT_DEBUG:  #381 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #382 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #384 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #385 (line in Coconut source)
        if mod is not None:  #386 (line in Coconut source)
            return mod  #387 (line in Coconut source)
        if PRINT_DEBUG:  #388 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #389 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #391 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #394 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #395 (line in Coconut source)
    if mod is not None:  #396 (line in Coconut source)
        return mod["id"]  #397 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #400 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #401 (line in Coconut source)
    missing_mods = []  #402 (line in Coconut source)
    for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #403 (line in Coconut source)
        curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #404 (line in Coconut source)
        if curseforge_id is None:  #405 (line in Coconut source)
            missing_mods.append(mod_name)  #406 (line in Coconut source)
        else:  #407 (line in Coconut source)
            mod_names_to_curseforge_ids[mod_name] = curseforge_id  #408 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #409 (line in Coconut source)



@_coconut_tco  #412 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #412 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #413 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #416 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #417 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #418 (line in Coconut source)
    if match_results is None:  #419 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #420 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #421 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #422 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #427 (line in Coconut source)
    return parsed_time  #428 (line in Coconut source)



@_coconut_tco  #431 (line in Coconut source)
def timestamp_sort(curseforge_files):  #431 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #431 (line in Coconut source)



@_coconut_tco  #438 (line in Coconut source)
def get_max_version(versions):  #438 (line in Coconut source)
    ver_tuples = []  #439 (line in Coconut source)
    for ver_str in versions:  #440 (line in Coconut source)
        try:  #441 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #442 (line in Coconut source)
        except ValueError:  #443 (line in Coconut source)
            pass  #444 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #445 (line in Coconut source)



@_coconut_tco  #448 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #448 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #448 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #462 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #463 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #466 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #467 (line in Coconut source)
    if url is None:  #468 (line in Coconut source)
        return None  #469 (line in Coconut source)
    else:  #470 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #471 (line in Coconut source)



def correct_modloader(versions, jar_name):  #474 (line in Coconut source)
    versions = [v.lower() for v in versions]  #475 (line in Coconut source)

    if MODLOADER.lower() in versions:  #477 (line in Coconut source)
        return True  #478 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #479 (line in Coconut source)
        return False  #480 (line in Coconut source)

    jar_name = jar_name.lower()  #482 (line in Coconut source)
    if has_bad_modloader(jar_name):  #483 (line in Coconut source)
        return False  #484 (line in Coconut source)

    return True  #486 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #489 (line in Coconut source)
    for file_data in curseforge_files:  #490 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #491 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #492 (line in Coconut source)
            return file_data  #493 (line in Coconut source)
    return None  #494 (line in Coconut source)



@_coconut_tco  #497 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #497 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #498 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #500 (line in Coconut source)
    if old_curseforge_file is None:  #501 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #502 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #503 (line in Coconut source)

    curseforge_files_and_versions = []  #505 (line in Coconut source)
    for file_data in curseforge_files:  #506 (line in Coconut source)
        versions = file_data["gameVersions"]  #507 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #508 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #509 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #514 (line in Coconut source)

    correctly_versioned_files = []  #516 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #517 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #518 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #519 (line in Coconut source)
    if correctly_versioned_files:  #520 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #521 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #522 (line in Coconut source)

    compatibly_versioned_files = []  #524 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #525 (line in Coconut source)
        for raw_ver in versions:  #526 (line in Coconut source)
            try:  #527 (line in Coconut source)
                ver = ver_split(raw_ver)  #528 (line in Coconut source)
            except ValueError:  #529 (line in Coconut source)
                pass  #530 (line in Coconut source)
            else:  #531 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #532 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #533 (line in Coconut source)
    if compatibly_versioned_files:  #534 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #535 (line in Coconut source)

    maybe_compatible_files = []  #537 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #538 (line in Coconut source)
        for ver in versions:  #539 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #540 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #541 (line in Coconut source)
                break  #542 (line in Coconut source)
    if maybe_compatible_files:  #543 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #544 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #545 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #546 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #549 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #550 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #553 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #554 (line in Coconut source)
    missing_mods = []  #555 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #556 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #557 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #558 (line in Coconut source)
        if latest_version is None:  #559 (line in Coconut source)
            missing_mods.append(mod_name)  #560 (line in Coconut source)
        else:  #561 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #562 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #563 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #566 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #567 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #568 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #569 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #570 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #571 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #572 (line in Coconut source)
    return updated_mod_names_to_files  #573 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #576 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #577 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #578 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #579 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #580 (line in Coconut source)
    if os.path.exists(new_jar_path):  #581 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #582 (line in Coconut source)
    else:  #583 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #584 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #585 (line in Coconut source)
        if new_mod_name != mod_name:  #586 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #587 (line in Coconut source)
        result = requests.get(url)  #588 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #589 (line in Coconut source)
            jar_fobj.write(result.content)  #590 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #593 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #594 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #595 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #596 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #597 (line in Coconut source)
        if jar_name in seen_jar_names:  #598 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #599 (line in Coconut source)
        else:  #600 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #601 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #602 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #605 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #606 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #607 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #608 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #609 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #610 (line in Coconut source)



def make_dirs(*dirs):  #613 (line in Coconut source)
    for d in dirs:  #614 (line in Coconut source)
        if not os.path.exists(d):  #615 (line in Coconut source)
            os.mkdir(d)  #616 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None):  #619 (line in Coconut source)
    if interact is None and not PRINT_DEBUG:  #620 (line in Coconut source)
        interact = False  #621 (line in Coconut source)
    try:  #622 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #623 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names)  #624 (line in Coconut source)
        if not dry_run:  #625 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #626 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #627 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #628 (line in Coconut source)
            if updated_mod_names_to_files:  #629 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #630 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #631 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #632 (line in Coconut source)
        else:  #633 (line in Coconut source)
            missing_ids_mods = []  #634 (line in Coconut source)
            missing_files_mods = []  #635 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #636 (line in Coconut source)
    except Exception:  #637 (line in Coconut source)
        if interact is not False:  #638 (line in Coconut source)
            traceback.print_exc()  #639 (line in Coconut source)

            from coconut import embed  #641 (line in Coconut source)
            embed()  #642 (line in Coconut source)
        raise  #643 (line in Coconut source)
    if interact:  #644 (line in Coconut source)
        from coconut import embed  #645 (line in Coconut source)
        embed()  #646 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None):  #649 (line in Coconut source)
    couldnt_update = []  #650 (line in Coconut source)
    for mods_dir in mods_dirs:  #651 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #652 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #653 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact)  #654 (line in Coconut source)
    for mod_name in couldnt_update:  #655 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #656 (line in Coconut source)



def main():  #659 (line in Coconut source)
    sync_mods.main()  #660 (line in Coconut source)

    update_all([sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR], dry_run="--dry-run" in sys.argv)  #662 (line in Coconut source)

# from coconut import embed
# embed()



if __name__ == "__main__":  #676 (line in Coconut source)
    main()  #677 (line in Coconut source)
