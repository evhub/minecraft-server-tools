#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xea4ed659

# Compiled with Coconut version 3.1.0-post_dev12

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.0-post_dev12', '', True)
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
try:  #8 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #8 (line in Coconut source)
except _coconut.NameError:  #8 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #8 (line in Coconut source)
sys = _coconut_sys  #8 (line in Coconut source)
if sys.version_info >= (3,):  #8 (line in Coconut source)
    from urllib.parse import quote_plus  #8 (line in Coconut source)
else:  #8 (line in Coconut source)
    from urllib import quote_plus  #8 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #8 (line in Coconut source)
    sys = _coconut_sys_0  #8 (line in Coconut source)
from pprint import pprint  #9 (line in Coconut source)

import requests  #11 (line in Coconut source)

from minecraft_server_tools import sync_mods  #13 (line in Coconut source)
from minecraft_server_tools.constants import COMMENT_JSON  #14 (line in Coconut source)
from minecraft_server_tools.constants import MC_VERSION  #14 (line in Coconut source)
from minecraft_server_tools.constants import COMPONENT_SEPS  #14 (line in Coconut source)
from minecraft_server_tools.constants import NON_NAME_COMPONENT_REGEX  #14 (line in Coconut source)
from minecraft_server_tools.constants import NAME_REGEXES_TO_SPACE  #14 (line in Coconut source)
from minecraft_server_tools.constants import SEARCH_URL_TEMPLATE  #14 (line in Coconut source)
from minecraft_server_tools.constants import SECRETS  #14 (line in Coconut source)
from minecraft_server_tools.constants import GOOGLE_QUERY_TEMPLATE  #14 (line in Coconut source)
from minecraft_server_tools.constants import NON_CURSEFORGE_MODS  #14 (line in Coconut source)
from minecraft_server_tools.constants import MODLOADER  #14 (line in Coconut source)
from minecraft_server_tools.constants import WRONG_MODLOADERS  #14 (line in Coconut source)
from minecraft_server_tools.constants import MOD_PAGE_NAME_SUFFIX  #14 (line in Coconut source)
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


BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #45 (line in Coconut source)


@_coconut_tco  #48 (line in Coconut source)
def google(query):  #48 (line in Coconut source)
    print("Sending google search query {_coconut_format_0!r}...".format(_coconut_format_0=(query)))  #49 (line in Coconut source)
    return _coconut_tail_call(((requests.get)(SEARCH_URL_TEMPLATE.format(google_api_key=SECRETS["google_api_key"], search_engine_id=SECRETS["search_engine_id"], query=quote_plus(query)))).json)  #50 (line in Coconut source)



def get_mod_name(jar_name, silent=None):  #61 (line in Coconut source)
    if silent is None:  #62 (line in Coconut source)
        silent = not DEBUG  #63 (line in Coconut source)
    base_name = jar_name.removesuffix(".jar")  #64 (line in Coconut source)
    for sep, min_count in COMPONENT_SEPS:  #65 (line in Coconut source)
        components = base_name.split(sep)  #66 (line in Coconut source)
        if len(components) > min_count:  #67 (line in Coconut source)
            break  #68 (line in Coconut source)
    else:  #69 (line in Coconut source)
        if not silent:  #70 (line in Coconut source)
            print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #71 (line in Coconut source)
        components = [base_name,]  #72 (line in Coconut source)
    name_cmpnts = []  #73 (line in Coconut source)
    for cmpnt in components:  #74 (line in Coconut source)
        is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #75 (line in Coconut source)
        if is_name_cmpnt:  #76 (line in Coconut source)
            name_cmpnts.append(cmpnt)  #77 (line in Coconut source)
        elif name_cmpnts:  #78 (line in Coconut source)
            break  #79 (line in Coconut source)
    if not name_cmpnts:  #80 (line in Coconut source)
        if not silent:  #81 (line in Coconut source)
            print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #82 (line in Coconut source)
        name_cmpnts = [components[0],]  #83 (line in Coconut source)
    mod_name = " ".join(name_cmpnts)  #84 (line in Coconut source)
    for to_space in NAME_REGEXES_TO_SPACE:  #85 (line in Coconut source)
        mod_name = to_space.sub(" ", mod_name)  #86 (line in Coconut source)
    mod_name = mod_name.strip()  #87 (line in Coconut source)
    if not silent:  #88 (line in Coconut source)
        print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #89 (line in Coconut source)
    return mod_name  #90 (line in Coconut source)



