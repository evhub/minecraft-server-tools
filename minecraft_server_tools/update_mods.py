#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfa59d9fd

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
from minecraft_server_tools.constants import ver_join  #14 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #14 (line in Coconut source)


BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #44 (line in Coconut source)


def get_mod_name(jar_name, silent=None, lower=False):  #47 (line in Coconut source)
    if silent is None:  #48 (line in Coconut source)
        silent = not DEBUG  #49 (line in Coconut source)
    base_name = jar_name.removesuffix(".jar")  #50 (line in Coconut source)
    for sep, min_count in COMPONENT_SEPS:  #51 (line in Coconut source)
        components = base_name.split(sep)  #52 (line in Coconut source)
        if len(components) > min_count:  #53 (line in Coconut source)
            break  #54 (line in Coconut source)
    else:  #55 (line in Coconut source)
        if not silent:  #56 (line in Coconut source)
            print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #57 (line in Coconut source)
        components = [base_name,]  #58 (line in Coconut source)
    name_cmpnts = []  #59 (line in Coconut source)
    for cmpnt in components:  #60 (line in Coconut source)
        is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #61 (line in Coconut source)
        if is_name_cmpnt:  #62 (line in Coconut source)
            name_cmpnts.append(cmpnt)  #63 (line in Coconut source)
        elif name_cmpnts:  #64 (line in Coconut source)
            break  #65 (line in Coconut source)
    if not name_cmpnts:  #66 (line in Coconut source)
        if not silent:  #67 (line in Coconut source)
            print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #68 (line in Coconut source)
        name_cmpnts = [components[0],]  #69 (line in Coconut source)
    mod_name = " ".join(name_cmpnts)  #70 (line in Coconut source)
    for to_space in NAME_REGEXES_TO_SPACE:  #71 (line in Coconut source)
        mod_name = to_space.sub(" ", mod_name)  #72 (line in Coconut source)
    mod_name = mod_name.strip()  #73 (line in Coconut source)
    if not silent:  #74 (line in Coconut source)
        print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #75 (line in Coconut source)
    if lower:  #76 (line in Coconut source)
        mod_name = mod_name.lower()  #77 (line in Coconut source)
    return mod_name  #78 (line in Coconut source)



def get_curseforge_name(mod_name, jar_name):  #81 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #82 (line in Coconut source)
        return None  #83 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #84 (line in Coconut source)
    try:  #92 (line in Coconut source)
        while True:  #93 (line in Coconut source)
            search_json = google_api.google(query)  #94 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #95 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #96 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #97 (line in Coconut source)
                break  #98 (line in Coconut source)
            if "items" in search_json:  #99 (line in Coconut source)
                break  #100 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #101 (line in Coconut source)
            if "spelling" in search_json:  #102 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #103 (line in Coconut source)
                continue  #104 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #105 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #106 (line in Coconut source)
            break  #107 (line in Coconut source)
        items = search_json["items"]  #108 (line in Coconut source)
        curseforge_name = None  #109 (line in Coconut source)
        for result in items:  #110 (line in Coconut source)
            mod_page = result["title"]  #111 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #112 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #113 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #114 (line in Coconut source)
                    break  #115 (line in Coconut source)
            if curseforge_name is not None:  #116 (line in Coconut source)
                break  #117 (line in Coconut source)
            else:  #118 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #119 (line in Coconut source)
        if curseforge_name is None:  #120 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #121 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #122 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #123 (line in Coconut source)
        else:  #124 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #125 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #126 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #127 (line in Coconut source)
        if mod is None:  #128 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #129 (line in Coconut source)
        else:  #130 (line in Coconut source)
            return mod["name"]  #131 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #132 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #133 (line in Coconut source)
        pprint(search_json)  #134 (line in Coconut source)
        raise  #135 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #138 (line in Coconut source)
    old_curseforge_name = None  #139 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #140 (line in Coconut source)
        old_curseforge_name = curseforge_name  #141 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #142 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #143 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #144 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #145 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #146 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #147 (line in Coconut source)
    return curseforge_name  #148 (line in Coconut source)



