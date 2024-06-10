#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x358160d4

# Compiled with Coconut version 3.1.1-post_dev1

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.1-post_dev1', '', True)
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

import requests  #11 (line in Coconut source)

from minecraft_server_tools import sync_mods  #13 (line in Coconut source)
from minecraft_server_tools import google_api  #13 (line in Coconut source)
from minecraft_server_tools.constants import COMMENT_JSON  #14 (line in Coconut source)
from minecraft_server_tools.constants import MC_VERSION  #14 (line in Coconut source)
from minecraft_server_tools.constants import COMPONENT_SEPS  #14 (line in Coconut source)
from minecraft_server_tools.constants import NON_NAME_COMPONENT_REGEX  #14 (line in Coconut source)
from minecraft_server_tools.constants import NAME_REGEXES_TO_SPACE  #14 (line in Coconut source)
from minecraft_server_tools.constants import GOOGLE_QUERY_TEMPLATE  #14 (line in Coconut source)
from minecraft_server_tools.constants import NON_CURSEFORGE_MODS  #14 (line in Coconut source)
from minecraft_server_tools.constants import MODLOADER  #14 (line in Coconut source)
from minecraft_server_tools.constants import WRONG_MODLOADERS  #14 (line in Coconut source)
from minecraft_server_tools.constants import MAYBE_WRONG_MODLOADERS  #14 (line in Coconut source)
from minecraft_server_tools.constants import MOD_PAGE_NAME_SUFFICES  #14 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_NAMES_FILE  #14 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_FILE  #14 (line in Coconut source)
from minecraft_server_tools.constants import TIMESTAMP_FORMAT_REGEX  #14 (line in Coconut source)
from minecraft_server_tools.constants import UPDATED_MODS_DIR_SUFFIX  #14 (line in Coconut source)
from minecraft_server_tools.constants import OLD_MODS_DIR_SUFFIX  #14 (line in Coconut source)
from minecraft_server_tools.constants import DEBUG  #14 (line in Coconut source)
from minecraft_server_tools.constants import MAX_DEBUG_RESULTS  #14 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_NAME_ELEMS_TO_STRIP  #14 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_QUERY_TEMPLATES  #14 (line in Coconut source)
from minecraft_server_tools.constants import ALWAYS_USE_LATEST_VERSION_FOR_MODS  #14 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_RETRIES  #14 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_API_RETRY_DELAY  #14 (line in Coconut source)
from minecraft_server_tools.constants import AVOID_FILES_PUBLISHED_WITHIN  #14 (line in Coconut source)
from minecraft_server_tools.constants import FIX_MOD_NAMES  #14 (line in Coconut source)
from minecraft_server_tools.constants import ver_join  #14 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #14 (line in Coconut source)


BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #45 (line in Coconut source)