def get_curseforge_name(mod_name, jar_name):  #93 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #94 (line in Coconut source)
        return None  #95 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFIX)  #96 (line in Coconut source)
    try:  #104 (line in Coconut source)
        while True:  #105 (line in Coconut source)
            search_json = google(query)  #106 (line in Coconut source)
            if "items" in search_json:  #107 (line in Coconut source)
                break  #108 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #109 (line in Coconut source)
            if search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #110 (line in Coconut source)
                raise Exception("Google API rate limit exceeded; try waiting or switching API keys.")  #111 (line in Coconut source)
            query = search_json["spelling"]["correctedQuery"]  #112 (line in Coconut source)
        items = search_json["items"]  #113 (line in Coconut source)
        curseforge_name = None  #114 (line in Coconut source)
        for result in items:  #115 (line in Coconut source)
            mod_page = result["title"]  #116 (line in Coconut source)
            if mod_page.lower().endswith(MOD_PAGE_NAME_SUFFIX.lower()):  #117 (line in Coconut source)
                curseforge_name = clean_curseforge_name(mod_page[:-len(MOD_PAGE_NAME_SUFFIX)])  #118 (line in Coconut source)
                break  #119 (line in Coconut source)
            else:  #120 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #121 (line in Coconut source)
        if curseforge_name is None:  #122 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #123 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #124 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #125 (line in Coconut source)
        else:  #126 (line in Coconut source)
            print("Found Curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name)))  #127 (line in Coconut source)
            return curseforge_name  #128 (line in Coconut source)
    except (KeyError, IndexError):  #129 (line in Coconut source)
        print("ERROR: Invalid search results for query {_coconut_format_0!r}:".format(_coconut_format_0=(query)))  #130 (line in Coconut source)
        pprint(search_json)  #131 (line in Coconut source)
        raise  #132 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #135 (line in Coconut source)
    old_curseforge_name = None  #136 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #137 (line in Coconut source)
        old_curseforge_name = curseforge_name  #138 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #139 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #140 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #141 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #142 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #143 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #144 (line in Coconut source)
    return curseforge_name  #145 (line in Coconut source)



@_coconut_tco  #148 (line in Coconut source)
def load_curseforge_names():  #148 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #149 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #150 (line in Coconut source)
            return COMMENT_JSON.load(ids_fobj)  #151 (line in Coconut source)
    else:  #152 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #153 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #156 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #157 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #158 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names):  #161 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #162 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #163 (line in Coconut source)
    try:  #164 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #165 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #166 (line in Coconut source)
                curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name])  #167 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #170 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #171 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #172 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #174 (line in Coconut source)
    finally:  #175 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #176 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #179 (line in Coconut source)
    nulled_mods = []  #180 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #181 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #182 (line in Coconut source)
        if curseforge_name is None:  #183 (line in Coconut source)
            nulled_mods.append(mod_name)  #184 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #185 (line in Coconut source)
        else:  #186 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #187 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #188 (line in Coconut source)



def get_jar_names(mods_dir):  #191 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #192 (line in Coconut source)
        if fname.endswith(".jar"):  #193 (line in Coconut source)
            yield fname  #194 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, silent=None):  #197 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #198 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir):  #199 (line in Coconut source)
        mod_name = get_mod_name(jar_name, silent=silent)  #200 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #201 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #202 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #203 (line in Coconut source)
    return mod_names_to_jar_names  #204 (line in Coconut source)