@_coconut_tco  #151 (line in Coconut source)
def load_curseforge_names():  #151 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #152 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #153 (line in Coconut source)
            return COMMENT_JSON.load(ids_fobj)  #154 (line in Coconut source)
    else:  #155 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #156 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #159 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #160 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #161 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names):  #164 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #165 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #166 (line in Coconut source)
    try:  #167 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #168 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #169 (line in Coconut source)
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name])  #170 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #173 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #174 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #175 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #177 (line in Coconut source)
    finally:  #178 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #179 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #182 (line in Coconut source)
    nulled_mods = []  #183 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #184 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #185 (line in Coconut source)
        if curseforge_name is None:  #186 (line in Coconut source)
            nulled_mods.append(mod_name)  #187 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #188 (line in Coconut source)
        else:  #189 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #190 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #191 (line in Coconut source)



def get_jar_names(mods_dir):  #194 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #195 (line in Coconut source)
        if fname.endswith(".jar"):  #196 (line in Coconut source)
            yield fname  #197 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, **kwargs):  #200 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #201 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #202 (line in Coconut source)
        mod_name = get_mod_name(jar_name, **kwargs)  #203 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #204 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #205 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #206 (line in Coconut source)
    return mod_names_to_jar_names  #207 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #210 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #211 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #212 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #213 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #214 (line in Coconut source)
        if cmd_result.stderr:  #215 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #216 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #217 (line in Coconut source)
        else:  #218 (line in Coconut source)
            break  #219 (line in Coconut source)
    else:  #220 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #221 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #222 (line in Coconut source)
    if not api_result:  #223 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #224 (line in Coconut source)
        return []  #225 (line in Coconut source)
    try:  #226 (line in Coconut source)
        return json.loads(api_result)  #227 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #228 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #229 (line in Coconut source)
        print(api_result)  #230 (line in Coconut source)
        raise  #231 (line in Coconut source)



def has_bad_modloader(name):  #234 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS)):  #235 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #236 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS:  #237 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #238 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #239 (line in Coconut source)
    return False  #240 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #242 (line in Coconut source)
    found_mod = None  #243 (line in Coconut source)
    valid_modloader_results = []  #244 (line in Coconut source)
    for mod in results:  #245 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #246 (line in Coconut source)
        if mod["name"] == curseforge_name:  #247 (line in Coconut source)
            if not valid_modloader:  #248 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #249 (line in Coconut source)
            found_mod = mod  #250 (line in Coconut source)
            break  #251 (line in Coconut source)
        if valid_modloader:  #252 (line in Coconut source)
            valid_modloader_results.append(mod)  #253 (line in Coconut source)
    if found_mod is None:  #254 (line in Coconut source)
        for mod in valid_modloader_results:  #255 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #256 (line in Coconut source)
                found_mod = mod  #257 (line in Coconut source)
                break  #258 (line in Coconut source)
    if found_mod is None:  #259 (line in Coconut source)
        for mod in valid_modloader_results:  #260 (line in Coconut source)
            if curseforge_name in mod["name"]:  #261 (line in Coconut source)
                found_mod = mod  #262 (line in Coconut source)
                break  #263 (line in Coconut source)
    if found_mod is None:  #264 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #265 (line in Coconut source)
        for mod in valid_modloader_results:  #266 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #267 (line in Coconut source)
                found_mod = mod  #268 (line in Coconut source)
                break  #269 (line in Coconut source)
    if found_mod is None:  #270 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #271 (line in Coconut source)
        if core_curseforge_name:  #272 (line in Coconut source)
            for mod in valid_modloader_results:  #273 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #274 (line in Coconut source)
                    found_mod = mod  #275 (line in Coconut source)
                    break  #276 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #277 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #278 (line in Coconut source)
    return found_mod  #279 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #282 (line in Coconut source)
    if verbose:  #283 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #284 (line in Coconut source)
    else:  #285 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #286 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #289 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #292 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #293 (line in Coconut source)

    seen_queries = set()  #295 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #296 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #297 (line in Coconut source)
        if query in seen_queries:  #302 (line in Coconut source)
            continue  #303 (line in Coconut source)
        seen_queries.add(query)  #304 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #306 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #307 (line in Coconut source)
        if mod is not None:  #308 (line in Coconut source)
            return mod  #309 (line in Coconut source)
        if DEBUG:  #310 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #311 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #313 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #314 (line in Coconut source)
        if mod is not None:  #315 (line in Coconut source)
            return mod  #316 (line in Coconut source)
        if DEBUG:  #317 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #318 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #320 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #321 (line in Coconut source)
        if mod is not None:  #322 (line in Coconut source)
            return mod  #323 (line in Coconut source)
        if DEBUG:  #324 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #325 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #327 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #328 (line in Coconut source)
        if mod is not None:  #329 (line in Coconut source)
            return mod  #330 (line in Coconut source)
        if DEBUG:  #331 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #332 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #334 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #335 (line in Coconut source)
        if mod is not None:  #336 (line in Coconut source)
            return mod  #337 (line in Coconut source)
        if DEBUG:  #338 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #339 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #341 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #342 (line in Coconut source)
        if mod is not None:  #343 (line in Coconut source)
            return mod  #344 (line in Coconut source)
        if DEBUG:  #345 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #346 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #348 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #351 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #352 (line in Coconut source)
    if mod is not None:  #353 (line in Coconut source)
        return mod["id"]  #354 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #357 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #358 (line in Coconut source)
    missing_mods = []  #359 (line in Coconut source)
    for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #360 (line in Coconut source)
        curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #361 (line in Coconut source)
        if curseforge_id is None:  #362 (line in Coconut source)
            missing_mods.append(mod_name)  #363 (line in Coconut source)
        else:  #364 (line in Coconut source)
            mod_names_to_curseforge_ids[mod_name] = curseforge_id  #365 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #366 (line in Coconut source)