@_coconut_tco  #48 (line in Coconut source)
def get_mod_name(jar_name, silent=None, do_component_splitting=True):  #48 (line in Coconut source)
    def _coconut_mock_0(jar_name, silent=_coconut_sentinel, do_component_splitting=_coconut_sentinel):  #49 (line in Coconut source)
        if silent is _coconut_sentinel: silent = _coconut_recursive_func_0._coconut_tco_func.__defaults__[0]  #49 (line in Coconut source)
        if do_component_splitting is _coconut_sentinel: do_component_splitting = _coconut_recursive_func_0._coconut_tco_func.__defaults__[1]  #49 (line in Coconut source)
        return (jar_name, silent, do_component_splitting,)  #49 (line in Coconut source)
    while True:  #49 (line in Coconut source)
        if silent is None:  #49 (line in Coconut source)
            silent = not DEBUG  #50 (line in Coconut source)

        base_name = jar_name.removesuffix(".jar")  #52 (line in Coconut source)

        if do_component_splitting:  #54 (line in Coconut source)
            for sep, min_count in COMPONENT_SEPS:  #55 (line in Coconut source)
                components = base_name.split(sep)  #56 (line in Coconut source)
                if len(components) > min_count:  #57 (line in Coconut source)
                    break  #58 (line in Coconut source)
            else:  #59 (line in Coconut source)
                if not silent:  #60 (line in Coconut source)
                    print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #61 (line in Coconut source)
                components = [base_name,]  #62 (line in Coconut source)

            name_cmpnts = []  #64 (line in Coconut source)
            for cmpnt in components:  #65 (line in Coconut source)
                is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #66 (line in Coconut source)
                if is_name_cmpnt:  #67 (line in Coconut source)
                    name_cmpnts.append(cmpnt)  #68 (line in Coconut source)
                elif name_cmpnts:  #69 (line in Coconut source)
                    break  #70 (line in Coconut source)
            if not name_cmpnts:  #71 (line in Coconut source)
                if not silent:  #72 (line in Coconut source)
                    print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #73 (line in Coconut source)
                name_cmpnts = [components[0],]  #74 (line in Coconut source)
            mod_name = " ".join(name_cmpnts)  #75 (line in Coconut source)
        else:  #76 (line in Coconut source)
            mod_name = base_name  #77 (line in Coconut source)

        for to_space in NAME_REGEXES_TO_SPACE:  #79 (line in Coconut source)
            mod_name = to_space.sub(" ", mod_name)  #80 (line in Coconut source)

        if not mod_name:  #82 (line in Coconut source)
            if not silent:  #83 (line in Coconut source)
                print("Got empty mod name for jar {_coconut_format_0!r}; falling back to no component splitting.".format(_coconut_format_0=(jar_name)))  #84 (line in Coconut source)
            try:  #85 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #85 (line in Coconut source)
            except _coconut.NameError:  #85 (line in Coconut source)
                _coconut_tre_check_0 = False  #85 (line in Coconut source)
            if _coconut_tre_check_0:  #85 (line in Coconut source)
                (jar_name, silent, do_component_splitting,) = _coconut_mock_0(jar_name, do_component_splitting=False)  #85 (line in Coconut source)
                continue  #85 (line in Coconut source)
            else:  #85 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False)  #85 (line in Coconut source)


        camel_case_parts = [mod_name[0],]  #87 (line in Coconut source)
        prev_is_lower = mod_name[0].islower()  #88 (line in Coconut source)
        for c in mod_name[1:]:  #89 (line in Coconut source)
            if prev_is_lower and c.isupper():  #90 (line in Coconut source)
                camel_case_parts.append("")  #91 (line in Coconut source)
            camel_case_parts[-1] += c  #92 (line in Coconut source)
            prev_is_lower = c.islower()  #93 (line in Coconut source)

        mod_name = " ".join(camel_case_parts)  #95 (line in Coconut source)
        while "  " in mod_name:  #96 (line in Coconut source)
            mod_name = mod_name.replace("  ", " ")  #97 (line in Coconut source)

        mod_name = mod_name.strip().lower()  #99 (line in Coconut source)
        if not silent:  #100 (line in Coconut source)
            print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #101 (line in Coconut source)
        return mod_name  #104 (line in Coconut source)
    return None  #105 (line in Coconut source)

_coconut_recursive_func_0 = get_mod_name  #105 (line in Coconut source)

def get_curseforge_name(mod_name, jar_name):  #105 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #106 (line in Coconut source)
        return None  #107 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #108 (line in Coconut source)
    try:  #116 (line in Coconut source)
        while True:  #117 (line in Coconut source)
            search_json = google_api.google(query)  #118 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #119 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #120 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #121 (line in Coconut source)
                break  #122 (line in Coconut source)
            if "items" in search_json:  #123 (line in Coconut source)
                break  #124 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #125 (line in Coconut source)
            if "spelling" in search_json:  #126 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #127 (line in Coconut source)
                continue  #128 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #129 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #130 (line in Coconut source)
            break  #131 (line in Coconut source)
        items = search_json["items"]  #132 (line in Coconut source)
        curseforge_name = None  #133 (line in Coconut source)
        for result in items:  #134 (line in Coconut source)
            mod_page = result["title"]  #135 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #136 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #137 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #138 (line in Coconut source)
                    break  #139 (line in Coconut source)
            if curseforge_name is not None:  #140 (line in Coconut source)
                break  #141 (line in Coconut source)
            else:  #142 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #143 (line in Coconut source)
        if curseforge_name is None:  #144 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #145 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #146 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #147 (line in Coconut source)
        else:  #148 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #149 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #150 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #151 (line in Coconut source)
        if mod is None:  #152 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #153 (line in Coconut source)
        else:  #154 (line in Coconut source)
            return mod["name"]  #155 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #156 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #157 (line in Coconut source)
        pprint(search_json)  #158 (line in Coconut source)
        raise  #159 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #162 (line in Coconut source)
    old_curseforge_name = None  #163 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #164 (line in Coconut source)
        old_curseforge_name = curseforge_name  #165 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #166 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #167 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #168 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #169 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #170 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #171 (line in Coconut source)
    return curseforge_name  #172 (line in Coconut source)