def run_curseforge_api_cmd(cmd):  #207 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #208 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #209 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #210 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #211 (line in Coconut source)
        if cmd_result.stderr:  #212 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #213 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #214 (line in Coconut source)
        else:  #215 (line in Coconut source)
            break  #216 (line in Coconut source)
    else:  #217 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #218 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #219 (line in Coconut source)
    if not api_result:  #220 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #221 (line in Coconut source)
        return []  #222 (line in Coconut source)
    try:  #223 (line in Coconut source)
        return json.loads(api_result)  #224 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #225 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #226 (line in Coconut source)
        print(api_result)  #227 (line in Coconut source)
        raise  #228 (line in Coconut source)



def has_bad_modloader(name):  #231 (line in Coconut source)
    return (MODLOADER.lower() not in name.lower() and any((m.lower() in name.lower() for m in WRONG_MODLOADERS)))  #231 (line in Coconut source)



def get_matching_mod(results, curseforge_name, mod_name):  #237 (line in Coconut source)
    found_mod = None  #238 (line in Coconut source)
    valid_modloader_results = []  #239 (line in Coconut source)
    for mod in results:  #240 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #241 (line in Coconut source)
        if mod["name"] == curseforge_name:  #242 (line in Coconut source)
            if not valid_modloader:  #243 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #244 (line in Coconut source)
            found_mod = mod  #245 (line in Coconut source)
            break  #246 (line in Coconut source)
        if valid_modloader:  #247 (line in Coconut source)
            valid_modloader_results.append(mod)  #248 (line in Coconut source)
    if found_mod is None:  #249 (line in Coconut source)
        for mod in valid_modloader_results:  #250 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #251 (line in Coconut source)
                found_mod = mod  #252 (line in Coconut source)
                break  #253 (line in Coconut source)
    if found_mod is None:  #254 (line in Coconut source)
        for mod in valid_modloader_results:  #255 (line in Coconut source)
            if curseforge_name in mod["name"]:  #256 (line in Coconut source)
                found_mod = mod  #257 (line in Coconut source)
                break  #258 (line in Coconut source)
    if found_mod is None:  #259 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #260 (line in Coconut source)
        for mod in valid_modloader_results:  #261 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #262 (line in Coconut source)
                found_mod = mod  #263 (line in Coconut source)
                break  #264 (line in Coconut source)
    if found_mod is None:  #265 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #266 (line in Coconut source)
        if core_curseforge_name:  #267 (line in Coconut source)
            for mod in valid_modloader_results:  #268 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #269 (line in Coconut source)
                    found_mod = mod  #270 (line in Coconut source)
                    break  #271 (line in Coconut source)
    if found_mod is not None and found_mod["name"] != curseforge_name:  #272 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #273 (line in Coconut source)
    return found_mod  #274 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #277 (line in Coconut source)
    if verbose:  #278 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #279 (line in Coconut source)
    else:  #280 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #281 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #284 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name):  #287 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #288 (line in Coconut source)
    for query_template in CURSEFORGE_QUERY_TEMPLATES:  #289 (line in Coconut source)
        query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #290 (line in Coconut source)

        modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER])  #296 (line in Coconut source)
        mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #297 (line in Coconut source)
        if mod is not None:  #298 (line in Coconut source)
            return mod  #299 (line in Coconut source)
        if DEBUG:  #300 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #301 (line in Coconut source)

        modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER])  #303 (line in Coconut source)
        mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #304 (line in Coconut source)
        if mod is not None:  #305 (line in Coconut source)
            return mod  #306 (line in Coconut source)
        if DEBUG:  #307 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #308 (line in Coconut source)

        version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION)])  #310 (line in Coconut source)
        mod = get_matching_mod(version_results, curseforge_name, mod_name)  #311 (line in Coconut source)
        if mod is not None:  #312 (line in Coconut source)
            return mod  #313 (line in Coconut source)
        if DEBUG:  #314 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #315 (line in Coconut source)

        compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2])])  #317 (line in Coconut source)
        mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #318 (line in Coconut source)
        if mod is not None:  #319 (line in Coconut source)
            return mod  #320 (line in Coconut source)
        if DEBUG:  #321 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #322 (line in Coconut source)

        modloader_results = run_curseforge_api_cmd(["search", query, MODLOADER])  #324 (line in Coconut source)
        mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #325 (line in Coconut source)
        if mod is not None:  #326 (line in Coconut source)
            return mod  #327 (line in Coconut source)
        if DEBUG:  #328 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #329 (line in Coconut source)

        versionless_results = run_curseforge_api_cmd(["search", query])  #331 (line in Coconut source)
        mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #332 (line in Coconut source)
        if mod is not None:  #333 (line in Coconut source)
            return mod  #334 (line in Coconut source)
        if DEBUG:  #335 (line in Coconut source)
            print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #336 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #338 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name):  #341 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name)  #342 (line in Coconut source)
    if mod is not None:  #343 (line in Coconut source)
        return mod["id"]  #344 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names):  #347 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #348 (line in Coconut source)
    missing_mods = []  #349 (line in Coconut source)
    for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #350 (line in Coconut source)
        curseforge_id = get_curseforge_id(curseforge_name, mod_name)  #351 (line in Coconut source)
        if curseforge_id is None:  #352 (line in Coconut source)
            missing_mods.append(mod_name)  #353 (line in Coconut source)
        else:  #354 (line in Coconut source)
            mod_names_to_curseforge_ids[mod_name] = curseforge_id  #355 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #356 (line in Coconut source)