@_coconut_tco  #369 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #369 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #370 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #373 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #374 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #375 (line in Coconut source)
    if match_results is None:  #376 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #377 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #378 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #379 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #384 (line in Coconut source)
    return parsed_time  #385 (line in Coconut source)



@_coconut_tco  #388 (line in Coconut source)
def timestamp_sort(curseforge_files):  #388 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #388 (line in Coconut source)



@_coconut_tco  #395 (line in Coconut source)
def get_max_version(versions):  #395 (line in Coconut source)
    ver_tuples = []  #396 (line in Coconut source)
    for ver_str in versions:  #397 (line in Coconut source)
        try:  #398 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #399 (line in Coconut source)
        except ValueError:  #400 (line in Coconut source)
            pass  #401 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #402 (line in Coconut source)



@_coconut_tco  #405 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #405 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #405 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #419 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #420 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #423 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #424 (line in Coconut source)
    if url is None:  #425 (line in Coconut source)
        return None  #426 (line in Coconut source)
    else:  #427 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #428 (line in Coconut source)



def correct_modloader(versions, jar_name):  #431 (line in Coconut source)
    versions = [v.lower() for v in versions]  #432 (line in Coconut source)

    if MODLOADER.lower() in versions:  #434 (line in Coconut source)
        return True  #435 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #436 (line in Coconut source)
        return False  #437 (line in Coconut source)

    jar_name = jar_name.lower()  #439 (line in Coconut source)
    if has_bad_modloader(jar_name):  #440 (line in Coconut source)
        return False  #441 (line in Coconut source)

    return True  #443 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #446 (line in Coconut source)
    for file_data in curseforge_files:  #447 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #448 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #449 (line in Coconut source)
            return file_data  #450 (line in Coconut source)
    return None  #451 (line in Coconut source)



