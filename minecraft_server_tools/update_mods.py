#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x34ac9e86

# Compiled with Coconut version 3.2.0-post_dev1

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.2.0-post_dev1', '', True)
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
from collections import namedtuple  #11 (line in Coconut source)

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
from minecraft_server_tools.constants import CURSEFORGE_CLASS_ID_MODS  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_CLASS_ID_DATAPACKS  #22 (line in Coconut source)
from minecraft_server_tools.constants import CURSEFORGE_CLASS_ID_RESOURCE_PACKS  #22 (line in Coconut source)
from minecraft_server_tools.constants import DATAPACK_FOLDER_PATHS  #22 (line in Coconut source)
from minecraft_server_tools.constants import ver_join  #22 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #22 (line in Coconut source)


UPDATE_MODS_DIRS = [sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR]  #60 (line in Coconut source)

UPDATE_DATAPACK_DIRS = DATAPACK_FOLDER_PATHS  #67 (line in Coconut source)

BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #69 (line in Coconut source)

# Configuration for different content types (mods vs datapacks)
ContentTypeConfig = namedtuple('ContentTypeConfig', ['name', 'file_extension', 'curseforge_class_ids', 'use_modloader'])  # "mod" or "datapack"  # whether to filter by modloader  # list of CurseForge classIds to search  # ".jar" or ".zip"  #72 (line in Coconut source)

MOD_CONFIG = ContentTypeConfig(name="mod", file_extension=".jar", curseforge_class_ids=[CURSEFORGE_CLASS_ID_MODS,], use_modloader=True)  #79 (line in Coconut source)

DATAPACK_CONFIG = ContentTypeConfig(name="datapack", file_extension=".zip", curseforge_class_ids=[CURSEFORGE_CLASS_ID_DATAPACKS, CURSEFORGE_CLASS_ID_RESOURCE_PACKS], use_modloader=False)  #86 (line in Coconut source)


