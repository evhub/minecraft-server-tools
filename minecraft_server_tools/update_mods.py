#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7cc6b92e

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
from minecraft_server_tools.constants import UPDATE_MODS_GOOGLE_TEMPLATE  #22 (line in Coconut source)
from minecraft_server_tools.constants import NON_CURSEFORGE_MODS  #22 (line in Coconut source)
from minecraft_server_tools.constants import MODLOADER  #22 (line in Coconut source)
from minecraft_server_tools.constants import WRONG_MODLOADERS  #22 (line in Coconut source)
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
from minecraft_server_tools.constants import SERVER_DIR  #22 (line in Coconut source)
from minecraft_server_tools.constants import DEDUPLICATE_MODS_NAME  #22 (line in Coconut source)
from minecraft_server_tools.constants import DEDUPLICATE_CLIENT_MODS_NAME  #22 (line in Coconut source)
from minecraft_server_tools.constants import ver_join  #22 (line in Coconut source)
from minecraft_server_tools.constants import ver_split  #22 (line in Coconut source)


UPDATE_MODS_DIRS = [sync_mods.EXTRA_CLIENT_MODS_DIR, sync_mods.EXTRA_MODS_DIR, sync_mods.BASE_CLIENT_MODS_DIR, sync_mods.BASE_MODS_DIR]  #62 (line in Coconut source)

UPDATE_DATAPACK_DIRS = DATAPACK_FOLDER_PATHS  #69 (line in Coconut source)

UPDATE_DEDUPLICATE_DIRS = [os.path.join(SERVER_DIR, DEDUPLICATE_CLIENT_MODS_NAME), os.path.join(SERVER_DIR, DEDUPLICATE_MODS_NAME)]  #71 (line in Coconut source)

BEGINNING_OF_TIME = datetime.datetime(1, 1, 1)  #76 (line in Coconut source)

# Configuration for different content types (mods vs datapacks)
ContentTypeConfig = namedtuple('ContentTypeConfig', ['name', 'file_extension', 'curseforge_class_ids', 'use_modloader'])  # whether to filter by modloader  # ".jar" or ".zip"  # "mod" or "datapack"  # list of CurseForge classIds to search  #79 (line in Coconut source)

MOD_CONFIG = ContentTypeConfig(name="mod", file_extension=".jar", curseforge_class_ids=[CURSEFORGE_CLASS_ID_MODS,], use_modloader=True)  #86 (line in Coconut source)

DATAPACK_CONFIG = ContentTypeConfig(name="datapack", file_extension=".zip", curseforge_class_ids=[CURSEFORGE_CLASS_ID_DATAPACKS, CURSEFORGE_CLASS_ID_RESOURCE_PACKS], use_modloader=False)  #93 (line in Coconut source)