@_coconut_tco  #454 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #454 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #455 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #457 (line in Coconut source)
    if old_curseforge_file is None:  #458 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #459 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #460 (line in Coconut source)

    curseforge_files_and_versions = []  #462 (line in Coconut source)
    for file_data in curseforge_files:  #463 (line in Coconut source)
        versions = file_data["gameVersions"]  #464 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #465 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #466 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #471 (line in Coconut source)

    correctly_versioned_files = []  #473 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #474 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #475 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #476 (line in Coconut source)
    if correctly_versioned_files:  #477 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #478 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #479 (line in Coconut source)

    compatibly_versioned_files = []  #481 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #482 (line in Coconut source)
        for raw_ver in versions:  #483 (line in Coconut source)
            try:  #484 (line in Coconut source)
                ver = ver_split(raw_ver)  #485 (line in Coconut source)
            except ValueError:  #486 (line in Coconut source)
                pass  #487 (line in Coconut source)
            else:  #488 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #489 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #490 (line in Coconut source)
    if compatibly_versioned_files:  #491 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #492 (line in Coconut source)

    maybe_compatible_files = []  #494 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #495 (line in Coconut source)
        for ver in versions:  #496 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #497 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #498 (line in Coconut source)
                break  #499 (line in Coconut source)
    if maybe_compatible_files:  #500 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #501 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #502 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #503 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #506 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #507 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #510 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #511 (line in Coconut source)
    missing_mods = []  #512 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #513 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #514 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #515 (line in Coconut source)
        if latest_version is None:  #516 (line in Coconut source)
            missing_mods.append(mod_name)  #517 (line in Coconut source)
        else:  #518 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #519 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #520 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #523 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #524 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #525 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #526 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #527 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #528 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #529 (line in Coconut source)
    return updated_mod_names_to_files  #530 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #533 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #534 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #535 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #536 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #537 (line in Coconut source)
    if os.path.exists(new_jar_path):  #538 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #539 (line in Coconut source)
    else:  #540 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #541 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #542 (line in Coconut source)
        if new_mod_name != mod_name:  #543 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #544 (line in Coconut source)
        result = requests.get(url)  #545 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #546 (line in Coconut source)
            jar_fobj.write(result.content)  #547 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #550 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #551 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #552 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #553 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #554 (line in Coconut source)
        if jar_name in seen_jar_names:  #555 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #556 (line in Coconut source)
        else:  #557 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #558 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #559 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #562 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #563 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #564 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #565 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #566 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #567 (line in Coconut source)



def make_dirs(*dirs):  #570 (line in Coconut source)
    for d in dirs:  #571 (line in Coconut source)
        if not os.path.exists(d):  #572 (line in Coconut source)
            os.mkdir(d)  #573 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None):  #576 (line in Coconut source)
    if interact is None and not DEBUG:  #577 (line in Coconut source)
        interact = False  #578 (line in Coconut source)
    try:  #579 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #580 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names)  #581 (line in Coconut source)
        if not dry_run:  #582 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #583 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #584 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #585 (line in Coconut source)
            if updated_mod_names_to_files:  #586 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #587 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #588 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #589 (line in Coconut source)
        else:  #590 (line in Coconut source)
            missing_ids_mods = []  #591 (line in Coconut source)
            missing_files_mods = []  #592 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #593 (line in Coconut source)
    except Exception:  #594 (line in Coconut source)
        if interact is not False:  #595 (line in Coconut source)
            traceback.print_exc()  #596 (line in Coconut source)

            from coconut import embed  #598 (line in Coconut source)
            embed()  #599 (line in Coconut source)
        raise  #600 (line in Coconut source)
    if interact:  #601 (line in Coconut source)
        from coconut import embed  #602 (line in Coconut source)
        embed()  #603 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None):  #606 (line in Coconut source)
    couldnt_update = []  #607 (line in Coconut source)
    for mods_dir in mods_dirs:  #608 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #609 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #610 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact)  #611 (line in Coconut source)
    for mod_name in couldnt_update:  #612 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #613 (line in Coconut source)



def main():  #616 (line in Coconut source)
    sync_mods.main()  #617 (line in Coconut source)

    update_all([sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR], dry_run="--dry-run" in sys.argv)  #619 (line in Coconut source)

# from coconut import embed
# embed()



if __name__ == "__main__":  #633 (line in Coconut source)
    main()  #634 (line in Coconut source)