class MissingCurseforgeNameError(KeyError):  #94 (line in Coconut source)
    """Exception raised when a CurseForge name mapping is missing."""  #95 (line in Coconut source)
    def __init__(self, mod_name, query):  #96 (line in Coconut source)
        self.mod_name = mod_name  #97 (line in Coconut source)
        self.query = query  #98 (line in Coconut source)
        __class__ = MissingCurseforgeNameError  #99 (line in Coconut source)

        super().__init__("No Curseforge name for mod {_coconut_format_0!r}; expecting Claude to search for it and add it to curseforge_names.json (suggested search query: {_coconut_format_1!r}).".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #99 (line in Coconut source)



_coconut_call_set_names(MissingCurseforgeNameError)  #102 (line in Coconut source)
@_coconut_tco  #102 (line in Coconut source)
def get_mod_name(jar_name, silent=None, do_component_splitting=True, use_all_components=False, file_extension=".jar"):  #102 (line in Coconut source)
    def _coconut_mock_0(jar_name, silent=_coconut_sentinel, do_component_splitting=_coconut_sentinel, use_all_components=_coconut_sentinel, file_extension=_coconut_sentinel):  #103 (line in Coconut source)
        if silent is _coconut_sentinel: silent = _coconut_recursive_func_0._coconut_tco_func.__defaults__[0]  #103 (line in Coconut source)
        if do_component_splitting is _coconut_sentinel: do_component_splitting = _coconut_recursive_func_0._coconut_tco_func.__defaults__[1]  #103 (line in Coconut source)
        if use_all_components is _coconut_sentinel: use_all_components = _coconut_recursive_func_0._coconut_tco_func.__defaults__[2]  #103 (line in Coconut source)
        if file_extension is _coconut_sentinel: file_extension = _coconut_recursive_func_0._coconut_tco_func.__defaults__[3]  #103 (line in Coconut source)
        return (jar_name, silent, do_component_splitting, use_all_components, file_extension,)  #103 (line in Coconut source)
    while True:  #103 (line in Coconut source)
        if silent is None:  #103 (line in Coconut source)
            silent = not PRINT_DEBUG  #104 (line in Coconut source)

        base_name = jar_name.removesuffix(file_extension)  #106 (line in Coconut source)

        if do_component_splitting:  #108 (line in Coconut source)
            for sep, min_count in COMPONENT_SEPS:  #109 (line in Coconut source)
                components = base_name.split(sep)  #110 (line in Coconut source)
                if len(components) > min_count:  #111 (line in Coconut source)
                    break  #112 (line in Coconut source)
            else:  #113 (line in Coconut source)
                if not silent:  #114 (line in Coconut source)
                    print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #115 (line in Coconut source)
                components = [base_name,]  #116 (line in Coconut source)

            name_cmpnts = []  #118 (line in Coconut source)
            for cmpnt in components:  #119 (line in Coconut source)
                is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #120 (line in Coconut source)
                if is_name_cmpnt:  #121 (line in Coconut source)
                    name_cmpnts.append(cmpnt)  #122 (line in Coconut source)
                elif name_cmpnts and not use_all_components:  #123 (line in Coconut source)
                    break  #124 (line in Coconut source)
            if not name_cmpnts:  #125 (line in Coconut source)
                if not silent:  #126 (line in Coconut source)
                    print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #127 (line in Coconut source)
                name_cmpnts = [components[0],]  #128 (line in Coconut source)
            mod_name = " ".join(name_cmpnts)  #129 (line in Coconut source)
        else:  #130 (line in Coconut source)
            mod_name = base_name  #131 (line in Coconut source)

        for to_space in NAME_REGEXES_TO_SPACE:  #133 (line in Coconut source)
            mod_name = to_space.sub(" ", mod_name)  #134 (line in Coconut source)

        if not mod_name:  #136 (line in Coconut source)
            if not silent:  #137 (line in Coconut source)
                print("Got empty mod name for jar {_coconut_format_0!r}; falling back to no component splitting.".format(_coconut_format_0=(jar_name)))  #138 (line in Coconut source)
            try:  #139 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #139 (line in Coconut source)
            except _coconut.NameError:  #139 (line in Coconut source)
                _coconut_tre_check_0 = False  #139 (line in Coconut source)
            if _coconut_tre_check_0:  #139 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components, file_extension,) = _coconut_mock_0(jar_name, do_component_splitting=False, file_extension=file_extension)  #139 (line in Coconut source)
                continue  #139 (line in Coconut source)
            else:  #139 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False, file_extension=file_extension)  #139 (line in Coconut source)


        camel_case_parts = [mod_name[0],]  #141 (line in Coconut source)
        prev_is_lower = mod_name[0].islower()  #142 (line in Coconut source)
        for c in mod_name[1:]:  #143 (line in Coconut source)
            if prev_is_lower and c.isupper():  #144 (line in Coconut source)
                camel_case_parts.append("")  #145 (line in Coconut source)
            camel_case_parts[-1] += c  #146 (line in Coconut source)
            prev_is_lower = c.islower()  #147 (line in Coconut source)

        mod_name = " ".join(camel_case_parts)  #149 (line in Coconut source)
        while "  " in mod_name:  #150 (line in Coconut source)
            mod_name = mod_name.replace("  ", " ")  #151 (line in Coconut source)

        mod_name = mod_name.strip().lower()  #153 (line in Coconut source)

        if mod_name in NO_COMPONENT_SPLIT_MODS:  #155 (line in Coconut source)
            if not silent:  #156 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as no component splitting; redoing without component splitting.".format(_coconut_format_0=(mod_name)))  #157 (line in Coconut source)
            try:  #158 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #158 (line in Coconut source)
            except _coconut.NameError:  #158 (line in Coconut source)
                _coconut_tre_check_0 = False  #158 (line in Coconut source)
            if _coconut_tre_check_0:  #158 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components, file_extension,) = _coconut_mock_0(jar_name, do_component_splitting=False, file_extension=file_extension)  #158 (line in Coconut source)
                continue  #158 (line in Coconut source)
            else:  #158 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False, file_extension=file_extension)  #158 (line in Coconut source)


        if mod_name in USE_ALL_COMPONENTS_MODS and not use_all_components:  #160 (line in Coconut source)
            if not silent:  #161 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as use all components; redoing with all components.".format(_coconut_format_0=(mod_name)))  #162 (line in Coconut source)
            try:  #163 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #163 (line in Coconut source)
            except _coconut.NameError:  #163 (line in Coconut source)
                _coconut_tre_check_0 = False  #163 (line in Coconut source)
            if _coconut_tre_check_0:  #163 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components, file_extension,) = _coconut_mock_0(jar_name, use_all_components=True, file_extension=file_extension)  #163 (line in Coconut source)
                continue  #163 (line in Coconut source)
            else:  #163 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, use_all_components=True, file_extension=file_extension)  #163 (line in Coconut source)


        if not silent:  #165 (line in Coconut source)
            print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #166 (line in Coconut source)
        return mod_name  #169 (line in Coconut source)
    return None  #170 (line in Coconut source)

_coconut_recursive_func_0 = get_mod_name  #170 (line in Coconut source)

def get_curseforge_name(mod_name, jar_name, google=False):  #170 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #171 (line in Coconut source)
        return None  #172 (line in Coconut source)
    query = GOOGLE_QUERY_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #173 (line in Coconut source)
    if not google:  #181 (line in Coconut source)
        raise MissingCurseforgeNameError(mod_name, query)  #182 (line in Coconut source)
    try:  #183 (line in Coconut source)
        while True:  #184 (line in Coconut source)
            search_json = google_api.google(query)  #185 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #186 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #187 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #188 (line in Coconut source)
                break  #189 (line in Coconut source)
            if "items" in search_json:  #190 (line in Coconut source)
                break  #191 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #192 (line in Coconut source)
            if "spelling" in search_json:  #193 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #194 (line in Coconut source)
                continue  #195 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #196 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #197 (line in Coconut source)
            break  #198 (line in Coconut source)
        items = search_json["items"]  #199 (line in Coconut source)
        curseforge_name = None  #200 (line in Coconut source)
        for result in items:  #201 (line in Coconut source)
            mod_page = result["title"]  #202 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #203 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #204 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #205 (line in Coconut source)
                    break  #206 (line in Coconut source)
            if curseforge_name is not None:  #207 (line in Coconut source)
                break  #208 (line in Coconut source)
            else:  #209 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #210 (line in Coconut source)
        if curseforge_name is None:  #211 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #212 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #213 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #214 (line in Coconut source)
        else:  #215 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #216 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #217 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #218 (line in Coconut source)
        if mod is None:  #219 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #220 (line in Coconut source)
        else:  #221 (line in Coconut source)
            return mod["name"]  #222 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #223 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #224 (line in Coconut source)
        pprint(search_json)  #225 (line in Coconut source)
        raise  #226 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #229 (line in Coconut source)
    old_curseforge_name = None  #230 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #231 (line in Coconut source)
        old_curseforge_name = curseforge_name  #232 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #233 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #234 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #235 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #236 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #237 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #238 (line in Coconut source)
    return curseforge_name  #239 (line in Coconut source)



@_coconut_tco  #242 (line in Coconut source)
def load_curseforge_names():  #242 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #243 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #244 (line in Coconut source)
            curseforge_names = COMMENT_JSON.load(ids_fobj)  #245 (line in Coconut source)
            if FIX_MOD_NAMES:  #246 (line in Coconut source)
                curseforge_names = _coconut.dict(((get_mod_name(mod_name)), (curseforge_name)) for mod_name, curseforge_name in curseforge_names.items())  #247 (line in Coconut source)
            return curseforge_names  #248 (line in Coconut source)
    else:  #249 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #250 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #253 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #254 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #255 (line in Coconut source)



@_coconut_tco  #258 (line in Coconut source)
def load_curseforge_ids_cache():  #258 (line in Coconut source)
    """Load the cached curseforge_name -> curseforge_id mappings."""  #259 (line in Coconut source)
    if os.path.exists(CURSEFORGE_IDS_CACHE_FILE):  #260 (line in Coconut source)
        with open(CURSEFORGE_IDS_CACHE_FILE, "r") as cache_fobj:  #261 (line in Coconut source)
            return json.load(cache_fobj)  #262 (line in Coconut source)
    else:  #263 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #264 (line in Coconut source)



def save_curseforge_ids_cache(curseforge_ids_cache):  #267 (line in Coconut source)
    """Save the curseforge_name -> curseforge_id cache."""  #268 (line in Coconut source)
    with open(CURSEFORGE_IDS_CACHE_FILE, "w") as cache_fobj:  #269 (line in Coconut source)
        json.dump(curseforge_ids_cache, cache_fobj, indent=4)  #270 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names, google=False):  #273 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #274 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #275 (line in Coconut source)
    missing_curseforge_names = []  # collect all missing names first  #276 (line in Coconut source)
    try:  #277 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #278 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #279 (line in Coconut source)
                try:  #280 (line in Coconut source)
                    curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name], google=google)  #281 (line in Coconut source)
                except MissingCurseforgeNameError as e:  #282 (line in Coconut source)
                    missing_curseforge_names.append((e.mod_name, e.query))  #283 (line in Coconut source)
                    continue  #284 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #287 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #288 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #289 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #291 (line in Coconut source)
    finally:  #292 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #293 (line in Coconut source)