class MissingCurseforgeNameError(KeyError):  #101 (line in Coconut source)
    """Exception raised when a CurseForge name mapping is missing."""  #102 (line in Coconut source)
    def __init__(self, mod_name, query):  #103 (line in Coconut source)
        self.mod_name = mod_name  #104 (line in Coconut source)
        self.query = query  #105 (line in Coconut source)
        __class__ = MissingCurseforgeNameError  #106 (line in Coconut source)

        super().__init__("No Curseforge name for mod {_coconut_format_0!r}; expecting Claude to search for it and add it to curseforge_names.json (suggested search query: {_coconut_format_1!r}).".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #106 (line in Coconut source)



_coconut_call_set_names(MissingCurseforgeNameError)  #109 (line in Coconut source)
@_coconut_tco  #109 (line in Coconut source)
def get_mod_name(jar_name, silent=None, do_component_splitting=True, use_all_components=False, file_extension=".jar"):  #109 (line in Coconut source)
    def _coconut_mock_0(jar_name, silent=_coconut_sentinel, do_component_splitting=_coconut_sentinel, use_all_components=_coconut_sentinel, file_extension=_coconut_sentinel):  #110 (line in Coconut source)
        if silent is _coconut_sentinel: silent = _coconut_recursive_func_0._coconut_tco_func.__defaults__[0]  #110 (line in Coconut source)
        if do_component_splitting is _coconut_sentinel: do_component_splitting = _coconut_recursive_func_0._coconut_tco_func.__defaults__[1]  #110 (line in Coconut source)
        if use_all_components is _coconut_sentinel: use_all_components = _coconut_recursive_func_0._coconut_tco_func.__defaults__[2]  #110 (line in Coconut source)
        if file_extension is _coconut_sentinel: file_extension = _coconut_recursive_func_0._coconut_tco_func.__defaults__[3]  #110 (line in Coconut source)
        return (jar_name, silent, do_component_splitting, use_all_components, file_extension,)  #110 (line in Coconut source)
    while True:  #110 (line in Coconut source)
        if silent is None:  #110 (line in Coconut source)
            silent = not PRINT_DEBUG  #111 (line in Coconut source)

        base_name = jar_name.removesuffix(file_extension)  #113 (line in Coconut source)

        if do_component_splitting:  #115 (line in Coconut source)
            for sep, min_count in COMPONENT_SEPS:  #116 (line in Coconut source)
                components = base_name.split(sep)  #117 (line in Coconut source)
                if len(components) > min_count:  #118 (line in Coconut source)
                    break  #119 (line in Coconut source)
            else:  #120 (line in Coconut source)
                if not silent:  #121 (line in Coconut source)
                    print("Failed to find components for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #122 (line in Coconut source)
                components = [base_name,]  #123 (line in Coconut source)

            name_cmpnts = []  #125 (line in Coconut source)
            for cmpnt in components:  #126 (line in Coconut source)
                is_name_cmpnt = NON_NAME_COMPONENT_REGEX.match(cmpnt.lower()) is None  #127 (line in Coconut source)
                if is_name_cmpnt:  #128 (line in Coconut source)
                    name_cmpnts.append(cmpnt)  #129 (line in Coconut source)
                elif name_cmpnts and not use_all_components:  #130 (line in Coconut source)
                    break  #131 (line in Coconut source)
            if not name_cmpnts:  #132 (line in Coconut source)
                if not silent:  #133 (line in Coconut source)
                    print("Failed to find name component for jar {_coconut_format_0!r}.".format(_coconut_format_0=(jar_name)))  #134 (line in Coconut source)
                name_cmpnts = [components[0],]  #135 (line in Coconut source)
            mod_name = " ".join(name_cmpnts)  #136 (line in Coconut source)
        else:  #137 (line in Coconut source)
            mod_name = base_name  #138 (line in Coconut source)

        for to_space in NAME_REGEXES_TO_SPACE:  #140 (line in Coconut source)
            mod_name = to_space.sub(" ", mod_name)  #141 (line in Coconut source)

        if not mod_name:  #143 (line in Coconut source)
            if not silent:  #144 (line in Coconut source)
                print("Got empty mod name for jar {_coconut_format_0!r}; falling back to no component splitting.".format(_coconut_format_0=(jar_name)))  #145 (line in Coconut source)
            try:  #146 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #146 (line in Coconut source)
            except _coconut.NameError:  #146 (line in Coconut source)
                _coconut_tre_check_0 = False  #146 (line in Coconut source)
            if _coconut_tre_check_0:  #146 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components, file_extension,) = _coconut_mock_0(jar_name, do_component_splitting=False, file_extension=file_extension)  #146 (line in Coconut source)
                continue  #146 (line in Coconut source)
            else:  #146 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False, file_extension=file_extension)  #146 (line in Coconut source)


        camel_case_parts = [mod_name[0],]  #148 (line in Coconut source)
        prev_is_lower = mod_name[0].islower()  #149 (line in Coconut source)
        for c in mod_name[1:]:  #150 (line in Coconut source)
            if prev_is_lower and c.isupper():  #151 (line in Coconut source)
                camel_case_parts.append("")  #152 (line in Coconut source)
            camel_case_parts[-1] += c  #153 (line in Coconut source)
            prev_is_lower = c.islower()  #154 (line in Coconut source)

        mod_name = " ".join(camel_case_parts)  #156 (line in Coconut source)
        while "  " in mod_name:  #157 (line in Coconut source)
            mod_name = mod_name.replace("  ", " ")  #158 (line in Coconut source)

        mod_name = mod_name.strip().lower()  #160 (line in Coconut source)

        if not use_all_components and mod_name in USE_ALL_COMPONENTS_MODS and not use_all_components:  #162 (line in Coconut source)
            if not silent:  #163 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as use all components; redoing with all components.".format(_coconut_format_0=(mod_name)))  #164 (line in Coconut source)
            try:  #165 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #165 (line in Coconut source)
            except _coconut.NameError:  #165 (line in Coconut source)
                _coconut_tre_check_0 = False  #165 (line in Coconut source)
            if _coconut_tre_check_0:  #165 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components, file_extension,) = _coconut_mock_0(jar_name, use_all_components=True, file_extension=file_extension)  #165 (line in Coconut source)
                continue  #165 (line in Coconut source)
            else:  #165 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, use_all_components=True, file_extension=file_extension)  #165 (line in Coconut source)


        if do_component_splitting and mod_name in NO_COMPONENT_SPLIT_MODS:  #167 (line in Coconut source)
            if not silent:  #168 (line in Coconut source)
                print("Got mod name {_coconut_format_0!r}, but it's marked as no component splitting; redoing without component splitting.".format(_coconut_format_0=(mod_name)))  #169 (line in Coconut source)
            try:  #170 (line in Coconut source)
                _coconut_tre_check_0 = get_mod_name is _coconut_recursive_func_0  # type: ignore  #170 (line in Coconut source)
            except _coconut.NameError:  #170 (line in Coconut source)
                _coconut_tre_check_0 = False  #170 (line in Coconut source)
            if _coconut_tre_check_0:  #170 (line in Coconut source)
                (jar_name, silent, do_component_splitting, use_all_components, file_extension,) = _coconut_mock_0(jar_name, do_component_splitting=False, file_extension=file_extension)  #170 (line in Coconut source)
                continue  #170 (line in Coconut source)
            else:  #170 (line in Coconut source)
                return _coconut_tail_call(get_mod_name, jar_name, do_component_splitting=False, file_extension=file_extension)  #170 (line in Coconut source)


        if not silent:  #172 (line in Coconut source)
            print("Determined mod name {_coconut_format_0!r} for jar {_coconut_format_1!r}.".format(_coconut_format_0=(mod_name), _coconut_format_1=(jar_name)))  #173 (line in Coconut source)
        return mod_name  #176 (line in Coconut source)
    return None  #177 (line in Coconut source)

_coconut_recursive_func_0 = get_mod_name  #177 (line in Coconut source)

def get_curseforge_name(mod_name, jar_name, google=False):  #177 (line in Coconut source)
    if mod_name in NON_CURSEFORGE_MODS:  #178 (line in Coconut source)
        return None  #179 (line in Coconut source)
    query = UPDATE_MODS_GOOGLE_TEMPLATE.format(mod_name=mod_name, jar_name=jar_name, modloader=MODLOADER, mc_version=ver_join(MC_VERSION), mc_version_2=ver_join(MC_VERSION[:2]), mod_page_name_suffix=MOD_PAGE_NAME_SUFFICES[0])  #180 (line in Coconut source)
    if not google:  #188 (line in Coconut source)
        raise MissingCurseforgeNameError(mod_name, query)  #189 (line in Coconut source)
    try:  #190 (line in Coconut source)
        while True:  #191 (line in Coconut source)
            search_json = google_api.google(query)  #192 (line in Coconut source)
            if search_json is None or "error" in search_json and search_json["error"]["errors"][0]["reason"] == "rateLimitExceeded":  #193 (line in Coconut source)
                print("WARNING: Google API failed (try waiting or switching API keys).")  #194 (line in Coconut source)
                search_json = _coconut.dict((("items", []),))  #195 (line in Coconut source)
                break  #196 (line in Coconut source)
            if "items" in search_json:  #197 (line in Coconut source)
                break  #198 (line in Coconut source)
            print("Got no results for query {_coconut_format_0!r}.".format(_coconut_format_0=(query)))  #199 (line in Coconut source)
            if "spelling" in search_json:  #200 (line in Coconut source)
                query = unquote(search_json["spelling"]["correctedQuery"]).replace("+", " ")  #201 (line in Coconut source)
                continue  #202 (line in Coconut source)
            assert search_json["searchInformation"]["totalResults"] == "0", search_json  #203 (line in Coconut source)
            search_json = _coconut.dict((("items", []),))  #204 (line in Coconut source)
            break  #205 (line in Coconut source)
        items = search_json["items"]  #206 (line in Coconut source)
        curseforge_name = None  #207 (line in Coconut source)
        for result in items:  #208 (line in Coconut source)
            mod_page = result["title"]  #209 (line in Coconut source)
            for suffix in MOD_PAGE_NAME_SUFFICES:  #210 (line in Coconut source)
                if mod_page.lower().endswith(suffix.lower()):  #211 (line in Coconut source)
                    curseforge_name = clean_curseforge_name(mod_page[:-len(suffix)])  #212 (line in Coconut source)
                    break  #213 (line in Coconut source)
            if curseforge_name is not None:  #214 (line in Coconut source)
                break  #215 (line in Coconut source)
            else:  #216 (line in Coconut source)
                print("Skipping search result {_coconut_format_0!r}.".format(_coconut_format_0=(mod_page)))  #217 (line in Coconut source)
        if curseforge_name is None:  #218 (line in Coconut source)
            print("Could not find curseforge name for mod {_coconut_format_0!r} in results for query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #219 (line in Coconut source)
            pprint(items[:MAX_DEBUG_RESULTS])  #220 (line in Coconut source)
            curseforge_name = query.rsplit(MODLOADER, 1)[0].strip()  #221 (line in Coconut source)
        else:  #222 (line in Coconut source)
            print("Found curseforge name {_coconut_format_0!r} for mod {_coconut_format_1!r} in result {_coconut_format_2!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(mod_name), _coconut_format_2=(mod_page)))  #223 (line in Coconut source)
        print("Verifying found curseforge name using curseforge search...")  #224 (line in Coconut source)
        mod = get_curseforge_mod(mod_name, curseforge_name)  #225 (line in Coconut source)
        if mod is None:  #226 (line in Coconut source)
            raise IOError("Could not find curseforge name for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #227 (line in Coconut source)
        else:  #228 (line in Coconut source)
            return mod["name"]  #229 (line in Coconut source)
    except (KeyError, IndexError, AssertionError):  #230 (line in Coconut source)
        print("ERROR: Invalid search results for mod {_coconut_format_0!r} and query {_coconut_format_1!r}:".format(_coconut_format_0=(mod_name), _coconut_format_1=(query)))  #231 (line in Coconut source)
        pprint(search_json)  #232 (line in Coconut source)
        raise  #233 (line in Coconut source)



def clean_curseforge_name(curseforge_name):  #236 (line in Coconut source)
    old_curseforge_name = None  #237 (line in Coconut source)
    while old_curseforge_name != curseforge_name:  #238 (line in Coconut source)
        old_curseforge_name = curseforge_name  #239 (line in Coconut source)
        for strip_str in CURSEFORGE_NAME_ELEMS_TO_STRIP:  #240 (line in Coconut source)
            if curseforge_name.startswith(strip_str):  #241 (line in Coconut source)
                curseforge_name = curseforge_name[len(strip_str):]  #242 (line in Coconut source)
            if curseforge_name.endswith(strip_str):  #243 (line in Coconut source)
                curseforge_name = curseforge_name[:-len(strip_str)]  #244 (line in Coconut source)
        curseforge_name = curseforge_name.strip()  #245 (line in Coconut source)
    return curseforge_name  #246 (line in Coconut source)



@_coconut_tco  #249 (line in Coconut source)
def load_curseforge_names():  #249 (line in Coconut source)
    if os.path.exists(CURSEFORGE_NAMES_FILE):  #250 (line in Coconut source)
        with open(CURSEFORGE_NAMES_FILE, "r") as ids_fobj:  #251 (line in Coconut source)
            curseforge_names = COMMENT_JSON.load(ids_fobj)  #252 (line in Coconut source)
            if FIX_MOD_NAMES:  #253 (line in Coconut source)
                curseforge_names = _coconut.dict(((get_mod_name(mod_name)), (curseforge_name)) for mod_name, curseforge_name in curseforge_names.items())  #254 (line in Coconut source)
            return curseforge_names  #255 (line in Coconut source)
    else:  #256 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #257 (line in Coconut source)



def save_curseforge_names(mod_names_to_curseforge_names):  #260 (line in Coconut source)
    with open(CURSEFORGE_NAMES_FILE, "w") as ids_fobj:  #261 (line in Coconut source)
        json.dump(mod_names_to_curseforge_names, ids_fobj, indent=4)  #262 (line in Coconut source)



@_coconut_tco  #265 (line in Coconut source)
def load_curseforge_ids_cache():  #265 (line in Coconut source)
    """Load the cached curseforge_name -> curseforge_id mappings."""  #266 (line in Coconut source)
    if os.path.exists(CURSEFORGE_IDS_CACHE_FILE):  #267 (line in Coconut source)
        with open(CURSEFORGE_IDS_CACHE_FILE, "r") as cache_fobj:  #268 (line in Coconut source)
            return json.load(cache_fobj)  #269 (line in Coconut source)
    else:  #270 (line in Coconut source)
        return _coconut_tail_call(_coconut.dict)  #271 (line in Coconut source)



def save_curseforge_ids_cache(curseforge_ids_cache):  #274 (line in Coconut source)
    """Save the curseforge_name -> curseforge_id cache."""  #275 (line in Coconut source)
    with open(CURSEFORGE_IDS_CACHE_FILE, "w") as cache_fobj:  #276 (line in Coconut source)
        json.dump(curseforge_ids_cache, cache_fobj, indent=4)  #277 (line in Coconut source)



def get_curseforge_names_for(mod_names_to_jar_names, google=False):  #280 (line in Coconut source)
    all_mod_names_to_curseforge_names = load_curseforge_names()  #281 (line in Coconut source)
    found_curseforge_names_to_mod_names = _coconut.dict()  #282 (line in Coconut source)
    missing_curseforge_names = []  # collect all missing names first  #283 (line in Coconut source)
    try:  #284 (line in Coconut source)
        for mod_name in mod_names_to_jar_names:  #285 (line in Coconut source)
            if mod_name not in all_mod_names_to_curseforge_names:  #286 (line in Coconut source)
                try:  #287 (line in Coconut source)
                    curseforge_name = get_curseforge_name(mod_name, mod_names_to_jar_names[mod_name], google=google)  #288 (line in Coconut source)
                except MissingCurseforgeNameError as e:  #289 (line in Coconut source)
                    missing_curseforge_names.append((e.mod_name, e.query))  #290 (line in Coconut source)
                    continue  #291 (line in Coconut source)

# do validation
                if curseforge_name in found_curseforge_names_to_mod_names:  #294 (line in Coconut source)
                    raise ValueError("resolved multiple mod names to curseforge name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_curseforge_names_to_mod_names[curseforge_name]), _coconut_format_2=(mod_name)))  #295 (line in Coconut source)
                found_curseforge_names_to_mod_names[curseforge_name] = mod_name  #296 (line in Coconut source)

                all_mod_names_to_curseforge_names[mod_name] = curseforge_name  #298 (line in Coconut source)
    finally:  #299 (line in Coconut source)
        save_curseforge_names(all_mod_names_to_curseforge_names)  #300 (line in Coconut source)

# raise error with all missing names at once
    if missing_curseforge_names:  #303 (line in Coconut source)
        print("\n{_coconut_format_0}".format(_coconut_format_0=('=' * 60)))  #304 (line in Coconut source)
        print("MISSING CURSEFORGE NAME MAPPINGS:")  #305 (line in Coconut source)
        print("{_coconut_format_0}\n".format(_coconut_format_0=('=' * 60)))  #306 (line in Coconut source)
        for mod_name, query in missing_curseforge_names:  #307 (line in Coconut source)
            print("{_coconut_format_0!r}".format(_coconut_format_0=(mod_name)))  #308 (line in Coconut source)
            print("\tSuggested search query: {_coconut_format_0!r}\n".format(_coconut_format_0=(query)))  #309 (line in Coconut source)
        print("{_coconut_format_0}\n".format(_coconut_format_0=('=' * 60)))  #310 (line in Coconut source)
        raise KeyError("Missing {_coconut_format_0} Curseforge name mappings; expecting Claude to search for them and add them to curseforge_names.json.".format(_coconut_format_0=(len(missing_curseforge_names))))  #311 (line in Coconut source)

# get nulled mods
    requested_mod_names_to_curseforge_names = _coconut.dict()  #314 (line in Coconut source)
    nulled_mods = []  #315 (line in Coconut source)
    for mod_name in mod_names_to_jar_names:  #316 (line in Coconut source)
        curseforge_name = all_mod_names_to_curseforge_names[mod_name]  #317 (line in Coconut source)
        if curseforge_name is None:  #318 (line in Coconut source)
            nulled_mods.append(mod_name)  #319 (line in Coconut source)
            print("Skipping mod {_coconut_format_0!r} due to explicitly nulled CurseForge name.".format(_coconut_format_0=(mod_name)))  #320 (line in Coconut source)
        else:  #321 (line in Coconut source)
            requested_mod_names_to_curseforge_names[mod_name] = curseforge_name  #322 (line in Coconut source)
    return requested_mod_names_to_curseforge_names, nulled_mods  #323 (line in Coconut source)



def get_jar_names(mods_dir, file_extension=".jar"):  #326 (line in Coconut source)
    for fname in os.listdir(mods_dir):  #327 (line in Coconut source)
        if fname.endswith(file_extension):  #328 (line in Coconut source)
            yield fname  #329 (line in Coconut source)



def get_mod_names_to_all_jar_names(mods_dir, file_extension=".jar", **kwargs):  #332 (line in Coconut source)
    mod_names_to_all_jar_names = defaultdict(list)  #333 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir, file_extension=file_extension):  #334 (line in Coconut source)
        mod_name = get_mod_name(jar_name, file_extension=file_extension, **kwargs)  #335 (line in Coconut source)
        mod_names_to_all_jar_names[mod_name] += [jar_name,]  #336 (line in Coconut source)
    return mod_names_to_all_jar_names  #337 (line in Coconut source)



def get_mod_names_to_jar_names(mods_dir, file_extension=".jar", **kwargs):  #340 (line in Coconut source)
    mod_names_to_jar_names = _coconut.dict()  #341 (line in Coconut source)
    for jar_name in get_jar_names(mods_dir, file_extension=file_extension):  #342 (line in Coconut source)
        mod_name = get_mod_name(jar_name, file_extension=file_extension, **kwargs)  #343 (line in Coconut source)
        if mod_name in mod_names_to_jar_names:  #344 (line in Coconut source)
            raise ValueError("resolved multiple jars to name {_coconut_format_0!r}: {_coconut_format_1} and {_coconut_format_2}".format(_coconut_format_0=(mod_name), _coconut_format_1=(mod_names_to_jar_names[mod_name]), _coconut_format_2=(jar_name)))  #345 (line in Coconut source)
        mod_names_to_jar_names[mod_name] = jar_name  #346 (line in Coconut source)
    return mod_names_to_jar_names  #347 (line in Coconut source)



def run_curseforge_api_cmd(cmd, class_id=None):  #350 (line in Coconut source)
    cmd = [str(x) for x in cmd]  #351 (line in Coconut source)
    if class_id is not None:  #352 (line in Coconut source)
        cmd.append(str(class_id))  #353 (line in Coconut source)
    for _ in range(CURSEFORGE_API_RETRIES):  #354 (line in Coconut source)
        print("Executing curseforge api cmd: {_coconut_format_0!r}".format(_coconut_format_0=(cmd)))  #355 (line in Coconut source)
        cmd_result = subprocess.run(["node", CURSEFORGE_API_FILE] + cmd, capture_output=True)  #356 (line in Coconut source)
        if cmd_result.stderr:  #357 (line in Coconut source)
            print("\tcurseforge api cmd {_coconut_format_0!r} failed: {_coconut_format_1}".format(_coconut_format_0=(cmd), _coconut_format_1=(cmd_result.stderr.decode('utf-8'))))  #358 (line in Coconut source)
            time.sleep(CURSEFORGE_API_RETRY_DELAY)  #359 (line in Coconut source)
        else:  #360 (line in Coconut source)
            break  #361 (line in Coconut source)
    else:  #362 (line in Coconut source)
        raise Exception("Curseforge api cmd {_coconut_format_0!r} failed {_coconut_format_1} times.".format(_coconut_format_0=(cmd), _coconut_format_1=(CURSEFORGE_API_RETRIES)))  #363 (line in Coconut source)
    api_result = cmd_result.stdout.decode("utf-8")  #364 (line in Coconut source)
    if not api_result:  #365 (line in Coconut source)
        print("\tGot no output from curseforge api.")  #366 (line in Coconut source)
        return []  #367 (line in Coconut source)
    try:  #368 (line in Coconut source)
        return json.loads(api_result)  #369 (line in Coconut source)
    except json.decoder.JSONDecodeError:  #370 (line in Coconut source)
        print("\nERROR: Could not parse curseforge api output:")  #371 (line in Coconut source)
        print(api_result)  #372 (line in Coconut source)
        raise  #373 (line in Coconut source)



def has_bad_modloader(name):  #376 (line in Coconut source)
    if any((wrong_modloader.lower() in name.lower() for wrong_modloader in WRONG_MODLOADERS)):  #377 (line in Coconut source)
        non_wrong_modloader_name = name.lower()  #378 (line in Coconut source)
        for wrong_modloader in WRONG_MODLOADERS:  #379 (line in Coconut source)
            non_wrong_modloader_name = non_wrong_modloader_name.replace(wrong_modloader.lower(), " ")  #380 (line in Coconut source)
        return MODLOADER.lower() not in non_wrong_modloader_name  #381 (line in Coconut source)
    return False  #382 (line in Coconut source)


def get_matching_mod(results, curseforge_name, mod_name):  #384 (line in Coconut source)
    found_mod = None  #385 (line in Coconut source)
    valid_modloader_results = []  #386 (line in Coconut source)
    for mod in results:  #387 (line in Coconut source)
        valid_modloader = not has_bad_modloader(mod["name"])  #388 (line in Coconut source)
        if mod["name"] == curseforge_name:  #389 (line in Coconut source)
            if not valid_modloader:  #390 (line in Coconut source)
                print("\tWARNING: found Curseforge mod by name, but it looks like it has an invalid modloader: {_coconut_format_0}".format(_coconut_format_0=(curseforge_name)))  #391 (line in Coconut source)
            found_mod = mod  #392 (line in Coconut source)
            break  #393 (line in Coconut source)
        if valid_modloader:  #394 (line in Coconut source)
            valid_modloader_results.append(mod)  #395 (line in Coconut source)
    if found_mod is None:  #396 (line in Coconut source)
        for mod in valid_modloader_results:  #397 (line in Coconut source)
            if mod["name"].startswith(curseforge_name):  #398 (line in Coconut source)
                found_mod = mod  #399 (line in Coconut source)
                break  #400 (line in Coconut source)
    if found_mod is None:  #401 (line in Coconut source)
        for mod in valid_modloader_results:  #402 (line in Coconut source)
            if curseforge_name in mod["name"]:  #403 (line in Coconut source)
                found_mod = mod  #404 (line in Coconut source)
                break  #405 (line in Coconut source)
    if found_mod is None:  #406 (line in Coconut source)
        slug_name = mod_name.replace(" ", "").lower()  #407 (line in Coconut source)
        for mod in valid_modloader_results:  #408 (line in Coconut source)
            if mod["slug"].replace("-", "").lower() == slug_name:  #409 (line in Coconut source)
                found_mod = mod  #410 (line in Coconut source)
                break  #411 (line in Coconut source)
    if found_mod is None:  #412 (line in Coconut source)
        core_curseforge_name = get_core_name(curseforge_name)  #413 (line in Coconut source)
        if core_curseforge_name:  #414 (line in Coconut source)
            for mod in valid_modloader_results:  #415 (line in Coconut source)
                if core_curseforge_name in mod["name"]:  #416 (line in Coconut source)
                    found_mod = mod  #417 (line in Coconut source)
                    break  #418 (line in Coconut source)
    if found_mod is not None and found_mod["name"].strip() != curseforge_name:  #419 (line in Coconut source)
        print("\tWARNING: found Curseforge mod with different name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(found_mod['name'])))  #420 (line in Coconut source)
    return found_mod  #421 (line in Coconut source)



def log_curseforge_results(results, verbose=False):  #424 (line in Coconut source)
    if verbose:  #425 (line in Coconut source)
        pprint(results[:MAX_DEBUG_RESULTS])  #426 (line in Coconut source)
    else:  #427 (line in Coconut source)
        pprint([m["name"] for m in results[:MAX_DEBUG_RESULTS]])  #428 (line in Coconut source)



get_core_name = _coconut_partial(get_mod_name, silent=True)  #431 (line in Coconut source)


def get_curseforge_mod(curseforge_name, mod_name, config=MOD_CONFIG):  #434 (line in Coconut source)
    core_curseforge_name = get_core_name(curseforge_name)  #435 (line in Coconut source)

# Try each classId in the config
    for class_id in config.curseforge_class_ids:  #438 (line in Coconut source)
        seen_queries = set()  #439 (line in Coconut source)
        for query_template in CURSEFORGE_QUERY_TEMPLATES:  #440 (line in Coconut source)
            query = query_template.format(curseforge_name=curseforge_name, core_curseforge_name=core_curseforge_name, mod_name=mod_name)  #441 (line in Coconut source)
            if query in seen_queries:  #446 (line in Coconut source)
                continue  #447 (line in Coconut source)
            seen_queries.add(query)  #448 (line in Coconut source)

            if config.use_modloader:  #450 (line in Coconut source)
                modloader_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), MODLOADER], class_id=class_id)  #451 (line in Coconut source)
                mod = get_matching_mod(modloader_version_results, curseforge_name, mod_name)  #452 (line in Coconut source)
                if mod is not None:  #453 (line in Coconut source)
                    return mod  #454 (line in Coconut source)
                if PRINT_DEBUG:  #455 (line in Coconut source)
                    print("\tCould not find mod {_coconut_format_0!r} in modloader-version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #456 (line in Coconut source)

                modloader_compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), MODLOADER], class_id=class_id)  #458 (line in Coconut source)
                mod = get_matching_mod(modloader_compatible_version_results, curseforge_name, mod_name)  #459 (line in Coconut source)
                if mod is not None:  #460 (line in Coconut source)
                    return mod  #461 (line in Coconut source)
                if PRINT_DEBUG:  #462 (line in Coconut source)
                    print("\tCould not find mod {_coconut_format_0!r} in modloader-compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #463 (line in Coconut source)

            version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION), ""], class_id=class_id)  #465 (line in Coconut source)
            mod = get_matching_mod(version_results, curseforge_name, mod_name)  #466 (line in Coconut source)
            if mod is not None:  #467 (line in Coconut source)
                return mod  #468 (line in Coconut source)
            if PRINT_DEBUG:  #469 (line in Coconut source)
                print("\tCould not find mod {_coconut_format_0!r} in version-specific results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #470 (line in Coconut source)

            compatible_version_results = run_curseforge_api_cmd(["search", query, ver_join(MC_VERSION[:2]), ""], class_id=class_id)  #472 (line in Coconut source)
            mod = get_matching_mod(compatible_version_results, curseforge_name, mod_name)  #473 (line in Coconut source)
            if mod is not None:  #474 (line in Coconut source)
                return mod  #475 (line in Coconut source)
            if PRINT_DEBUG:  #476 (line in Coconut source)
                print("\tCould not find mod {_coconut_format_0!r} in compatibly-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #477 (line in Coconut source)

            if config.use_modloader:  #479 (line in Coconut source)
                modloader_results = run_curseforge_api_cmd(["search", query, "", MODLOADER], class_id=class_id)  #480 (line in Coconut source)
                mod = get_matching_mod(modloader_results, curseforge_name, mod_name)  #481 (line in Coconut source)
                if mod is not None:  #482 (line in Coconut source)
                    return mod  #483 (line in Coconut source)
                if PRINT_DEBUG:  #484 (line in Coconut source)
                    print("\tCould not find mod {_coconut_format_0!r} in modloader-versioned results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #485 (line in Coconut source)

            versionless_results = run_curseforge_api_cmd(["search", query, "", ""], class_id=class_id)  #487 (line in Coconut source)
            mod = get_matching_mod(versionless_results, curseforge_name, mod_name)  #488 (line in Coconut source)
            if mod is not None:  #489 (line in Coconut source)
                return mod  #490 (line in Coconut source)
            if PRINT_DEBUG:  #491 (line in Coconut source)
                print("\tCould not find mod {_coconut_format_0!r} in version-less results for query {_coconut_format_1!r}.".format(_coconut_format_0=(curseforge_name), _coconut_format_1=(query)))  #492 (line in Coconut source)

    print("\nERROR: Failed to find mod {_coconut_format_0!r} in any results.\n".format(_coconut_format_0=(curseforge_name)))  #494 (line in Coconut source)



def get_curseforge_id(curseforge_name, mod_name, **kwargs):  #497 (line in Coconut source)
    mod = get_curseforge_mod(curseforge_name, mod_name, **kwargs)  #498 (line in Coconut source)
    if mod is not None:  #499 (line in Coconut source)
        return mod["id"]  #500 (line in Coconut source)



def get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names, **kwargs):  #503 (line in Coconut source)
    curseforge_ids_cache = load_curseforge_ids_cache()  #504 (line in Coconut source)
    mod_names_to_curseforge_ids = _coconut.dict()  #505 (line in Coconut source)
    missing_mods = []  #506 (line in Coconut source)
    try:  #507 (line in Coconut source)
        for mod_name, curseforge_name in mod_names_to_curseforge_names.items():  #508 (line in Coconut source)
# Check cache first
            if curseforge_name in curseforge_ids_cache:  #510 (line in Coconut source)
                curseforge_id = curseforge_ids_cache[curseforge_name]  #511 (line in Coconut source)
                print("Using cached CurseForge ID for {_coconut_format_0!r}.".format(_coconut_format_0=(curseforge_name)))  #512 (line in Coconut source)
            else:  #513 (line in Coconut source)
                curseforge_id = get_curseforge_id(curseforge_name, mod_name, **kwargs)  #514 (line in Coconut source)
                if curseforge_id is not None:  #515 (line in Coconut source)
                    curseforge_ids_cache[curseforge_name] = curseforge_id  #516 (line in Coconut source)

            if curseforge_id is None:  #518 (line in Coconut source)
                missing_mods.append(mod_name)  #519 (line in Coconut source)
            else:  #520 (line in Coconut source)
                mod_names_to_curseforge_ids[mod_name] = curseforge_id  #521 (line in Coconut source)
    finally:  #522 (line in Coconut source)
        save_curseforge_ids_cache(curseforge_ids_cache)  #523 (line in Coconut source)
    return mod_names_to_curseforge_ids, missing_mods  #524 (line in Coconut source)



@_coconut_tco  #527 (line in Coconut source)
def get_curseforge_files(curseforge_id):  #527 (line in Coconut source)
    return _coconut_tail_call(run_curseforge_api_cmd, ["getfiles", curseforge_id])  #528 (line in Coconut source)



def get_curseforge_file_time(curseforge_file, mod_name):  #531 (line in Coconut source)
    timestamp = curseforge_file["fileDate"]  #532 (line in Coconut source)
    match_results = TIMESTAMP_FORMAT_REGEX.match(timestamp)  #533 (line in Coconut source)
    if match_results is None:  #534 (line in Coconut source)
        raise ValueError("failed to parse timestamp {_coconut_format_0!r}".format(_coconut_format_0=(timestamp)))  #535 (line in Coconut source)
    parsed_time = datetime.datetime(*(int(match_results[i]) for i in range(1, 7)))  #536 (line in Coconut source)
    if (AVOID_FILES_PUBLISHED_WITHIN is not None and mod_name not in ALWAYS_USE_LATEST_VERSION_FOR_MODS and datetime.datetime.now() - parsed_time < AVOID_FILES_PUBLISHED_WITHIN):  #537 (line in Coconut source)
        parsed_time = BEGINNING_OF_TIME  #542 (line in Coconut source)
    return parsed_time  #543 (line in Coconut source)



@_coconut_tco  #546 (line in Coconut source)
def timestamp_sort(curseforge_files):  #546 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: get_curseforge_file_time(f, mod_name=None), reverse=True)  #546 (line in Coconut source)



@_coconut_tco  #553 (line in Coconut source)
def get_max_version(versions):  #553 (line in Coconut source)
    ver_tuples = []  #554 (line in Coconut source)
    for ver_str in versions:  #555 (line in Coconut source)
        try:  #556 (line in Coconut source)
            ver_tuples.append(ver_split(ver_str))  #557 (line in Coconut source)
        except ValueError:  #558 (line in Coconut source)
            pass  #559 (line in Coconut source)
    return _coconut_tail_call(max, ver_tuples)  #560 (line in Coconut source)



@_coconut_tco  #563 (line in Coconut source)
def sort_releases(curseforge_files, mod_name):  #563 (line in Coconut source)
    return _coconut_tail_call(sorted, curseforge_files, key=lambda f: (get_max_version(f["gameVersions"]), (0 if mod_name in ALWAYS_USE_LATEST_VERSION_FOR_MODS else -f["releaseType"]), get_curseforge_file_time(f, mod_name)), reverse=True)  #563 (line in Coconut source)



def best_release(curseforge_files, mod_name):  #577 (line in Coconut source)
    return sort_releases(curseforge_files, mod_name)[0]  #578 (line in Coconut source)



@_coconut_tco  #581 (line in Coconut source)
def reconstruct_curseforge_download_url(curseforge_file):  #581 (line in Coconut source)
    """Reconstruct download URL from file ID when downloadUrl is None."""  #582 (line in Coconut source)
    file_id = curseforge_file["id"]  #583 (line in Coconut source)
    filename = curseforge_file["fileName"]  #584 (line in Coconut source)
    first_part = file_id // 1000  #585 (line in Coconut source)
    second_part = file_id % 1000  #586 (line in Coconut source)
    return _coconut_tail_call("https://edge.forgecdn.net/files/{_coconut_format_0}/{_coconut_format_1}/{_coconut_format_2}".format, _coconut_format_0=(first_part), _coconut_format_1=(second_part), _coconut_format_2=(filename))  #587 (line in Coconut source)



@_coconut_tco  #590 (line in Coconut source)
def get_curseforge_download_url(curseforge_file):  #590 (line in Coconut source)
    """Get download URL, reconstructing it if necessary."""  #591 (line in Coconut source)
    url = curseforge_file["downloadUrl"]  #592 (line in Coconut source)
    if url is None:  #593 (line in Coconut source)
        return _coconut_tail_call(reconstruct_curseforge_download_url, curseforge_file)  #594 (line in Coconut source)
    return url  #595 (line in Coconut source)



def get_jar_name_for_curseforge_file(curseforge_file):  #598 (line in Coconut source)
    return (((get_curseforge_download_url(curseforge_file)).rsplit("/", 1))[-1])  #598 (line in Coconut source)



def correct_modloader(versions, jar_name=None):  #605 (line in Coconut source)
    versions = [v.lower() for v in versions]  #606 (line in Coconut source)

    if MODLOADER.lower() in versions:  #608 (line in Coconut source)
        return True  #609 (line in Coconut source)
    if any((wrong_modloader.lower() in versions for wrong_modloader in WRONG_MODLOADERS)):  #610 (line in Coconut source)
        return False  #611 (line in Coconut source)

    if jar_name is not None:  #613 (line in Coconut source)
        jar_name = jar_name.lower()  #614 (line in Coconut source)
        if has_bad_modloader(jar_name):  #615 (line in Coconut source)
            return False  #616 (line in Coconut source)

    return None  #618 (line in Coconut source)



def find_curseforge_file_for_jar(curseforge_files, find_jar_name):  #621 (line in Coconut source)
    for file_data in curseforge_files:  #622 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #623 (line in Coconut source)
        if jar_name is not None and are_same_jar(jar_name, find_jar_name):  #624 (line in Coconut source)
            return file_data  #625 (line in Coconut source)
    return None  #626 (line in Coconut source)



@_coconut_tco  #629 (line in Coconut source)
def get_latest_version(mod_name, curseforge_id, old_jar_name, config=MOD_CONFIG):  #629 (line in Coconut source)
    curseforge_files = get_curseforge_files(curseforge_id)  #630 (line in Coconut source)

    old_curseforge_file = find_curseforge_file_for_jar(curseforge_files, old_jar_name)  #632 (line in Coconut source)
    if old_curseforge_file is None:  #633 (line in Coconut source)
        print("WARNING: Could not find curseforge file for existing jar: {_coconut_format_0}".format(_coconut_format_0=(old_jar_name)))  #634 (line in Coconut source)
    old_file_time = get_curseforge_file_time(old_curseforge_file, mod_name) if old_curseforge_file is not None else BEGINNING_OF_TIME  #635 (line in Coconut source)

    curseforge_files_and_versions = []  #637 (line in Coconut source)
    for file_data in curseforge_files:  #638 (line in Coconut source)
        versions = file_data["gameVersions"]  #639 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(file_data)  #640 (line in Coconut source)
        modloader_ok = not config.use_modloader or correct_modloader(versions, jar_name) is not False  #641 (line in Coconut source)
        if (jar_name is not None and jar_name.endswith(config.file_extension) and modloader_ok and get_curseforge_file_time(file_data, mod_name) >= old_file_time):  #642 (line in Coconut source)
            curseforge_files_and_versions.append((file_data, versions))  #648 (line in Coconut source)

    if config.use_modloader:  #650 (line in Coconut source)
        correct_modloader_and_version_files = []  #651 (line in Coconut source)
        for file_data, versions in curseforge_files_and_versions:  #652 (line in Coconut source)
            if correct_modloader(versions) and ver_join(MC_VERSION) in versions:  #653 (line in Coconut source)
                correct_modloader_and_version_files.append(file_data)  #654 (line in Coconut source)
        if correct_modloader_and_version_files:  #655 (line in Coconut source)
            return _coconut_tail_call(best_release, correct_modloader_and_version_files, mod_name)  #656 (line in Coconut source)

    correctly_versioned_files = []  #658 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #659 (line in Coconut source)
        if ver_join(MC_VERSION) in versions:  #660 (line in Coconut source)
            correctly_versioned_files.append(file_data)  #661 (line in Coconut source)
    if correctly_versioned_files:  #662 (line in Coconut source)
        return _coconut_tail_call(best_release, correctly_versioned_files, mod_name)  #663 (line in Coconut source)
    print("No correctly versioned files found for mod {_coconut_format_0!r}.".format(_coconut_format_0=(mod_name)))  #664 (line in Coconut source)

    correct_modloader_compatibly_versioned_files = []  #666 (line in Coconut source)
    compatibly_versioned_files = []  #667 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #668 (line in Coconut source)
        for raw_ver in versions:  #669 (line in Coconut source)
            try:  #670 (line in Coconut source)
                ver = ver_split(raw_ver)  #671 (line in Coconut source)
            except ValueError:  #672 (line in Coconut source)
                pass  #673 (line in Coconut source)
            else:  #674 (line in Coconut source)
                if MC_VERSION[:2] <= ver <= MC_VERSION:  #675 (line in Coconut source)
                    if config.use_modloader and correct_modloader(versions):  #676 (line in Coconut source)
                        correct_modloader_compatibly_versioned_files.append(file_data)  #677 (line in Coconut source)
                    compatibly_versioned_files.append(file_data)  #678 (line in Coconut source)
                    break  #679 (line in Coconut source)
    if correct_modloader_compatibly_versioned_files:  #680 (line in Coconut source)
        return _coconut_tail_call(best_release, correct_modloader_compatibly_versioned_files, mod_name)  #681 (line in Coconut source)
    if compatibly_versioned_files:  #682 (line in Coconut source)
        return _coconut_tail_call(best_release, compatibly_versioned_files, mod_name)  #683 (line in Coconut source)

    correct_modloader_maybe_compatible_files = []  #685 (line in Coconut source)
    maybe_compatible_files = []  #686 (line in Coconut source)
    for file_data, versions in curseforge_files_and_versions:  #687 (line in Coconut source)
        for ver in versions:  #688 (line in Coconut source)
            if ver.startswith(ver_join(MC_VERSION[:2])):  #689 (line in Coconut source)
                if config.use_modloader and correct_modloader(versions):  #690 (line in Coconut source)
                    correct_modloader_maybe_compatible_files.append(file_data)  #691 (line in Coconut source)
                maybe_compatible_files.append(file_data)  #692 (line in Coconut source)
                break  #693 (line in Coconut source)
    if correct_modloader_maybe_compatible_files:  #694 (line in Coconut source)
        return _coconut_tail_call(best_release, correct_modloader_maybe_compatible_files, mod_name)  #695 (line in Coconut source)
    if maybe_compatible_files:  #696 (line in Coconut source)
        return _coconut_tail_call(best_release, maybe_compatible_files, mod_name)  #697 (line in Coconut source)
    print("No compatibly versioned files found for mod {_coconut_format_0!r} in:".format(_coconut_format_0=(mod_name)))  #698 (line in Coconut source)
    pprint(list(timestamp_sort(curseforge_files))[:MAX_DEBUG_RESULTS])  #699 (line in Coconut source)



def are_same_jar(jar_name_1, jar_name_2):  #702 (line in Coconut source)
    return jar_name_1.replace(" ", "+") == jar_name_2.replace(" ", "+")  #703 (line in Coconut source)



def get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names, **kwargs):  #706 (line in Coconut source)
    mod_names_to_latest_versions = _coconut.dict()  #707 (line in Coconut source)
    missing_mods = []  #708 (line in Coconut source)
    for mod_name, curseforge_id in mod_names_to_curseforge_ids.items():  #709 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #710 (line in Coconut source)
        latest_version = get_latest_version(mod_name, curseforge_id, jar_name, **kwargs)  #711 (line in Coconut source)
        if latest_version is None:  #712 (line in Coconut source)
            missing_mods.append(mod_name)  #713 (line in Coconut source)
        else:  #714 (line in Coconut source)
            mod_names_to_latest_versions[mod_name] = latest_version  #715 (line in Coconut source)
    return mod_names_to_latest_versions, missing_mods  #716 (line in Coconut source)



def get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions):  #719 (line in Coconut source)
    updated_mod_names_to_files = _coconut.dict()  #720 (line in Coconut source)
    for mod_name, latest_file in mod_names_to_latest_versions.items():  #721 (line in Coconut source)
        old_jar = mod_names_to_jar_names[mod_name]  #722 (line in Coconut source)
        new_jar = get_jar_name_for_curseforge_file(latest_file)  #723 (line in Coconut source)
        if new_jar is not None and not are_same_jar(new_jar, old_jar):  #724 (line in Coconut source)
            updated_mod_names_to_files[mod_name] = latest_file  #725 (line in Coconut source)
    return updated_mod_names_to_files  #726 (line in Coconut source)



