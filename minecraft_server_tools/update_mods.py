#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4077f8c4

# Compiled with Coconut version 3.1.1

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.1', '', True)
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
from minecraft_server_tools.constants import ver_join  #14 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #14 (line in Coconut source)


BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #43 (line in Coconut source)


def get_mod_name(jar_name, silent=None):  #46 (line in Coconut source)
    if silent is None:  #47 (line in Coconut source)
        silent = not DEBUG  #48 (line in Coconut source)
    base_name = jar_name.removesuffix(".jar")  #49 (line in Coconut source)
    for sep, min_count in COMPONENT_SEPS:  #50 (line in Coconut source)
        components = base_name.split(sep)  #51 (line in Coconut source)
        if len(components) > min_count:  #52 (line in Coconut source)
            break  #53 (line in Coconut source)
    else:  #54 (line in Coconut source)
        if not silent:  #55 (line in Coconut source)
            print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #56 (line in Coconut source)
        components = [base_name,]  #57 (line in Coconut source)
    name_cmpnts = []  #58 (line in Coconut source)
    for cmpnt in components:  #59 (line in Coconut source)
        is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #60 (line in Coconut source)
        if is_name_cmpnt:  #61 (line in Coconut source)
            name_cmpnts.append(cmpnt)  #62 (line in Coconut source)
        elif name_cmpnts:  #63 (line in Coconut source)
            break  #64 (line in Coconut source)
    if not name_cmpnts:  #65 (line in Coconut source)
        if not silent:  #66 (line in Coconut source)
            print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #67 (line in Coconut source)
        name_cmpnts = [components[0],]  #68 (line in Coconut source)
    mod_name = " ".join(name_cmpnts)  #69 (line in Coconut source)
    for to_space in NAME_REGEXES_TO_SPACE:  #70 (line in Coconut source)
        mod_name = to_space.sub(" ", mod_name)  #71 (line in Coconut source)
    mod_name = mod_name.strip()  #72 (line in Coconut source)
    if not silent:  #73 (line in Coconut source)
        print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #74 (line in Coconut source)
    return mod_name  #75 (line in Coconut source)



def get_curseforge_name(mod_name, jar_name):  #78 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #79 (line in Coconut source)
        return None  #80 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #81 (line in Coconut source)
    try:  #89 (line in Coconut source)
        while True:  #90 (line in Coconut source)
            search_json = google_api.google(query)  #91 (line in Coconut source)
            if "items" in search_json:  #92 (line in Coconut source)
                break  #93 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #94 (line in Coconut source)
            if "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #95 (line in Coconut source)
                raise Exception("Google API rate limit exceeded; try waiting or switching API keys.")  #96 (line in Coconut source)
            query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #97 (line in Coconut source)
        items = search_json["items"]  #98 (line in Coconut source)
        curseforge_name = None  #99 (line in Coconut source)
        for result in items:  #100 (line in Coconut source)
            mod_page = result["title"]  #101 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #102 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #103 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #104 (line in Coconut source)
                    break  #105 (line in Coconut source)
            if curseforge_name is not None:  #106 (line in Coconut source)
                break  #107 (line in Coconut source)
            else:  #108 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #109 (line in Coconut source)
        if curseforge_name is None:  #110 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #111 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #112 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #113 (line in Coconut source)
        else:  #114 (line in Coconut source)
            print("Found Curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name)))  #115 (line in Coconut source)
            return curseforge_name  #116 (line in Coconut source)
    except (KeyError, IndexError):  #117 (line in Coconut source)
        print("ERROR: Invalid search results for query {_coconut_format_0!r}:".format(_coconut_format_0=(query)))  #118 (line in Coconut source)
        pprint(search_json)  #119 (line in Coconut source)
        raise  #120 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #123 (line in Coconut source)
    old_curseforge_name = None  #124 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #125 (line in Coconut source)
        old_curseforge_name = curseforge_name  #126 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #127 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #128 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #129 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #130 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #131 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #132 (line in Coconut source)
    return curseforge_name  #133 (line in Coconut source)



@_coconut_tco  #136 (line in Coconut source)
def load_curseforge_names():  #136 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #137 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #138 (line in Coconut source)
            return COMMENT_JSON.load(ids_fobj)  #139 (line in Coconut source)
    else:  #140 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #141 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #144 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #145 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #146 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names):  #149 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #150 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #151 (line in Coconut source)
    try:  #152 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #153 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #154 (line in Coconut source)
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name])  #155 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #158 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #159 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #160 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #162 (line in Coconut source)
    finally:  #163 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #164 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #167 (line in Coconut source)
    nulled_mods = []  #168 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #169 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #170 (line in Coconut source)
        if curseforge_name is None:  #171 (line in Coconut source)
            nulled_mods.append(mod_name)  #172 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #173 (line in Coconut source)
        else:  #174 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #175 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #176 (line in Coconut source)