# raise error with all missing names at once
    if missing_curseforge_names:  #296 (line in Coconut source)
        print("\n{_coconut_format_0}".format(_coconut_format_0=('=' * 60)))  #297 (line in Coconut source)
        print("MISSING CURSEFORGE NAME MAPPINGS:")  #298 (line in Coconut source)
        print("{_coconut_format_0}\n".format(_coconut_format_0=('=' * 60)))  #299 (line in Coconut source)
        for mod_name, query in missing_curseforge_names:  #300 (line in Coconut source)
            print("{_coconut_format_0!r}".format(_coconut_format_0=(mod_name)))  #301 (line in Coconut source)
            print("\tSuggested search query: {_coconut_format_0!r}\n".format(_coconut_format_0=(query)))  #302 (line in Coconut source)
        print("{_coconut_format_0}\n".format(_coconut_format_0=('=' * 60)))  #303 (line in Coconut source)
        raise KeyError("Missing {_coconut_format_0} Curseforge name mappings; expecting Claude to search for them and add them to curseforge_names.json.".format(_coconut_format_0=(len(missing_curseforge_names))))  #304 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #307 (line in Coconut source)
    nulled_mods = []  #308 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #309 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #310 (line in Coconut source)
        if curseforge_name is None:  #311 (line in Coconut source)
            nulled_mods.append(mod_name)  #312 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #313 (line in Coconut source)
        else:  #314 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #315 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #316 (line in Coconut source)