def download_file(curseforge_file, updated_mods_dir, mod_name):  #729 (line in Coconut source)
    jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #730 (line in Coconut source)
    assert jar_name is not None, "cannot download from curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #731 (line in Coconut source)
    url = get_curseforge_download_url(curseforge_file)  #732 (line in Coconut source)
    new_jar_path = os.path.join(updated_mods_dir, jar_name)  #733 (line in Coconut source)
    if os.path.exists(new_jar_path):  #734 (line in Coconut source)
        print("WARNING: attempting to redownload existing jar {_coconut_format_0!r}".format(_coconut_format_0=(jar_name)))  #735 (line in Coconut source)
    else:  #736 (line in Coconut source)
        print("Downloading {_coconut_format_0}...".format(_coconut_format_0=(jar_name)))  #737 (line in Coconut source)
        new_mod_name = get_mod_name(jar_name, silent=True)  #738 (line in Coconut source)
        if new_mod_name != mod_name:  #739 (line in Coconut source)
            print("\tWARNING: new mod name: {_coconut_format_0!r} -> {_coconut_format_1!r}".format(_coconut_format_0=(mod_name), _coconut_format_1=(new_mod_name)))  #740 (line in Coconut source)
        result = requests.get(url)  #741 (line in Coconut source)
        with open(new_jar_path, "wb") as jar_fobj:  #742 (line in Coconut source)
            jar_fobj.write(result.content)  #743 (line in Coconut source)