def get_jar_names(mods_dir):  #179 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #180 (line in Coconut source)
        if fname.endswith(".jar"):  #181 (line in Coconut source)
            yield fname  #182 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, silent=None):  #185 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #186 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #187 (line in Coconut source)
        mod_name = get_mod_name(jar_name, silent=silent)  #188 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #189 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #190 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #191 (line in Coconut source)
    return mod_names_to_jar_names  #192 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #195 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #196 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #197 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #198 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #199 (line in Coconut source)
        if cmd_result.stderr:  #200 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #201 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #202 (line in Coconut source)
        else:  #203 (line in Coconut source)
            break  #204 (line in Coconut source)
    else:  #205 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #206 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #207 (line in Coconut source)
    if not api_result:  #208 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #209 (line in Coconut source)
        return []  #210 (line in Coconut source)
    try:  #211 (line in Coconut source)
        return json.loads(api_result)  #212 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #213 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #214 (line in Coconut source)
        print(api_result)  #215 (line in Coconut source)
        raise  #216 (line in Coconut source)



def has_bad_modloader(name):  #219 (line in Coconut source)
    return (MODLOADER.lower() not in name.lower() and any((m.lower() in name.lower() for m in WRONG_MODLOADERS)))  #219 (line in Coconut source)



def get_matching_mod(results, curseforge_name, mod_name):  #225 (line in Coconut source)
    found_mod = None  #226 (line in Coconut source)
    valid_modloader_results = []  #227 (line in Coconut source)
    for mod in results:  #228 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #229 (line in Coconut source)
        if mod["name"] == curseforge_name:  #230 (line in Coconut source)
            if not valid_modloader:  #231 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #232 (line in Coconut source)
            found_mod = mod  #233 (line in Coconut source)
            break  #234 (line in Coconut source)
        if valid_modloader:  #235 (line in Coconut source)
            valid_modloader_results.append(mod)  #236 (line in Coconut source)
    if found_mod is None:  #237 (line in Coconut source)
        for mod in valid_modloader_results:  #238 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #239 (line in Coconut source)
                found_mod = mod  #240 (line in Coconut source)
                break  #241 (line in Coconut source)
    if found_mod is None:  #242 (line in Coconut source)
        for mod in valid_modloader_results:  #243 (line in Coconut source)
            if curseforge_name in mod["name"]:  #244 (line in Coconut source)
                found_mod = mod  #245 (line in Coconut source)
                break  #246 (line in Coconut source)
    if found_mod is None:  #247 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #248 (line in Coconut source)
        for mod in valid_modloader_results:  #249 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #250 (line in Coconut source)
                found_mod = mod  #251 (line in Coconut source)
                break  #252 (line in Coconut source)
    if found_mod is None:  #253 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #254 (line in Coconut source)
        if core_curseforge_name:  #255 (line in Coconut source)
            for mod in valid_modloader_results:  #256 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #257 (line in Coconut source)
                    found_mod = mod  #258 (line in Coconut source)
                    break  #259 (line in Coconut source)
    if found_mod is not None and found_mod["name"] != curseforge_name:  #260 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #261 (line in Coconut source)
    return found_mod  #262 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #265 (line in Coconut source)
    if verbose:  #266 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #267 (line in Coconut source)
    else:  #268 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #269 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #272 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #275 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #276 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #277 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #278 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #284 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #285 (line in Coconut source)
        if mod is not None:  #286 (line in Coconut source)
            return mod  #287 (line in Coconut source)
        if DEBUG:  #288 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #289 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #291 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #292 (line in Coconut source)
        if mod is not None:  #293 (line in Coconut source)
            return mod  #294 (line in Coconut source)
        if DEBUG:  #295 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #296 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #298 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #299 (line in Coconut source)
        if mod is not None:  #300 (line in Coconut source)
            return mod  #301 (line in Coconut source)
        if DEBUG:  #302 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #303 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #305 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #306 (line in Coconut source)
        if mod is not None:  #307 (line in Coconut source)
            return mod  #308 (line in Coconut source)
        if DEBUG:  #309 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #310 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #312 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #313 (line in Coconut source)
        if mod is not None:  #314 (line in Coconut source)
            return mod  #315 (line in Coconut source)
        if DEBUG:  #316 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #317 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #319 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #320 (line in Coconut source)
        if mod is not None:  #321 (line in Coconut source)
            return mod  #322 (line in Coconut source)
        if DEBUG:  #323 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #324 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #326 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #329 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #330 (line in Coconut source)
    if mod is not None:  #331 (line in Coconut source)
        return mod["id"]  #332 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #335 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #336 (line in Coconut source)
    missing_mods = []  #337 (line in Coconut source)
    for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #338 (line in Coconut source)
        curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #339 (line in Coconut source)
        if curseforge_id is None:  #340 (line in Coconut source)
            missing_mods.append(mod_name)  #341 (line in Coconut source)
        else:  #342 (line in Coconut source)
            mod_names_to_curseforge_ids[mod_name] = curseforge_id  #343 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #344 (line in Coconut source)