def get_jar_names(mods_dir, file_extension=".jar"):  #319 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #320 (line in Coconut source)
        if fname.endswith(file_extension):  #321 (line in Coconut source)
            yield fname  #322 (line in Coconut source)



def get_mod_names_to_all_jar_names(mods_dir, file_extension=".jar", **kwargs):  #325 (line in Coconut source)
    mod_names_to_all_jar_names = defaultdict(list)  #326 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir, file_extension=file_extension):  #327 (line in Coconut source)
        mod_name = get_mod_name(jar_name, file_extension=file_extension, **kwargs)  #328 (line in Coconut source)
        mod_names_to_all_jar_names[mod_name] += [jar_name,]  #329 (line in Coconut source)
    return mod_names_to_all_jar_names  #330 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, file_extension=".jar", **kwargs):  #333 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #334 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir, file_extension=file_extension):  #335 (line in Coconut source)
        mod_name = get_mod_name(jar_name, file_extension=file_extension, **kwargs)  #336 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #337 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #338 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #339 (line in Coconut source)
    return mod_names_to_jar_names  #340 (line in Coconut source)



def run_curseforge_api_cmd(cmd, class_id=None):  #343 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #344 (line in Coconut source)
    if class_id is not None:  #345 (line in Coconut source)
        cmd.append(str(class_id))  #346 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #347 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #348 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #349 (line in Coconut source)
        if cmd_result.stderr:  #350 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #351 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #352 (line in Coconut source)
        else:  #353 (line in Coconut source)
            break  #354 (line in Coconut source)
    else:  #355 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #356 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #357 (line in Coconut source)
    if not api_result:  #358 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #359 (line in Coconut source)
        return []  #360 (line in Coconut source)
    try:  #361 (line in Coconut source)
        return json.loads(api_result)  #362 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #363 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #364 (line in Coconut source)
        print(api_result)  #365 (line in Coconut source)
        raise  #366 (line in Coconut source)