def update_files(updated_mod_names_to_files, updated_mods_dir):  #746 (line in Coconut source)
    seen_jar_names = _coconut.dict()  #747 (line in Coconut source)
    for mod_name, curseforge_file in updated_mod_names_to_files.items():  #748 (line in Coconut source)
        jar_name = get_jar_name_for_curseforge_file(curseforge_file)  #749 (line in Coconut source)
        assert jar_name is not None, "cannot update using curseforge file: {_coconut_format_0!r}".format(_coconut_format_0=(curseforge_file))  #750 (line in Coconut source)
        if jar_name in seen_jar_names:  #751 (line in Coconut source)
            print("\nWARNING: resolved multiple mod names to same jar name {_coconut_format_0!r}: {_coconut_format_1!r} and {_coconut_format_2!r}\n".format(_coconut_format_0=(jar_name), _coconut_format_1=(seen_jar_names[jar_name]), _coconut_format_2=(mod_name)))  #752 (line in Coconut source)
        else:  #753 (line in Coconut source)
            seen_jar_names[jar_name] = mod_name  #754 (line in Coconut source)
        download_file(curseforge_file, updated_mods_dir, mod_name)  #755 (line in Coconut source)



def move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir):  #758 (line in Coconut source)
    for mod_name in updated_mod_names_to_files:  #759 (line in Coconut source)
        jar_name = mod_names_to_jar_names[mod_name]  #760 (line in Coconut source)
        current_jar_path = os.path.join(mods_dir, jar_name)  #761 (line in Coconut source)
        new_jar_path = os.path.join(old_mods_dir, jar_name)  #762 (line in Coconut source)
        os.rename(current_jar_path, new_jar_path)  #763 (line in Coconut source)