@_coconut_tco  #359 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #359 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #360 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #363 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #364 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #365 (line in Coconut source)
    if match_results is None:  #366 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #367 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #368 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #369 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #374 (line in Coconut source)
    return parsed_time  #375 (line in Coconut source)



@_coconut_tco  #378 (line in Coconut source)
def timestamp_sort(curseforge_files):  #378 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #378 (line in Coconut source)



@_coconut_tco  #385 (line in Coconut source)
def get_max_version(versions):  #385 (line in Coconut source)
    ver_tuples = []  #386 (line in Coconut source)
    for ver_str in versions:  #387 (line in Coconut source)
        try:  #388 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #389 (line in Coconut source)
        except ValueError:  #390 (line in Coconut source)
            pass  #391 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #392 (line in Coconut source)



@_coconut_tco  #395 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #395 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #395 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #409 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #410 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #413 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #414 (line in Coconut source)
    if url is None:  #415 (line in Coconut source)
        return None  #416 (line in Coconut source)
    else:  #417 (line in Coconut source)
        return url.rsplit("/", 1)[-1]  #418 (line in Coconut source)



def correct_modloader(versions, jar_name):  #421 (line in Coconut source)
    versions = [v.lower() for v in versions]  #422 (line in Coconut source)

    if MODLOADER.lower() in versions:  #424 (line in Coconut source)
        return True  #425 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #426 (line in Coconut source)
        return False  #427 (line in Coconut source)

    jar_name = jar_name.lower()  #429 (line in Coconut source)
    if MODLOADER.lower() in jar_name:  #430 (line in Coconut source)
        return True  #431 (line in Coconut source)
    if any((wrong_modloader.lower() in jar_name for wrong_modloader in WRONG_MODLOADERS)):  #432 (line in Coconut source)
        return False  #433 (line in Coconut source)

    return True  #435 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #438 (line in Coconut source)
    for file_data in curseforge_files:  #439 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #440 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #441 (line in Coconut source)
            return file_data  #442 (line in Coconut source)
    return None  #443 (line in Coconut source)



