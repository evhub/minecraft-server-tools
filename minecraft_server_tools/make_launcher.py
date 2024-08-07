#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf2cb9b39

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

from minecraft_server_tools import install_client  #3 (line in Coconut source)
from minecraft_server_tools import launch_server  #3 (line in Coconut source)
from minecraft_server_tools.constants import WINDOWS  #4 (line in Coconut source)
from minecraft_server_tools.constants import ROOT_DIR  #4 (line in Coconut source)
from minecraft_server_tools.constants import MODPACK_NAME  #4 (line in Coconut source)
from minecraft_server_tools.constants import first_that_exists  #4 (line in Coconut source)
from minecraft_server_tools.constants import fixpath  #4 (line in Coconut source)


@_coconut_tco  #13 (line in Coconut source)
def get_custom_launcher_path():  #13 (line in Coconut source)
    desktop_dir = None  #14 (line in Coconut source)
    if WINDOWS:  #15 (line in Coconut source)
        desktop_dir = (_coconut_iter_getitem((((launch_server.get_cmd_output)(["powershell", "-Command", '[Environment]::GetFolderPath("Desktop")'])).splitlines()), (-1)))  #16 (line in Coconut source)
        if not os.path.exists(desktop_dir):  #22 (line in Coconut source)
            print("\tWARNING: Failed to locate Desktop at {_coconut_format_0!r}.".format(_coconut_format_0=(desktop_dir)))  #23 (line in Coconut source)
            desktop_dir = None  #24 (line in Coconut source)
    if desktop_dir is None:  #25 (line in Coconut source)
        desktop_dir = first_that_exists(["~/Desktop", "~/OneDrive/Desktop"])  #26 (line in Coconut source)
    return _coconut_tail_call(fixpath, os.path.join(desktop_dir, MODPACK_NAME + (".bat" if WINDOWS else ".sh")))  #30 (line in Coconut source)



def make_launcher_file(do_optional=False, do_barrel_roll=True):  #36 (line in Coconut source)
    """Create the launcher script."""  #37 (line in Coconut source)
    print("\nCreating custom launcher...")  #38 (line in Coconut source)
    launcher_path = get_custom_launcher_path()  #39 (line in Coconut source)
    install_client_args = ["--launch", "--no-zip"]  #40 (line in Coconut source)
    if do_optional is not None:  #41 (line in Coconut source)
        install_client_args += ["--yes-optional" if do_optional else "--no-optional",]  #42 (line in Coconut source)
    if do_barrel_roll is not None:  #43 (line in Coconut source)
        install_client_args += ["--yes-barrel-roll" if do_barrel_roll else "--no-barrel-roll",]  #44 (line in Coconut source)
    contents = """
cd "{_coconut_format_0}"
git pull
py -3 -m pip install -Ue .
py -3 -m minecraft_server_tools.install_client {_coconut_format_1}
    """.format(_coconut_format_0=(ROOT_DIR), _coconut_format_1=(" ".join(install_client_args))).strip()  #50 (line in Coconut source)
    with open(launcher_path, "w") as new_launcher_file:  #51 (line in Coconut source)
        new_launcher_file.write(contents)  #52 (line in Coconut source)
    if not WINDOWS:  #53 (line in Coconut source)
        launch_server.run_cmd(["chmod", "+x", launcher_path])  #54 (line in Coconut source)
    print("\tWrote custom launcher to: {_coconut_format_0}".format(_coconut_format_0=(launcher_path)))  #55 (line in Coconut source)



def main():  #58 (line in Coconut source)
    do_optional, do_barrel_roll = install_client.main()  #59 (line in Coconut source)
    make_launcher_file(do_optional=False, do_barrel_roll=do_barrel_roll)  #60 (line in Coconut source)



if __name__ == "__main__":  #63 (line in Coconut source)
    main()  #64 (line in Coconut source)