def has_bad_modloader(name):  #369 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS)):  #370 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #371 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS + MAYBE_WRONG_MODLOADERS:  #372 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #373 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #374 (line in Coconut source)
    return False  #375 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #377 (line in Coconut source)
    found_mod = None  #378 (line in Coconut source)
    valid_modloader_results = []  #379 (line in Coconut source)
    for mod in results:  #380 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #381 (line in Coconut source)
        if mod["name"] == curseforge_name:  #382 (line in Coconut source)
            if not valid_modloader:  #383 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #384 (line in Coconut source)
            found_mod = mod  #385 (line in Coconut source)
            break  #386 (line in Coconut source)
        if valid_modloader:  #387 (line in Coconut source)
            valid_modloader_results.append(mod)  #388 (line in Coconut source)
    if found_mod is None:  #389 (line in Coconut source)
        for mod in valid_modloader_results:  #390 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #391 (line in Coconut source)
                found_mod = mod  #392 (line in Coconut source)
                break  #393 (line in Coconut source)
    if found_mod is None:  #394 (line in Coconut source)
        for mod in valid_modloader_results:  #395 (line in Coconut source)
            if curseforge_name in mod["name"]:  #396 (line in Coconut source)
                found_mod = mod  #397 (line in Coconut source)
                break  #398 (line in Coconut source)
    if found_mod is None:  #399 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #400 (line in Coconut source)
        for mod in valid_modloader_results:  #401 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #402 (line in Coconut source)
                found_mod = mod  #403 (line in Coconut source)
                break  #404 (line in Coconut source)
    if found_mod is None:  #405 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #406 (line in Coconut source)
        if core_curseforge_name:  #407 (line in Coconut source)
            for mod in valid_modloader_results:  #408 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #409 (line in Coconut source)
                    found_mod = mod  #410 (line in Coconut source)
                    break  #411 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #412 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #413 (line in Coconut source)
    return found_mod  #414 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #417 (line in Coconut source)
    if verbose:  #418 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #419 (line in Coconut source)
    else:  #420 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #421 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #424 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name, config=None):  #427 (line in Coconut source)
    if config is None:  #428 (line in Coconut source)
        config = MOD_CONFIG  #429 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #430 (line in Coconut source)

# Try each classId in the config
    for class_id in config.curseforge_class_ids:  #433 (line in Coconut source)
        seen_queries = set()  #434 (line in Coconut source)
        for query_template in CURSEFORGE_QUERY_TEMPLATES:  #435 (line in Coconut source)
            query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #436 (line in Coconut source)
            if query in seen_queries:  #441 (line in Coconut source)
                continue  #442 (line in Coconut source)
            seen_queries.add(query)  #443 (line in Coconut source)

            if config.use_modloader:  #445 (line in Coconut source)
                modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER], class_id=class_id)  #446 (line in Coconut source)
                mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #447 (line in Coconut source)
                if mod is not None:  #448 (line in Coconut source)
                    return mod  #449 (line in Coconut source)
                if PRINT_DEBUG:  #450 (line in Coconut source)
                    print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #451 (line in Coconut source)

                modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER], class_id=class_id)  #453 (line in Coconut source)
                mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #454 (line in Coconut source)
                if mod is not None:  #455 (line in Coconut source)
                    return mod  #456 (line in Coconut source)
                if PRINT_DEBUG:  #457 (line in Coconut source)
                    print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #458 (line in Coconut source)

            version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), ""], class_id=class_id)  #460 (line in Coconut source)
            mod = get_matching_mod(version_results, curseforge_name, mod_name)  #461 (line in Coconut source)
            if mod is not None:  #462 (line in Coconut source)
                return mod  #463 (line in Coconut source)
            if PRINT_DEBUG:  #464 (line in Coconut source)
                print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #465 (line in Coconut source)

            compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), ""], class_id=class_id)  #467 (line in Coconut source)
            mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #468 (line in Coconut source)
            if mod is not None:  #469 (line in Coconut source)
                return mod  #470 (line in Coconut source)
            if PRINT_DEBUG:  #471 (line in Coconut source)
                print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #472 (line in Coconut source)

            if config.use_modloader:  #474 (line in Coconut source)
                modloader_results = run_curseforge_api_cmd(["search", query, "", MODLOADER], class_id=class_id)  #475 (line in Coconut source)
                mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #476 (line in Coconut source)
                if mod is not None:  #477 (line in Coconut source)
                    return mod  #478 (line in Coconut source)
                if PRINT_DEBUG:  #479 (line in Coconut source)
                    print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #480 (line in Coconut source)

            versionless_results = run_curseforge_api_cmd(["search", query, "", ""], class_id=class_id)  #482 (line in Coconut source)
            mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #483 (line in Coconut source)
            if mod is not None:  #484 (line in Coconut source)
                return mod  #485 (line in Coconut source)
            if PRINT_DEBUG:  #486 (line in Coconut source)
                print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #487 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #489 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name, config=None):  #492 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name, config=config)  #493 (line in Coconut source)
    if mod is not None:  #494 (line in Coconut source)
        return mod["id"]  #495 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names, config=None):  #498 (line in Coconut source)
    curseforge_ids_cache = load_curseforge_ids_cache()  #499 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #500 (line in Coconut source)
    missing_mods = []  #501 (line in Coconut source)
    try:  #502 (line in Coconut source)
        for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #503 (line in Coconut source)