@_coconut_tco  #175 (line in Coconut source)
def load_curseforge_names():  #175 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #176 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #177 (line in Coconut source)
            curseforge_names = COMMENT_JSON.load(ids_fobj)  #178 (line in Coconut source)
            if FIX_MOD_NAMES:  #179 (line in Coconut source)
                curseforge_names = _coconut.dict(((get_mod_name(mod_name)), (curseforge_name)) for mod_name, curseforge_name in curseforge_names.items())  #180 (line in Coconut source)
            return curseforge_names  #181 (line in Coconut source)
    else:  #182 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #183 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #186 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #187 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #188 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names):  #191 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #192 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #193 (line in Coconut source)
    try:  #194 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #195 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #196 (line in Coconut source)
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name])  #197 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #200 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #201 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #202 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #204 (line in Coconut source)
    finally:  #205 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #206 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #209 (line in Coconut source)
    nulled_mods = []  #210 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #211 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #212 (line in Coconut source)
        if curseforge_name is None:  #213 (line in Coconut source)
            nulled_mods.append(mod_name)  #214 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #215 (line in Coconut source)
        else:  #216 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #217 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #218 (line in Coconut source)



def get_jar_names(mods_dir):  #221 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #222 (line in Coconut source)
        if fname.endswith(".jar"):  #223 (line in Coconut source)
            yield fname  #224 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, **kwargs):  #227 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #228 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #229 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #230 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #231 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #232 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #233 (line in Coconut source)
    return mod_names_to_jar_names  #234 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #237 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #238 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #239 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #240 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #241 (line in Coconut source)
        if cmd_result.stderr:  #242 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #243 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #244 (line in Coconut source)
        else:  #245 (line in Coconut source)
            break  #246 (line in Coconut source)
    else:  #247 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #248 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #249 (line in Coconut source)
    if not api_result:  #250 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #251 (line in Coconut source)
        return []  #252 (line in Coconut source)
    try:  #253 (line in Coconut source)
        return json.loads(api_result)  #254 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #255 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #256 (line in Coconut source)
        print(api_result)  #257 (line in Coconut source)
        raise  #258 (line in Coconut source)