def make_dirs(*dirs):  #766 (line in Coconut source)
    for d in dirs:  #767 (line in Coconut source)
        if not os.path.exists(d):  #768 (line in Coconut source)
            os.mkdir(d)  #769 (line in Coconut source)



def update_mods(mods_dir, updated_mods_dir, old_mods_dir, dry_run=False, interact=None, google=False, config=MOD_CONFIG):  #772 (line in Coconut source)
    if interact is None and not PRINT_DEBUG:  #773 (line in Coconut source)
        interact = False  #774 (line in Coconut source)
    try:  #775 (line in Coconut source)
        mod_names_to_jar_names = get_mod_names_to_jar_names(mods_dir, file_extension=config.file_extension)  #776 (line in Coconut source)
        mod_names_to_curseforge_names, nulled_mods = get_curseforge_names_for(mod_names_to_jar_names, google=google)  #777 (line in Coconut source)
        if not dry_run:  #778 (line in Coconut source)
            mod_names_to_curseforge_ids, missing_ids_mods = get_mod_names_to_curseforge_ids(mod_names_to_curseforge_names, config=config)  #779 (line in Coconut source)
            mod_names_to_latest_versions, missing_files_mods = get_mod_names_to_latest_versions(mod_names_to_curseforge_ids, mod_names_to_jar_names, config=config)  #780 (line in Coconut source)
            updated_mod_names_to_files = get_updated_mod_names_to_files(mod_names_to_jar_names, mod_names_to_latest_versions)  #781 (line in Coconut source)
            if updated_mod_names_to_files:  #782 (line in Coconut source)
                make_dirs(updated_mods_dir, old_mods_dir)  #783 (line in Coconut source)
                update_files(updated_mod_names_to_files, updated_mods_dir)  #784 (line in Coconut source)
                move_old_files(updated_mod_names_to_files, mod_names_to_jar_names, mods_dir, old_mods_dir)  #785 (line in Coconut source)
        else:  #786 (line in Coconut source)
            missing_ids_mods = []  #787 (line in Coconut source)
            missing_files_mods = []  #788 (line in Coconut source)
        return nulled_mods + missing_ids_mods + missing_files_mods  #789 (line in Coconut source)
    except Exception:  #790 (line in Coconut source)
        if interact is not False:  #791 (line in Coconut source)
            traceback.print_exc()  #792 (line in Coconut source)

            from coconut import embed  #794 (line in Coconut source)
            embed()  #795 (line in Coconut source)
        raise  #796 (line in Coconut source)
    if interact:  #797 (line in Coconut source)
        from coconut import embed  #798 (line in Coconut source)
        embed()  #799 (line in Coconut source)