@_coconut_tco  #347 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #347 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #348 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #351 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #352 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #353 (line in Coconut source)
    if match_results is None:  #354 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #355 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #356 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #357 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #362 (line in Coconut source)
    return parsed_time  #363 (line in Coconut source)



@_coconut_tco  #366 (line in Coconut source)
def timestamp_sort(curseforge_files):  #366 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #366 (line in Coconut source)



@_coconut_tco  #373 (line in Coconut source)
def get_max_version(versions):  #373 (line in Coconut source)
    ver_tuples = []  #374 (line in Coconut source)
    for ver_str in versions:  #375 (line in Coconut source)
        try:  #376 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #377 (line in Coconut source)
        except ValueError:  #378 (line in Coconut source)
            pass  #379 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #380 (line in Coconut source)



@_coconut_tco  #383 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #383 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #383 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #397 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #398 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #401 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #402 (line in Coconut source)
    if url is None:  #403 (line in Coconut source)
        return None  #404 (line in Coconut source)
    else:  #405 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #406 (line in Coconut source)



def correct_modloader(versions, jar_name):  #409 (line in Coconut source)
    versions = [v.lower() for v in versions]  #410 (line in Coconut source)

    if MODLOADER.lower() in versions:  #412 (line in Coconut source)
        return True  #413 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #414 (line in Coconut source)
        return False  #415 (line in Coconut source)

    jar_name = jar_name.lower()  #417 (line in Coconut source)
    if MODLOADER.lower() in jar_name:  #418 (line in Coconut source)
        return True  #419 (line in Coconut source)
    if any((wrong_modloader.lower() in jar_name for wrong_modloader in WRONG_MODLOADERS)):  #420 (line in Coconut source)
        return False  #421 (line in Coconut source)

    return True  #423 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #426 (line in Coconut source)
    for file_data in curseforge_files:  #427 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #428 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #429 (line in Coconut source)
            return file_data  #430 (line in Coconut source)
    return None  #431 (line in Coconut source)



