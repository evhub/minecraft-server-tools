#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x77d229fb

# Compiled with Coconut version 3.2.0-post_dev1

"""Entry point to commit or revert pending mod updates.

After update_mods.coco runs, it creates:
- {mods_dir}-updates: Contains newly downloaded mod versions
- {mods_dir}-old: Contains old mod versions that were replaced

This script allows you to either:
- commit: Move updates into the main folders (keeping new versions)
- revert: Move old versions back into main folders (reverting to old versions)

In either case, the -updates and -old folders are deleted afterward.
"""

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


import os  #13 (line in Coconut source)
import shutil  #14 (line in Coconut source)
import argparse  #15 (line in Coconut source)
import time  #16 (line in Coconut source)

from minecraft_server_tools.constants import UPDATED_MODS_DIR_SUFFIX  #18 (line in Coconut source)
from minecraft_server_tools.constants import OLD_MODS_DIR_SUFFIX  #18 (line in Coconut source)
from minecraft_server_tools.update_mods import UPDATE_MODS_DIRS  #22 (line in Coconut source)


def get_update_dirs(mods_dir):  #25 (line in Coconut source)
    """Return (updates_dir, old_dir) paths for a given mods directory."""  #26 (line in Coconut source)
    return (mods_dir + UPDATED_MODS_DIR_SUFFIX, mods_dir + OLD_MODS_DIR_SUFFIX)  #27 (line in Coconut source)



def has_pending_updates(mods_dir):  #33 (line in Coconut source)
    """Check if a mods directory has pending updates."""  #34 (line in Coconut source)
    updates_dir, old_dir = get_update_dirs(mods_dir)  #35 (line in Coconut source)
    return os.path.exists(updates_dir) or os.path.exists(old_dir)  #36 (line in Coconut source)



def list_files(directory):  #39 (line in Coconut source)
    """List all files in a directory."""  #40 (line in Coconut source)
    if not os.path.exists(directory):  #41 (line in Coconut source)
        return []  #42 (line in Coconut source)
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]  #43 (line in Coconut source)



def move_files(src_dir, dst_dir):  #46 (line in Coconut source)
    """Move all files from src_dir to dst_dir."""  #47 (line in Coconut source)
    if not os.path.exists(src_dir):  #48 (line in Coconut source)
        return  #49 (line in Coconut source)
    for filename in list_files(src_dir):  #50 (line in Coconut source)
        src_path = os.path.join(src_dir, filename)  #51 (line in Coconut source)
        dst_path = os.path.join(dst_dir, filename)  #52 (line in Coconut source)
        if os.path.exists(dst_path):  #53 (line in Coconut source)
            print("  Overwriting: {_coconut_format_0}".format(_coconut_format_0=(filename)))  #54 (line in Coconut source)
            os.remove(dst_path)  #55 (line in Coconut source)
        else:  #56 (line in Coconut source)
            print("  Moving: {_coconut_format_0}".format(_coconut_format_0=(filename)))  #57 (line in Coconut source)
        shutil.move(src_path, dst_path)  #58 (line in Coconut source)



def remove_dir_if_exists(directory, max_retries=5, initial_delay=0.5):  #61 (line in Coconut source)
    """Remove a directory if it exists.

    Includes retry logic for Windows file locking issues (e.g., OneDrive sync).
    """  #65 (line in Coconut source)
    if not os.path.exists(directory):  #66 (line in Coconut source)
        return  #67 (line in Coconut source)

    delay = initial_delay  #69 (line in Coconut source)
    for attempt in range(max_retries):  #70 (line in Coconut source)
        try:  #71 (line in Coconut source)
            shutil.rmtree(directory)  #72 (line in Coconut source)
            print("  Removed directory: {_coconut_format_0}".format(_coconut_format_0=(os.path.basename(directory))))  #73 (line in Coconut source)
            return  #74 (line in Coconut source)
        except PermissionError as e:  #75 (line in Coconut source)
            if attempt < max_retries - 1:  #76 (line in Coconut source)
                print("  Retry {_coconut_format_0}/{_coconut_format_1}: waiting {_coconut_format_2:.1f}s for {_coconut_format_3}...".format(_coconut_format_0=(attempt + 1), _coconut_format_1=(max_retries), _coconut_format_2=(delay), _coconut_format_3=(os.path.basename(directory))))  #77 (line in Coconut source)
                time.sleep(delay)  #78 (line in Coconut source)
                delay *= 2  # exponential backoff  #79 (line in Coconut source)
            else:  #80 (line in Coconut source)
                print("  Warning: Could not remove {_coconut_format_0} after {_coconut_format_1} attempts: {_coconut_format_2}".format(_coconut_format_0=(os.path.basename(directory)), _coconut_format_1=(max_retries), _coconut_format_2=(e)))  #81 (line in Coconut source)
                print("  You may need to manually delete: {_coconut_format_0}".format(_coconut_format_0=(directory)))  #82 (line in Coconut source)