def update_all(mods_dirs, config=MOD_CONFIG, **kwargs):  #802 (line in Coconut source)
    couldnt_update = []  #803 (line in Coconut source)
    for mods_dir in mods_dirs:  #804 (line in Coconut source)
        if not os.path.exists(mods_dir):  #805 (line in Coconut source)
            print("Skipping non-existent directory: {_coconut_format_0}".format(_coconut_format_0=(mods_dir)))  #806 (line in Coconut source)
            continue  #807 (line in Coconut source)
        updated_mods_dir = mods_dir + UPDATED_MODS_DIR_SUFFIX  #808 (line in Coconut source)
        old_mods_dir = mods_dir + OLD_MODS_DIR_SUFFIX  #809 (line in Coconut source)
        couldnt_update += update_mods(mods_dir, updated_mods_dir, old_mods_dir, config=config, **kwargs)  #810 (line in Coconut source)
    config_name = config.name if kwargs.get("config") is not None else "mod"  #811 (line in Coconut source)
    for mod_name in couldnt_update:  #812 (line in Coconut source)
        print("Unable to automatically update {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(config_name), _coconut_format_1=(mod_name)))  #813 (line in Coconut source)



@_coconut_tco  #816 (line in Coconut source)
def parse_args():  #816 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Update mods and datapacks from CurseForge to their latest versions.")  #817 (line in Coconut source)
    parser.add_argument("--dry-run", action="store_true", help="Only check for missing CurseForge name mappings without downloading updates")  #820 (line in Coconut source)
    parser.add_argument("--google", action="store_true", help="Use Google search to find CurseForge names for unknown mods")  #825 (line in Coconut source)
    parser.add_argument("--mods-only", action="store_true", help="Only update mods, skip datapacks")  #830 (line in Coconut source)
    parser.add_argument("--datapacks-only", action="store_true", help="Only update datapacks, skip mods")  #835 (line in Coconut source)
    parser.add_argument("--update-only-deduplicate", action="store_true", help="Update deduplicate directories instead of normal mod directories")  #840 (line in Coconut source)
    return _coconut_tail_call(parser.parse_args)  #845 (line in Coconut source)



def main():  #848 (line in Coconut source)
    args = parse_args()  #849 (line in Coconut source)

    sync_mods.main()  #851 (line in Coconut source)

# Just update deduplicate dirs if --update-only-deduplicate
    if args.update_only_deduplicate:  #854 (line in Coconut source)
        print("\n" + "=" * 60)  #855 (line in Coconut source)
        print("UPDATING DEDUPLICATE DIRECTORIES")  #856 (line in Coconut source)
        print("=" * 60 + "\n")  #857 (line in Coconut source)
        update_all(UPDATE_DEDUPLICATE_DIRS, dry_run=args.dry_run, google=args.google, config=MOD_CONFIG)  #858 (line in Coconut source)
        return  #864 (line in Coconut source)

# Update mods (unless --datapacks-only)
    if not args.datapacks_only:  #867 (line in Coconut source)
        print("\n" + "=" * 60)  #868 (line in Coconut source)
        print("UPDATING MODS")  #869 (line in Coconut source)
        print("=" * 60 + "\n")  #870 (line in Coconut source)
        update_all(UPDATE_MODS_DIRS, dry_run=args.dry_run, google=args.google, config=MOD_CONFIG)  #871 (line in Coconut source)

# Update datapacks (unless --mods-only or --update-only-deduplicate)
    if not args.mods_only and not args.only_update_deduplicate:  #879 (line in Coconut source)
        print("\n" + "=" * 60)  #880 (line in Coconut source)
        print("UPDATING DATAPACKS")  #881 (line in Coconut source)
        print("=" * 60 + "\n")  #882 (line in Coconut source)
        update_all(UPDATE_DATAPACK_DIRS, dry_run=args.dry_run, google=args.google, config=DATAPACK_CONFIG)  #883 (line in Coconut source)



if __name__ == "__main__":  #891 (line in Coconut source)
    main()  #892 (line in Coconut source)
