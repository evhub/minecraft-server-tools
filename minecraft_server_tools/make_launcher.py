#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd0378c59

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

from minecraft_server_tools import install_client  #3 (line in Coconut source)
from minecraft_server_tools.constants import WINDOWS  #4 (line in Coconut source)
from minecraft_server_tools.constants import ROOT_DIR  #4 (line in Coconut source)
from minecraft_server_tools.constants import LAUNCHER_FILE  #4 (line in Coconut source)
from minecraft_server_tools.constants import NEW_LAUNCHER_PATH  #4 (line in Coconut source)

OPEN_CMD = "" if WINDOWS else "open "  #11 (line in Coconut source)


@_coconut_tco  #14 (line in Coconut source)
def get_launcher_file_contents(install_client_args=""):  #14 (line in Coconut source)
    """Get the contents that should go in the launcher script."""  #15 (line in Coconut source)
    if not os.path.exists(LAUNCHER_FILE):  #16 (line in Coconut source)
        raise OSError("Could not find Minecraft Launcher file!\n\nMod files have still been installed, but custom launcher creation failed. You'll need to keep running this script every time before you launch Minecraft.")  #17 (line in Coconut source)
    print("\tIdentified Minecraft Launcher location as: {_coconut_format_0!r}".format(_coconut_format_0=(LAUNCHER_FILE)))  #18 (line in Coconut source)
    return _coconut_tail_call("""
cd "{_coconut_format_0}"
git pull
py -3 -m pip install -Ue .
py -3 -m minecraft_server_tools.install_client{_coconut_format_1}
{_coconut_format_2}"{_coconut_format_3}"
    """.format(_coconut_format_0=(ROOT_DIR), _coconut_format_1=(install_client_args), _coconut_format_2=(OPEN_CMD), _coconut_format_3=(LAUNCHER_FILE)).strip)  #25 (line in Coconut source)



def make_launcher_file(do_optional=False):  #28 (line in Coconut source)
    """Create the launcher script."""  #29 (line in Coconut source)
    if do_optional is None:  #30 (line in Coconut source)
        install_client_args = ""  #31 (line in Coconut source)
    elif do_optional:  #32 (line in Coconut source)
        install_client_args = " --yes-optional"  #33 (line in Coconut source)
    else:  #34 (line in Coconut source)
        install_client_args = " --no-optional"  #35 (line in Coconut source)
    print("\nWriting mod launcher to {_coconut_format_0!r}...".format(_coconut_format_0=(NEW_LAUNCHER_PATH)))  #36 (line in Coconut source)
    contents = get_launcher_file_contents(install_client_args)  #37 (line in Coconut source)
    with open(NEW_LAUNCHER_PATH, "w") as new_launcher_file:  #38 (line in Coconut source)
        new_launcher_file.write(contents)  #39 (line in Coconut source)



def main():  #42 (line in Coconut source)
    install_client.main()  #43 (line in Coconut source)
    make_launcher_file()  #44 (line in Coconut source)



if __name__ == "__main__":  #47 (line in Coconut source)
    main()  #48 (line in Coconut source)