def has_bad_modloader(name):  #261 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS)):  #262 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #263 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS:  #264 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #265 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #266 (line in Coconut source)
    return False  #267 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #269 (line in Coconut source)
    found_mod = None  #270 (line in Coconut source)
    valid_modloader_results = []  #271 (line in Coconut source)
    for mod in results:  #272 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #273 (line in Coconut source)
        if mod["name"] == curseforge_name:  #274 (line in Coconut source)
            if not valid_modloader:  #275 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #276 (line in Coconut source)
            found_mod = mod  #277 (line in Coconut source)
            break  #278 (line in Coconut source)
        if valid_modloader:  #279 (line in Coconut source)
            valid_modloader_results.append(mod)  #280 (line in Coconut source)
    if found_mod is None:  #281 (line in Coconut source)
        for mod in valid_modloader_results:  #282 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #283 (line in Coconut source)
                found_mod = mod  #284 (line in Coconut source)
                break  #285 (line in Coconut source)
    if found_mod is None:  #286 (line in Coconut source)
        for mod in valid_modloader_results:  #287 (line in Coconut source)
            if curseforge_name in mod["name"]:  #288 (line in Coconut source)
                found_mod = mod  #289 (line in Coconut source)
                break  #290 (line in Coconut source)
    if found_mod is None:  #291 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #292 (line in Coconut source)
        for mod in valid_modloader_results:  #293 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #294 (line in Coconut source)
                found_mod = mod  #295 (line in Coconut source)
                break  #296 (line in Coconut source)
    if found_mod is None:  #297 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #298 (line in Coconut source)
        if core_curseforge_name:  #299 (line in Coconut source)
            for mod in valid_modloader_results:  #300 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #301 (line in Coconut source)
                    found_mod = mod  #302 (line in Coconut source)
                    break  #303 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #304 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #305 (line in Coconut source)
    return found_mod  #306 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #309 (line in Coconut source)
    if verbose:  #310 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #311 (line in Coconut source)
    else:  #312 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #313 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #316 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #319 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #320 (line in Coconut source)

    seen_queries = set()  #322 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #323 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #324 (line in Coconut source)
        if query in seen_queries:  #329 (line in Coconut source)
            continue  #330 (line in Coconut source)
        seen_queries.add(query)  #331 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #333 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #334 (line in Coconut source)
        if mod is not None:  #335 (line in Coconut source)
            return mod  #336 (line in Coconut source)
        if DEBUG:  #337 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #338 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #340 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #341 (line in Coconut source)
        if mod is not None:  #342 (line in Coconut source)
            return mod  #343 (line in Coconut source)
        if DEBUG:  #344 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #345 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #347 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #348 (line in Coconut source)
        if mod is not None:  #349 (line in Coconut source)
            return mod  #350 (line in Coconut source)
        if DEBUG:  #351 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #352 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #354 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #355 (line in Coconut source)
        if mod is not None:  #356 (line in Coconut source)
            return mod  #357 (line in Coconut source)
        if DEBUG:  #358 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #359 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #361 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #362 (line in Coconut source)
        if mod is not None:  #363 (line in Coconut source)
            return mod  #364 (line in Coconut source)
        if DEBUG:  #365 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #366 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #368 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #369 (line in Coconut source)
        if mod is not None:  #370 (line in Coconut source)
            return mod  #371 (line in Coconut source)
        if DEBUG:  #372 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #373 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #375 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #378 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #379 (line in Coconut source)
    if mod is not None:  #380 (line in Coconut source)
        return mod["id"]  #381 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #384 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #385 (line in Coconut source)
    missing_mods = []  #386 (line in Coconut source)
    for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #387 (line in Coconut source)
        curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #388 (line in Coconut source)
        if curseforge_id is None:  #389 (line in Coconut source)
            missing_mods.append(mod_name)  #390 (line in Coconut source)
        else:  #391 (line in Coconut source)
            mod_names_to_curseforge_ids[mod_name] = curseforge_id  #392 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #393 (line in Coconut source)



@_coconut_tco  #396 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #396 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #397 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #400 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #401 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #402 (line in Coconut source)
    if match_results is None:  #403 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #404 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #405 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #406 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #411 (line in Coconut source)
    return parsed_time  #412 (line in Coconut source)



@_coconut_tco  #415 (line in Coconut source)
def timestamp_sort(curseforge_files):  #415 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #415 (line in Coconut source)



@_coconut_tco  #422 (line in Coconut source)
def get_max_version(versions):  #422 (line in Coconut source)
    ver_tuples = []  #423 (line in Coconut source)
    for ver_str in versions:  #424 (line in Coconut source)
        try:  #425 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #426 (line in Coconut source)
        except ValueError:  #427 (line in Coconut source)
            pass  #428 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #429 (line in Coconut source)



@_coconut_tco  #432 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #432 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #432 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #446 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #447 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #450 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #451 (line in Coconut source)
    if url is None:  #452 (line in Coconut source)
        return None  #453 (line in Coconut source)
    else:  #454 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #455 (line in Coconut source)



def correct_modloader(versions, jar_name):  #458 (line in Coconut source)
    versions = [v.lower() for v in versions]  #459 (line in Coconut source)

    if MODLOADER.lower() in versions:  #461 (line in Coconut source)
        return True  #462 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #463 (line in Coconut source)
        return False  #464 (line in Coconut source)

    jar_name = jar_name.lower()  #466 (line in Coconut source)
    if has_bad_modloader(jar_name):  #467 (line in Coconut source)
        return False  #468 (line in Coconut source)

    return True  #470 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #473 (line in Coconut source)
    for file_data in curseforge_files:  #474 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #475 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #476 (line in Coconut source)
            return file_data  #477 (line in Coconut source)
    return None  #478 (line in Coconut source)



