#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa59a9e20

# Compiled with Coconut version 3.2.0-post_dev1

"""Entry point to commit or revert pending mod/datapack updates.

After update_mods.coco runs, it creates:
- {mods_dir}-updates: Contains newly downloaded mod/datapack versions
- {mods_dir}-old: Contains old mod/datapack versions that were replaced

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
import sys  #14 (line in Coconut source)
import shutil  #15 (line in Coconut source)
import argparse  #16 (line in Coconut source)
import time  #17 (line in Coconut source)
import subprocess  #18 (line in Coconut source)

from minecraft_server_tools.constants import UPDATED_MODS_DIR_SUFFIX  #20 (line in Coconut source)
from minecraft_server_tools.constants import OLD_MODS_DIR_SUFFIX  #20 (line in Coconut source)
from minecraft_server_tools.update_mods import UPDATE_MODS_DIRS  #24 (line in Coconut source)
from minecraft_server_tools.update_mods import UPDATE_DATAPACK_DIRS  #24 (line in Coconut source)
from minecraft_server_tools.sync_mods import get_location_table_for  #25 (line in Coconut source)
from minecraft_server_tools.sync_mods import display_mod_path  #25 (line in Coconut source)

# Combined list of all directories to check for pending updates
ALL_UPDATE_DIRS = UPDATE_MODS_DIRS + UPDATE_DATAPACK_DIRS  #28 (line in Coconut source)


def get_update_dirs(mods_dir):  #31 (line in Coconut source)
    """Return (updates_dir, old_dir) paths for a given mods directory."""  #32 (line in Coconut source)
    return (mods_dir + UPDATED_MODS_DIR_SUFFIX, mods_dir + OLD_MODS_DIR_SUFFIX)  #33 (line in Coconut source)



def has_pending_updates(mods_dir):  #39 (line in Coconut source)
    """Check if a mods directory has pending update directories (even if empty)."""  #40 (line in Coconut source)
    updates_dir, old_dir = get_update_dirs(mods_dir)  #41 (line in Coconut source)
    return os.path.exists(updates_dir) or os.path.exists(old_dir)  #42 (line in Coconut source)



@_coconut_tco  #45 (line in Coconut source)
def any_pending_dirs():  #45 (line in Coconut source)
    """Check if any mods/datapack directory has pending update directories."""  #46 (line in Coconut source)
    return _coconut_tail_call(any, (has_pending_updates(d) for d in ALL_UPDATE_DIRS))  #47 (line in Coconut source)



def move_mod(from_path, to_path):  #50 (line in Coconut source)
    """Move a single file with nice printing."""  #51 (line in Coconut source)
    print("  Moving {mod} from {src}...".format(mod=display_mod_path(to_path), src=display_mod_path(from_path)))  #52 (line in Coconut source)
    os.makedirs(os.path.dirname(to_path), exist_ok=True)  #56 (line in Coconut source)
    if os.path.exists(to_path):  #57 (line in Coconut source)
        os.remove(to_path)  #58 (line in Coconut source)
    shutil.move(from_path, to_path)  #59 (line in Coconut source)



def move_mods_from_to(source_table, dest_dir):  #62 (line in Coconut source)
    """Move all files from source locations to dest_dir."""  #63 (line in Coconut source)
    dest_table = get_location_table_for(dest_dir)  #64 (line in Coconut source)
    for name, src_path in source_table.items():  #65 (line in Coconut source)
        new_path = os.path.join(dest_dir, name)  #66 (line in Coconut source)
        if name in dest_table:  #67 (line in Coconut source)
            print("  Overwriting: {_coconut_format_0}".format(_coconut_format_0=(name)))  #68 (line in Coconut source)
            os.remove(dest_table[name])  #69 (line in Coconut source)
        move_mod(src_path, new_path)  #70 (line in Coconut source)



def remove_file_with_retry(filepath, max_retries=5, initial_delay=0.2):  #73 (line in Coconut source)
    """Remove a single file with retry logic for Windows file locking."""  #74 (line in Coconut source)
    delay = initial_delay  #75 (line in Coconut source)
    for attempt in range(max_retries):  #76 (line in Coconut source)
        try:  #77 (line in Coconut source)
            os.remove(filepath)  #78 (line in Coconut source)
            return True  #79 (line in Coconut source)
        except PermissionError:  #80 (line in Coconut source)
            if attempt < max_retries - 1:  #81 (line in Coconut source)
                time.sleep(delay)  #82 (line in Coconut source)
                delay *= 2  #83 (line in Coconut source)
    return False  #84 (line in Coconut source)



def remove_dir_if_exists(directory, max_retries=5, initial_delay=0.1):  #87 (line in Coconut source)
    """Remove a directory if it exists.

    Uses a multi-strategy approach for Windows/OneDrive file locking:
    1. Remove all files individually with retries
    2. Try os.rmdir() for the empty directory
    3. Fall back to Windows rmdir command if needed
    4. Retry with exponential backoff
    """  #95 (line in Coconut source)
    if not os.path.exists(directory):  #96 (line in Coconut source)
        return  #97 (line in Coconut source)

    dir_name = os.path.basename(directory)  #99 (line in Coconut source)

# First, remove all files individually
    for filename in os.listdir(directory):  #102 (line in Coconut source)
        filepath = os.path.join(directory, filename)  #103 (line in Coconut source)
        if os.path.isfile(filepath):  #104 (line in Coconut source)
            if not remove_file_with_retry(filepath):  #105 (line in Coconut source)
                print("  Warning: Could not remove file {_coconut_format_0}".format(_coconut_format_0=(filename)))  #106 (line in Coconut source)

# Now try to remove the empty directory with retries
    delay = initial_delay  #109 (line in Coconut source)
    for attempt in range(max_retries):  #110 (line in Coconut source)
        try:  #111 (line in Coconut source)
# Check if directory is empty
            remaining = os.listdir(directory)  #113 (line in Coconut source)
            if remaining:  #114 (line in Coconut source)
                print("  Warning: Directory {_coconut_format_0} not empty: {_coconut_format_1}".format(_coconut_format_0=(dir_name), _coconut_format_1=(remaining)))  #115 (line in Coconut source)
                return  #116 (line in Coconut source)

            os.rmdir(directory)  #118 (line in Coconut source)
            print("  Removed directory: {_coconut_format_0}".format(_coconut_format_0=(dir_name)))  #119 (line in Coconut source)
            return  #120 (line in Coconut source)
        except PermissionError:  #121 (line in Coconut source)
# On Windows, try using rmdir command as fallback
            if sys.platform == "win32" and attempt == max_retries // 2:  #123 (line in Coconut source)
                try:  #124 (line in Coconut source)
                    subprocess.run(["cmd", "/c", "rmdir", "/s", "/q", directory], check=True, capture_output=True)  #125 (line in Coconut source)
                    if not os.path.exists(directory):  #130 (line in Coconut source)
                        print("  Removed directory: {_coconut_format_0} (via rmdir)".format(_coconut_format_0=(dir_name)))  #131 (line in Coconut source)
                        return  #132 (line in Coconut source)
                except subprocess.CalledProcessError:  #133 (line in Coconut source)
                    pass  #134 (line in Coconut source)

            if attempt < max_retries - 1:  #136 (line in Coconut source)
                time.sleep(delay)  #137 (line in Coconut source)
                delay = min(delay * 1.5, 5.0)  # cap at 5 seconds  #138 (line in Coconut source)
            else:  #139 (line in Coconut source)
                print("  Warning: Could not remove {_coconut_format_0} - may be locked by OneDrive".format(_coconut_format_0=(dir_name)))  #140 (line in Coconut source)
        except OSError as e:  #141 (line in Coconut source)
            if attempt < max_retries - 1:  #142 (line in Coconut source)
                time.sleep(delay)  #143 (line in Coconut source)
                delay = min(delay * 1.5, 5.0)  #144 (line in Coconut source)
            else:  #145 (line in Coconut source)
                print("  Warning: Could not remove {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(dir_name), _coconut_format_1=(e)))  #146 (line in Coconut source)



def show_pending_updates():  #149 (line in Coconut source)
    """Show all pending updates across all mods/datapack directories."""  #150 (line in Coconut source)
    has_any = False  #151 (line in Coconut source)
    for mods_dir in ALL_UPDATE_DIRS:  #152 (line in Coconut source)
        updates_dir, old_dir = get_update_dirs(mods_dir)  #153 (line in Coconut source)
        updates_table = get_location_table_for(updates_dir)  #154 (line in Coconut source)
        old_table = get_location_table_for(old_dir)  #155 (line in Coconut source)

        if updates_table or old_table:  #157 (line in Coconut source)
            has_any = True  #158 (line in Coconut source)
            dir_name = os.path.basename(mods_dir)  #159 (line in Coconut source)
            print("\n{_coconut_format_0}:".format(_coconut_format_0=(dir_name)))  #160 (line in Coconut source)
            if updates_table:  #161 (line in Coconut source)
                print("  New versions ({_coconut_format_0} files):".format(_coconut_format_0=(len(updates_table))))  #162 (line in Coconut source)
                for f in sorted(updates_table.keys()):  #163 (line in Coconut source)
                    print("    + {_coconut_format_0}".format(_coconut_format_0=(f)))  #164 (line in Coconut source)
            if old_table:  #165 (line in Coconut source)
                print("  Old versions ({_coconut_format_0} files):".format(_coconut_format_0=(len(old_table))))  #166 (line in Coconut source)
                for f in sorted(old_table.keys()):  #167 (line in Coconut source)
                    print("    - {_coconut_format_0}".format(_coconut_format_0=(f)))  #168 (line in Coconut source)

    if not has_any:  #170 (line in Coconut source)
        print("No pending updates found.")  #171 (line in Coconut source)
    return has_any  #172 (line in Coconut source)



def commit_updates():  #175 (line in Coconut source)
    """Commit all pending updates by moving new versions into main folders."""  #176 (line in Coconut source)
    print("\nCommitting updates...")  #177 (line in Coconut source)

    for mods_dir in ALL_UPDATE_DIRS:  #179 (line in Coconut source)
        updates_dir, old_dir = get_update_dirs(mods_dir)  #180 (line in Coconut source)

        if not has_pending_updates(mods_dir):  #182 (line in Coconut source)
            continue  #183 (line in Coconut source)

        dir_name = os.path.basename(mods_dir)  #185 (line in Coconut source)
        print("\n{_coconut_format_0}:".format(_coconut_format_0=(dir_name)))  #186 (line in Coconut source)

# Move files from updates into the main folder
        updates_table = get_location_table_for(updates_dir)  #189 (line in Coconut source)
        if updates_table:  #190 (line in Coconut source)
            move_mods_from_to(updates_table, mods_dir)  #191 (line in Coconut source)

# Remove both -updates and -old directories
        remove_dir_if_exists(updates_dir)  #194 (line in Coconut source)
        remove_dir_if_exists(old_dir)  #195 (line in Coconut source)

    print("\nUpdates committed successfully.")  #197 (line in Coconut source)



def revert_updates():  #200 (line in Coconut source)
    """Revert all pending updates by restoring old versions into main folders."""  #201 (line in Coconut source)
    print("\nReverting updates (reverting to old versions)...")  #202 (line in Coconut source)

    for mods_dir in ALL_UPDATE_DIRS:  #204 (line in Coconut source)
        updates_dir, old_dir = get_update_dirs(mods_dir)  #205 (line in Coconut source)

        if not has_pending_updates(mods_dir):  #207 (line in Coconut source)
            continue  #208 (line in Coconut source)

        dir_name = os.path.basename(mods_dir)  #210 (line in Coconut source)
        print("\n{_coconut_format_0}:".format(_coconut_format_0=(dir_name)))  #211 (line in Coconut source)

# Move files from old back into the main folder
        old_table = get_location_table_for(old_dir)  #214 (line in Coconut source)
        if old_table:  #215 (line in Coconut source)
            move_mods_from_to(old_table, mods_dir)  #216 (line in Coconut source)

# Remove both -updates and -old directories
        remove_dir_if_exists(updates_dir)  #219 (line in Coconut source)
        remove_dir_if_exists(old_dir)  #220 (line in Coconut source)

    print("\nUpdates reverted successfully (reverted to old versions).")  #222 (line in Coconut source)



@_coconut_tco  #225 (line in Coconut source)
def parse_args():  #225 (line in Coconut source)
    parser = argparse.ArgumentParser(description="Commit or revert pending mod/datapack updates.")  #226 (line in Coconut source)
    subparsers = parser.add_subparsers(dest="command", help="Available commands")  #229 (line in Coconut source)

    subparsers.add_parser("status", help="Show pending updates")  #231 (line in Coconut source)
    subparsers.add_parser("commit", help="Apply updates (keep new versions)")  #235 (line in Coconut source)
    subparsers.add_parser("revert", help="Discard updates (revert to old versions)")  #239 (line in Coconut source)

    return _coconut_tail_call(parser.parse_args)  #244 (line in Coconut source)



def main():  #247 (line in Coconut source)
    args = parse_args()  #248 (line in Coconut source)

    if args.command is None or args.command == "status":  #250 (line in Coconut source)
        show_pending_updates()  #251 (line in Coconut source)
    elif args.command == "commit":  #252 (line in Coconut source)
        has_files = show_pending_updates()  #253 (line in Coconut source)
        if has_files or any_pending_dirs():  #254 (line in Coconut source)
            print()  #255 (line in Coconut source)
            commit_updates()  #256 (line in Coconut source)
    elif args.command == "revert":  #257 (line in Coconut source)
        has_files = show_pending_updates()  #258 (line in Coconut source)
        if has_files or any_pending_dirs():  #259 (line in Coconut source)
            print()  #260 (line in Coconut source)
            revert_updates()  #261 (line in Coconut source)



if __name__ == "__main__":  #264 (line in Coconut source)
    main()  #265 (line in Coconut source)