@_coconut_tco  #434 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #434 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #435 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #437 (line in Coconut source)
    if old_curseforge_file is None:  #438 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #439 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #440 (line in Coconut source)

    curseforge_files_and_versions = []  #442 (line in Coconut source)
    for file_data in curseforge_files:  #443 (line in Coconut source)
        versions = file_data["gameVersions"]  #444 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #445 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #446 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #451 (line in Coconut source)

    correctly_versioned_files = []  #453 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #454 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #455 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #456 (line in Coconut source)
    if correctly_versioned_files:  #457 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #458 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #459 (line in Coconut source)

    compatibly_versioned_files = []  #461 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #462 (line in Coconut source)
        for raw_ver in versions:  #463 (line in Coconut source)
            try:  #464 (line in Coconut source)
                ver = ver_split(raw_ver)  #465 (line in Coconut source)
            except ValueError:  #466 (line in Coconut source)
                pass  #467 (line in Coconut source)
            else:  #468 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #469 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #470 (line in Coconut source)
    if compatibly_versioned_files:  #471 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #472 (line in Coconut source)

    maybe_compatible_files = []  #474 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #475 (line in Coconut source)
        for ver in versions:  #476 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #477 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #478 (line in Coconut source)
                break  #479 (line in Coconut source)
    if maybe_compatible_files:  #480 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #481 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #482 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #483 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #486 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #487 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #490 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #491 (line in Coconut source)
    missing_mods = []  #492 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #493 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #494 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #495 (line in Coconut source)
        if latest_version is None:  #496 (line in Coconut source)
            missing_mods.append(mod_name)  #497 (line in Coconut source)
        else:  #498 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #499 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #500 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #503 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #504 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #505 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #506 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #507 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #508 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #509 (line in Coconut source)
    return updated_mod_names_to_files  #510 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #513 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #514 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #515 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #516 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #517 (line in Coconut source)
    if os.path.exists(new_jar_path):  #518 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #519 (line in Coconut source)
    else:  #520 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #521 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #522 (line in Coconut source)
        if new_mod_name != mod_name:  #523 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #524 (line in Coconut source)
        result = requests.get(url)  #525 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #526 (line in Coconut source)
            jar_fobj.write(result.content)  #527 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #530 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #531 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #532 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #533 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #534 (line in Coconut source)
        if jar_name in seen_jar_names:  #535 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #536 (line in Coconut source)
        else:  #537 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #538 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #539 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #542 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #543 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #544 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #545 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #546 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #547 (line in Coconut source)



def make_dirs(*dirs):  #550 (line in Coconut source)
    for d in dirs:  #551 (line in Coconut source)
        if not os.path.exists(d):  #552 (line in Coconut source)
            os.mkdir(d)  #553 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None):  #556 (line in Coconut source)
    if interact is None and not DEBUG:  #557 (line in Coconut source)
        interact = False  #558 (line in Coconut source)
    try:  #559 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #560 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names)  #561 (line in Coconut source)
        if not dry_run:  #562 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #563 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #564 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #565 (line in Coconut source)
            if updated_mod_names_to_files:  #566 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #567 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #568 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #569 (line in Coconut source)
        else:  #570 (line in Coconut source)
            missing_ids_mods = []  #571 (line in Coconut source)
            missing_files_mods = []  #572 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #573 (line in Coconut source)
    except Exception:  #574 (line in Coconut source)
        if interact is not False:  #575 (line in Coconut source)
            traceback.print_exc()  #576 (line in Coconut source)

            from coconut import embed  #578 (line in Coconut source)
            embed()  #579 (line in Coconut source)
        raise  #580 (line in Coconut source)
    if interact:  #581 (line in Coconut source)
        from coconut import embed  #582 (line in Coconut source)
        embed()  #583 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None):  #586 (line in Coconut source)
    couldnt_update = []  #587 (line in Coconut source)
    for mods_dir in mods_dirs:  #588 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #589 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #590 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact)  #591 (line in Coconut source)
    for mod_name in couldnt_update:  #592 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #593 (line in Coconut source)



def main():  #596 (line in Coconut source)
    sync_mods.main()  #597 (line in Coconut source)

    update_all([sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR], dry_run="--dry-run" in sys.argv)  #599 (line in Coconut source)

# from coconut import embed
# embed()



if __name__ == "__main__":  #613 (line in Coconut source)
    main()  #614 (line in Coconut source)