def show_pending_updates():  #85 (line in Coconut source)
    """Show all pending updates across all mods directories."""  #86 (line in Coconut source)
    has_any = False  #87 (line in Coconut source)
    for mods_dir in UPDATE_MODS_DIRS:  #88 (line in Coconut source)
        updates_dir, old_dir = get_update_dirs(mods_dir)  #89 (line in Coconut source)
        updates_files = list_files(updates_dir)  #90 (line in Coconut source)
        old_files = list_files(old_dir)  #91 (line in Coconut source)

        if updates_files or old_files:  #93 (line in Coconut source)
            has_any = True  #94 (line in Coconut source)
            dir_name = os.path.basename(mods_dir)  #95 (line in Coconut source)
            print("\n{_coconut_format_0}:".format(_coconut_format_0=(dir_name)))  #96 (line in Coconut source)
            if updates_files:  #97 (line in Coconut source)
                print("  New versions ({_coconut_format_0} files):".format(_coconut_format_0=(len(updates_files))))  #98 (line in Coconut source)
                for f in sorted(updates_files):  #99 (line in Coconut source)
                    print("    + {_coconut_format_0}".format(_coconut_format_0=(f)))  #100 (line in Coconut source)
            if old_files:  #101 (line in Coconut source)
                print("  Old versions ({_coconut_format_0} files):".format(_coconut_format_0=(len(old_files))))  #102 (line in Coconut source)
                for f in sorted(old_files):  #103 (line in Coconut source)
                    print("    - {_coconut_format_0}".format(_coconut_format_0=(f)))  #104 (line in Coconut source)

    if not has_any:  #106 (line in Coconut source)
        print("No pending updates found.")  #107 (line in Coconut source)
    return has_any  #108 (line in Coconut source)



def commit_updates():  #111 (line in Coconut source)
    """Commit all pending updates by moving new versions into main folders."""  #112 (line in Coconut source)
    print("\nCommitting updates...")  #113 (line in Coconut source)

    for mods_dir in UPDATE_MODS_DIRS:  #115 (line in Coconut source)
        updates_dir, old_dir = get_update_dirs(mods_dir)  #116 (line in Coconut source)

        if not has_pending_updates(mods_dir):  #118 (line in Coconut source)
            continue  #119 (line in Coconut source)

        dir_name = os.path.basename(mods_dir)  #121 (line in Coconut source)
        print("\n{_coconut_format_0}:".format(_coconut_format_0=(dir_name)))  #122 (line in Coconut source)

# Move files from updates into the main folder
        move_files(updates_dir, mods_dir)  #125 (line in Coconut source)

# Remove both -updates and -old directories
        remove_dir_if_exists(updates_dir)  #128 (line in Coconut source)
        remove_dir_if_exists(old_dir)  #129 (line in Coconut source)

    print("\nUpdates committed successfully.")  #131 (line in Coconut source)



def revert_updates():  #134 (line in Coconut source)
    """Revert all pending updates by restoring old versions into main folders."""  #135 (line in Coconut source)
    print("\nReverting updates (reverting to old versions)...")  #136 (line in Coconut source)

    for mods_dir in UPDATE_MODS_DIRS:  #138 (line in Coconut source)
        updates_dir, old_dir = get_update_dirs(mods_dir)  #139 (line in Coconut source)

        if not has_pending_updates(mods_dir):  #141 (line in Coconut source)
            continue  #142 (line in Coconut source)

        dir_name = os.path.basename(mods_dir)  #144 (line in Coconut source)
        print("\n{_coconut_format_0}:".format(_coconut_format_0=(dir_name)))  #145 (line in Coconut source)

# Move files from old back into the main folder
        move_files(old_dir, mods_dir)  #148 (line in Coconut source)

# Remove both -updates and -old directories
        remove_dir_if_exists(updates_dir)  #151 (line in Coconut source)
        remove_dir_if_exists(old_dir)  #152 (line in Coconut source)

    print("\nUpdates reverted successfully (reverted to old versions).")  #154 (line in Coconut source)



@_coconut_tco  #157 (line in Coconut source)
def parse_args():  #157 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Commit or revert pending mod updates.")  #158 (line in Coconut source)
    subparsers = parser.add_subparsers(dest="command", help="Available commands")  #161 (line in Coconut source)

    subparsers.add_parser("status", help="Show pending updates")  #163 (line in Coconut source)
    subparsers.add_parser("commit", help="Apply updates (keep new versions)")  #167 (line in Coconut source)
    subparsers.add_parser("revert", help="Discard updates (revert to old versions)")  #171 (line in Coconut source)

    return _coconut_tail_call(parser.parse_args)  #176 (line in Coconut source)



def main():  #179 (line in Coconut source)
    args = parse_args()  #180 (line in Coconut source)

    if args.command is None or args.command == "status":  #182 (line in Coconut source)
        show_pending_updates()  #183 (line in Coconut source)
    elif args.command == "commit":  #184 (line in Coconut source)
        if show_pending_updates():  #185 (line in Coconut source)
            print()  #186 (line in Coconut source)
            commit_updates()  #187 (line in Coconut source)
    elif args.command == "revert":  #188 (line in Coconut source)
        if show_pending_updates():  #189 (line in Coconut source)
            print()  #190 (line in Coconut source)
            revert_updates()  #191 (line in Coconut source)



if __name__ == "__main__":  #194 (line in Coconut source)
    main()  #195 (line in Coconut source)