# Check cache first
            if curseforge_name in curseforge_ids_cache:  #505 (line in Coconut source)
                curseforge_id = curseforge_ids_cache[curseforge_name]  #506 (line in Coconut source)
                print("Using cached CurseForge ID for {_coconut_format_0!r}.".format(_coconut_format_0=(curseforge_name)))  #507 (line in Coconut source)
            else:  #508 (line in Coconut source)
                curseforge_id = get_curseforge_id(curseforge_name, mod_name, config=config)  #509 (line in Coconut source)
                if curseforge_id is not None:  #510 (line in Coconut source)
                    curseforge_ids_cache[curseforge_name] = curseforge_id  #511 (line in Coconut source)

            if curseforge_id is None:  #513 (line in Coconut source)
                missing_mods.append(mod_name)  #514 (line in Coconut source)
            else:  #515 (line in Coconut source)
                mod_names_to_curseforge_ids[mod_name] = curseforge_id  #516 (line in Coconut source)
    finally:  #517 (line in Coconut source)
        save_curseforge_ids_cache(curseforge_ids_cache)  #518 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #519 (line in Coconut source)



@_coconut_tco  #522 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #522 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #523 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #526 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #527 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #528 (line in Coconut source)
    if match_results is None:  #529 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #530 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #531 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #532 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #537 (line in Coconut source)
    return parsed_time  #538 (line in Coconut source)



@_coconut_tco  #541 (line in Coconut source)
def timestamp_sort(curseforge_files):  #541 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #541 (line in Coconut source)



@_coconut_tco  #548 (line in Coconut source)
def get_max_version(versions):  #548 (line in Coconut source)
    ver_tuples = []  #549 (line in Coconut source)
    for ver_str in versions:  #550 (line in Coconut source)
        try:  #551 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #552 (line in Coconut source)
        except ValueError:  #553 (line in Coconut source)
            pass  #554 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #555 (line in Coconut source)



@_coconut_tco  #558 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #558 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #558 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #572 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #573 (line in Coconut source)



@_coconut_tco  #576 (line in Coconut source)
def reconstruct_curseforge_download_url(curseforge_file):  #576 (line in Coconut source)
    """Reconstruct download URL from file ID when downloadUrl is None."""  #577 (line in Coconut source)
    file_id = curseforge_file["id"]  #578 (line in Coconut source)
    filename = curseforge_file["fileName"]  #579 (line in Coconut source)
    first_part = file_id // 1000  #580 (line in Coconut source)
    second_part = file_id % 1000  #581 (line in Coconut source)
    return _coconut_tail_call("https://edge.forgecdn.net/files/{_coconut_format_0}/{_coconut_format_1}/{_coconut_format_2}".format, _coconut_format_0=(first_part), _coconut_format_1=(second_part), _coconut_format_2=(filename))  #582 (line in Coconut source)



@_coconut_tco  #585 (line in Coconut source)
def get_curseforge_download_url(curseforge_file):  #585 (line in Coconut source)
    """Get download URL, reconstructing it if necessary."""  #586 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #587 (line in Coconut source)
    if url is None:  #588 (line in Coconut source)
        return _coconut_tail_call(reconstruct_curseforge_download_url, curseforge_file)  #589 (line in Coconut source)
    return url  #590 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #593 (line in Coconut source)
    return (((get_curseforge_download_url(curseforge_file)).rsplit("/", 1))[-1])  #593 (line in Coconut source)



