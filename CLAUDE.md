# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minecraft Server Tools is a Python utility suite for managing Minecraft Forge/NeoForge servers with large mod collections. Key features include mod installation/synchronization, CurseForge API integration, launcher profile management, and JVM optimization.

## Build and Development Commands

**Important:** There are two directories to be aware of:
- **This repository** (`minecraft-server-tools/`) - Edit source code here, run `make build` to compile
- **Server directory** (`constants.SERVER_DIR`, typically `~/OneDrive/Minecraft/"1.21 Mod Server"`) - Run operational commands like `make update-mods` and `make update-mod-names` here

### In this repository:
```bash
# Compile Coconut source to Python (required before running)
make build

# Watch mode - auto-recompile on changes
make watch

# Install locally for development
make local-install

# Clean Coconut cache
make clean
```

### In the server directory:
```bash
cd ~/OneDrive/Minecraft/"1.21 Mod Server"

# Update/download mods from CurseForge
make update-mods

# Update mod name mappings (dry-run mode)
make update-mod-names
```

## Architecture

### Source Code Structure

- **`minecraft_server_tools-source/`** - Coconut source files (.coco) - edit these
- **`minecraft_server_tools/`** - Compiled Python output (.py) - generated, do not edit directly

### Key Modules

- `constants.coco` - Centralized configuration: Minecraft/Forge versions, paths, JVM args, CurseForge settings
- `update_mods.coco` - Main orchestrator for downloading/updating mods from CurseForge
- `sync_mods.coco` - Synchronizes mod files between directories
- `install_client.coco` - Installs Minecraft client with mods and configs
- `launch_server.coco` - Launches server with optimized JVM settings
- `binary_search.coco` - Finds incompatible mods via binary search elimination

### CurseForge Integration

- `curseforge_api.js` - Node.js wrapper for CurseForge API queries
- `curseforge_names.json` - Cached CurseForge mod name mappings
- Requires `CURSEFORGE_API_KEY` environment variable (or `secrets.json` in server dir)

## Language: Coconut

This project uses [Coconut](http://coconut-lang.org/), a functional programming superset of Python. Key points:

- Source files use `.coco` extension
- Compiles to Python 3 with `--strict` mode
- Uses Coconut-specific syntax: `then`/`else` ternaries, pattern matching, pipeline operators
- Always run `make build` after editing `.coco` files

## Configuration

Key constants in `constants.coco`:
- `MC_VERSION` / `FORGE_VERSION` - Current Minecraft and NeoForge versions
- `SERVER_DIR` - Server installation path (from env `MINECRAFT_SERVER_DIR` or default)
- `CLIENT_RAM` / `SERVER_RAM` - Memory allocation (auto-adjusted based on system RAM)
- `MODLOADER` - Currently "NeoForge"

## Entry Points

Run as Python modules after building, e.g.:
```bash
python -m minecraft_server_tools.update_mods
python -m minecraft_server_tools.install_client
python -m minecraft_server_tools.launch_server
python -m minecraft_server_tools.sync_mods
```

## Updating Mod Name Mappings

When adding new mods or updating to a new Minecraft version, the `curseforge_names.json` file may need new entries mapping internal mod names to their CurseForge display names.

### The Update Loop

Run this loop to populate missing mod name mappings:

1. **Run the update command** in the mod server directory:
   ```bash
   cd ~/OneDrive/Minecraft/"1.21 Mod Server" && make update-mod-names
   ```

2. **When it fails** with an error like:
   ```
   OSError: Could not find curseforge name for mod 'some mod name'.
   ```

3. **Search for the mod** on CurseForge using a web search:
   ```
   "some mod name" curseforge minecraft 1.21 NeoForge mod
   ```

4. **Add the mapping** to `curseforge_names.json`:
   ```json
   "some mod name": "Exact CurseForge Display Name"
   ```

5. **Repeat** until the command completes successfully.

### Common Issues

- Some mods have different names on CurseForge vs their internal mod ID (e.g., `"alexscaves"` -> `"Alex's Caves"`).
- Addon mods often have prefixes like `"Aether Addon: "` in their CurseForge names.