@_coconut_tco  #481 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #481 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #482 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #484 (line in Coconut source)
    if old_curseforge_file is None:  #485 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #486 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #487 (line in Coconut source)

    curseforge_files_and_versions = []  #489 (line in Coconut source)
    for file_data in curseforge_files:  #490 (line in Coconut source)
        versions = file_data["gameVersions"]  #491 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #492 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #493 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #498 (line in Coconut source)

    correctly_versioned_files = []  #500 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #501 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #502 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #503 (line in Coconut source)
    if correctly_versioned_files:  #504 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #505 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #506 (line in Coconut source)

    compatibly_versioned_files = []  #508 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #509 (line in Coconut source)
        for raw_ver in versions:  #510 (line in Coconut source)
            try:  #511 (line in Coconut source)
                ver = ver_split(raw_ver)  #512 (line in Coconut source)
            except ValueError:  #513 (line in Coconut source)
                pass  #514 (line in Coconut source)
            else:  #515 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #516 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #517 (line in Coconut source)
    if compatibly_versioned_files:  #518 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #519 (line in Coconut source)

    maybe_compatible_files = []  #521 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #522 (line in Coconut source)
        for ver in versions:  #523 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #524 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #525 (line in Coconut source)
                break  #526 (line in Coconut source)
    if maybe_compatible_files:  #527 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #528 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #529 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #530 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #533 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #534 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #537 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #538 (line in Coconut source)
    missing_mods = []  #539 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #540 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #541 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #542 (line in Coconut source)
        if latest_version is None:  #543 (line in Coconut source)
            missing_mods.append(mod_name)  #544 (line in Coconut source)
        else:  #545 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #546 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #547 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #550 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #551 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #552 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #553 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #554 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #555 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #556 (line in Coconut source)
    return updated_mod_names_to_files  #557 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #560 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #561 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #562 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #563 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #564 (line in Coconut source)
    if os.path.exists(new_jar_path):  #565 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #566 (line in Coconut source)
    else:  #567 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #568 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #569 (line in Coconut source)
        if new_mod_name != mod_name:  #570 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #571 (line in Coconut source)
        result = requests.get(url)  #572 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #573 (line in Coconut source)
            jar_fobj.write(result.content)  #574 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #577 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #578 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #579 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #580 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #581 (line in Coconut source)
        if jar_name in seen_jar_names:  #582 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #583 (line in Coconut source)
        else:  #584 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #585 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #586 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #589 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #590 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #591 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #592 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #593 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #594 (line in Coconut source)



def make_dirs(*dirs):  #597 (line in Coconut source)
    for d in dirs:  #598 (line in Coconut source)
        if not os.path.exists(d):  #599 (line in Coconut source)
            os.mkdir(d)  #600 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None):  #603 (line in Coconut source)
    if interact is None and not DEBUG:  #604 (line in Coconut source)
        interact = False  #605 (line in Coconut source)
    try:  #606 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #607 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names)  #608 (line in Coconut source)
        if not dry_run:  #609 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #610 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #611 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #612 (line in Coconut source)
            if updated_mod_names_to_files:  #613 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #614 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #615 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #616 (line in Coconut source)
        else:  #617 (line in Coconut source)
            missing_ids_mods = []  #618 (line in Coconut source)
            missing_files_mods = []  #619 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #620 (line in Coconut source)
    except Exception:  #621 (line in Coconut source)
        if interact is not False:  #622 (line in Coconut source)
            traceback.print_exc()  #623 (line in Coconut source)

            from coconut import embed  #625 (line in Coconut source)
            embed()  #626 (line in Coconut source)
        raise  #627 (line in Coconut source)
    if interact:  #628 (line in Coconut source)
        from coconut import embed  #629 (line in Coconut source)
        embed()  #630 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None):  #633 (line in Coconut source)
    couldnt_update = []  #634 (line in Coconut source)
    for mods_dir in mods_dirs:  #635 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #636 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #637 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact)  #638 (line in Coconut source)
    for mod_name in couldnt_update:  #639 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #640 (line in Coconut source)



def main():  #643 (line in Coconut source)
    sync_mods.main()  #644 (line in Coconut source)

    update_all([sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR], dry_run="--dry-run" in sys.argv)  #646 (line in Coconut source)

# from coconut import embed
# embed()



if __name__ == "__main__":  #660 (line in Coconut source)
    main()  #661 (line in Coconut source)