@_coconut_tco  #446 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name):  #446 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #447 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #449 (line in Coconut source)
    if old_curseforge_file is None:  #450 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #451 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #452 (line in Coconut source)

    curseforge_files_and_versions = []  #454 (line in Coconut source)
    for file_data in curseforge_files:  #455 (line in Coconut source)
        versions = file_data["gameVersions"]  #456 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #457 (line in Coconut source)
        if (jar_name is not None and correct_modloader(versions, jar_name) and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #458 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #463 (line in Coconut source)

    correctly_versioned_files = []  #465 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #466 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #467 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #468 (line in Coconut source)
    if correctly_versioned_files:  #469 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #470 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #471 (line in Coconut source)

    compatibly_versioned_files = []  #473 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #474 (line in Coconut source)
        for raw_ver in versions:  #475 (line in Coconut source)
            try:  #476 (line in Coconut source)
                ver = ver_split(raw_ver)  #477 (line in Coconut source)
            except ValueError:  #478 (line in Coconut source)
                pass  #479 (line in Coconut source)
            else:  #480 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #481 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #482 (line in Coconut source)
    if compatibly_versioned_files:  #483 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #484 (line in Coconut source)

    maybe_compatible_files = []  #486 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #487 (line in Coconut source)
        for ver in versions:  #488 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #489 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #490 (line in Coconut source)
                break  #491 (line in Coconut source)
    if maybe_compatible_files:  #492 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #493 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #494 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #495 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #498 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #499 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names):  #502 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #503 (line in Coconut source)
    missing_mods = []  #504 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #505 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #506 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name)  #507 (line in Coconut source)
        if latest_version is None:  #508 (line in Coconut source)
            missing_mods.append(mod_name)  #509 (line in Coconut source)
        else:  #510 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #511 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #512 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #515 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #516 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #517 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #518 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #519 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #520 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #521 (line in Coconut source)
    return updated_mod_names_to_files  #522 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #525 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #526 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #527 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #528 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #529 (line in Coconut source)
    if os.path.exists(new_jar_path):  #530 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #531 (line in Coconut source)
    else:  #532 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #533 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #534 (line in Coconut source)
        if new_mod_name != mod_name:  #535 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #536 (line in Coconut source)
        result = requests.get(url)  #537 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #538 (line in Coconut source)
            jar_fobj.write(result.content)  #539 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #542 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #543 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #544 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #545 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #546 (line in Coconut source)
        if jar_name in seen_jar_names:  #547 (line in Coconut source)
            print("\tWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #548 (line in Coconut source)
        else:  #549 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #550 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #551 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #554 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #555 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #556 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #557 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #558 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #559 (line in Coconut source)



def make_dirs(*dirs):  #562 (line in Coconut source)
    for d in dirs:  #563 (line in Coconut source)
        if not os.path.exists(d):  #564 (line in Coconut source)
            os.mkdir(d)  #565 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None):  #568 (line in Coconut source)
    if interact is None and not DEBUG:  #569 (line in Coconut source)
        interact = False  #570 (line in Coconut source)
    try:  #571 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir)  #572 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names)  #573 (line in Coconut source)
        if not dry_run:  #574 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names)  #575 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names)  #576 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #577 (line in Coconut source)
            if updated_mod_names_to_files:  #578 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #579 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #580 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #581 (line in Coconut source)
        else:  #582 (line in Coconut source)
            missing_ids_mods = []  #583 (line in Coconut source)
            missing_files_mods = []  #584 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #585 (line in Coconut source)
    except Exception:  #586 (line in Coconut source)
        if interact is not False:  #587 (line in Coconut source)
            traceback.print_exc()  #588 (line in Coconut source)

            from coconut import embed  #590 (line in Coconut source)
            embed()  #591 (line in Coconut source)
        raise  #592 (line in Coconut source)
    if interact:  #593 (line in Coconut source)
        from coconut import embed  #594 (line in Coconut source)
        embed()  #595 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None):  #598 (line in Coconut source)
    couldnt_update = []  #599 (line in Coconut source)
    for mods_dir in mods_dirs:  #600 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #601 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #602 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact)  #603 (line in Coconut source)
    for mod_name in couldnt_update:  #604 (line in Coconut source)
        print("Unable to automatically update mod: {_coconut_format_0}".format(_coconut_format_0=(mod_name)))  #605 (line in Coconut source)



def main():  #608 (line in Coconut source)
    sync_mods.main()  #609 (line in Coconut source)

    update_all([sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR], dry_run="--dry-run" in sys.argv)  #611 (line in Coconut source)

# from coconut import embed
# embed()



if __name__ == "__main__":  #625 (line in Coconut source)
    main()  #626 (line in Coconut source)