def correct_modloader(versions, jar_name):  #600 (line in Coconut source)
    versions = [v.lower() for v in versions]  #601 (line in Coconut source)

    if MODLOADER.lower() in versions:  #603 (line in Coconut source)
        return True  #604 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #605 (line in Coconut source)
        return False  #606 (line in Coconut source)

    jar_name = jar_name.lower()  #608 (line in Coconut source)
    if has_bad_modloader(jar_name):  #609 (line in Coconut source)
        return False  #610 (line in Coconut source)

    return True  #612 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #615 (line in Coconut source)
    for file_data in curseforge_files:  #616 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #617 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #618 (line in Coconut source)
            return file_data  #619 (line in Coconut source)
    return None  #620 (line in Coconut source)



@_coconut_tco  #623 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name, config=None):  #623 (line in Coconut source)
    if config is None:  #624 (line in Coconut source)
        config = MOD_CONFIG  #625 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #626 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #628 (line in Coconut source)
    if old_curseforge_file is None:  #629 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #630 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #631 (line in Coconut source)

    curseforge_files_and_versions = []  #633 (line in Coconut source)
    for file_data in curseforge_files:  #634 (line in Coconut source)
        versions = file_data["gameVersions"]  #635 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #636 (line in Coconut source)
# Check modloader only if config requires it
        modloader_ok = correct_modloader(versions, jar_name) if config.use_modloader else True  #638 (line in Coconut source)
        if (jar_name is not None and jar_name.endswith(config.file_extension) and modloader_ok and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #639 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #645 (line in Coconut source)

    correctly_versioned_files = []  #647 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #648 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #649 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #650 (line in Coconut source)
    if correctly_versioned_files:  #651 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #652 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #653 (line in Coconut source)

    compatibly_versioned_files = []  #655 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #656 (line in Coconut source)
        for raw_ver in versions:  #657 (line in Coconut source)
            try:  #658 (line in Coconut source)
                ver = ver_split(raw_ver)  #659 (line in Coconut source)
            except ValueError:  #660 (line in Coconut source)
                pass  #661 (line in Coconut source)
            else:  #662 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #663 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #664 (line in Coconut source)
    if compatibly_versioned_files:  #665 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #666 (line in Coconut source)

    maybe_compatible_files = []  #668 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #669 (line in Coconut source)
        for ver in versions:  #670 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #671 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #672 (line in Coconut source)
                break  #673 (line in Coconut source)
    if maybe_compatible_files:  #674 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #675 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #676 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #677 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #680 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #681 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names, config=None):  #684 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #685 (line in Coconut source)
    missing_mods = []  #686 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #687 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #688 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name, config=config)  #689 (line in Coconut source)
        if latest_version is None:  #690 (line in Coconut source)
            missing_mods.append(mod_name)  #691 (line in Coconut source)
        else:  #692 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #693 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #694 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #697 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #698 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #699 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #700 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #701 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #702 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #703 (line in Coconut source)
    return updated_mod_names_to_files  #704 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #707 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #708 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #709 (line in Coconut source)
    url = get_curseforge_download_url(curseforge_file)  #710 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #711 (line in Coconut source)
    if os.path.exists(new_jar_path):  #712 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #713 (line in Coconut source)
    else:  #714 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #715 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #716 (line in Coconut source)
        if new_mod_name != mod_name:  #717 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #718 (line in Coconut source)
        result = requests.get(url)  #719 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #720 (line in Coconut source)
            jar_fobj.write(result.content)  #721 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #724 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #725 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #726 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #727 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #728 (line in Coconut source)
        if jar_name in seen_jar_names:  #729 (line in Coconut source)
            print("\nWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}\n".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #730 (line in Coconut source)
        else:  #731 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #732 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #733 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #736 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #737 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #738 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #739 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #740 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #741 (line in Coconut source)



def make_dirs(*dirs):  #744 (line in Coconut source)
    for d in dirs:  #745 (line in Coconut source)
        if not os.path.exists(d):  #746 (line in Coconut source)
            os.mkdir(d)  #747 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None, google=False, config=None):  #750 (line in Coconut source)
    if config is None:  #751 (line in Coconut source)
        config = MOD_CONFIG  #752 (line in Coconut source)
    if interact is None and not PRINT_DEBUG:  #753 (line in Coconut source)
        interact = False  #754 (line in Coconut source)
    try:  #755 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir, file_extension=config.file_extension)  #756 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names, google=google)  #757 (line in Coconut source)
        if not dry_run:  #758 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names, config=config)  #759 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names, config=config)  #760 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #761 (line in Coconut source)
            if updated_mod_names_to_files:  #762 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #763 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #764 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #765 (line in Coconut source)
        else:  #766 (line in Coconut source)
            missing_ids_mods = []  #767 (line in Coconut source)
            missing_files_mods = []  #768 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #769 (line in Coconut source)
    except Exception:  #770 (line in Coconut source)
        if interact is not False:  #771 (line in Coconut source)
            traceback.print_exc()  #772 (line in Coconut source)

            from coconut import embed  #774 (line in Coconut source)
            embed()  #775 (line in Coconut source)
        raise  #776 (line in Coconut source)
    if interact:  #777 (line in Coconut source)
        from coconut import embed  #778 (line in Coconut source)
        embed()  #779 (line in Coconut source)



def update_all(mods_dirs, dry_run=False, interact=None, google=False, config=None):  #782 (line in Coconut source)
    couldnt_update = []  #783 (line in Coconut source)
    for mods_dir in mods_dirs:  #784 (line in Coconut source)
        if not os.path.exists(mods_dir):  #785 (line in Coconut source)
            print("Skipping non-existent directory: {_coconut_format_0}".format(_coconut_format_0=(mods_dir)))  #786 (line in Coconut source)
            continue  #787 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #788 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #789 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=dry_run, interact=interact, google=google, config=config)  #790 (line in Coconut source)
    config_name = config.name if config is not None else "mod"  #791 (line in Coconut source)
    for mod_name in couldnt_update:  #792 (line in Coconut source)
        print("Unable to automatically update {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(config_name), _coconut_format_1=(mod_name)))  #793 (line in Coconut source)



@_coconut_tco  #796 (line in Coconut source)
def parse_args():  #796 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Update mods and datapacks from CurseForge to their latest versions.")  #797 (line in Coconut source)
    parser.add_argument("--dry-run", action="store_true", help="Only check for missing CurseForge name mappings without downloading updates")  #800 (line in Coconut source)
    parser.add_argument("--google", action="store_true", help="Use Google search to find CurseForge names for unknown mods")  #805 (line in Coconut source)
    parser.add_argument("--mods-only", action="store_true", help="Only update mods, skip datapacks")  #810 (line in Coconut source)
    parser.add_argument("--datapacks-only", action="store_true", help="Only update datapacks, skip mods")  #815 (line in Coconut source)
    return _coconut_tail_call(parser.parse_args)  #820 (line in Coconut source)



def main():  #823 (line in Coconut source)
    args = parse_args()  #824 (line in Coconut source)

    sync_mods.main()  #826 (line in Coconut source)

# Update mods (unless --datapacks-only)
    if not args.datapacks_only:  #829 (line in Coconut source)
        print("\n" + "=" * 60)  #830 (line in Coconut source)
        print("UPDATING MODS")  #831 (line in Coconut source)
        print("=" * 60 + "\n")  #832 (line in Coconut source)
        update_all(UPDATE_MODS_DIRS, dry_run=args.dry_run, google=args.google, config=MOD_CONFIG)  #833 (line in Coconut source)

# Update datapacks (unless --mods-only)
    if not args.mods_only:  #841 (line in Coconut source)
        print("\n" + "=" * 60)  #842 (line in Coconut source)
        print("UPDATING DATAPACKS")  #843 (line in Coconut source)
        print("=" * 60 + "\n")  #844 (line in Coconut source)
        update_all(UPDATE_DATAPACK_DIRS, dry_run=args.dry_run, google=args.google, config=DATAPACK_CONFIG)  #845 (line in Coconut source)



if __name__ == "__main__":  #853 (line in Coconut source)
    main()  #854 (line in Coconut source)
