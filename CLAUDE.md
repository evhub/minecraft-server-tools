# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minecraft Server Tools is a Python utility suite for managing Minecraft Forge/NeoForge servers with large mod collections. Key features include mod installation/synchronization, CurseForge API integration, launcher profile management, and JVM optimization.

## Directories

**Important:** There are three directories to be aware of:
- **This repository** (`minecraft-server-tools/`) - Edit source code here, run `make build` to compile
- **Server directory** (`constants.SERVER_DIR`) - Run operational commands like `make update-mods` and `make update-mod-names` here
- **Client directory** (`constants.MINECRAFT_DIR`) - Look for logs or crashes here when debugging client issues

## Build and Development Commands

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
# Update/download mods from CurseForge
make update-mods

# Update mod name mappings (dry-run mode)
make update-mod-names
```

## Language: Coconut

This project uses [Coconut](http://coconut-lang.org/), a functional programming superset of Python. Key points:

- Source files use `.coco` extension
- Compiles to Python 3 with `--strict` mode
- Uses Coconut-specific syntax: `then`/`else` ternaries, pattern matching, pipeline operators
- Always run `make build` after editing `.coco` files

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

### Configuration

Key constants in `constants.coco`:
- `MC_VERSION` / `FORGE_VERSION` - Current Minecraft and NeoForge versions
- `SERVER_DIR` - Server installation path (from env `MINECRAFT_SERVER_DIR` or default)
- `CLIENT_RAM` / `SERVER_RAM` - Memory allocation (auto-adjusted based on system RAM)
- `MODLOADER` - Currently "NeoForge"

### Entry Points

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
   make update-mod-names
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

## Debugging Minecraft Mod Crashes

When analyzing Minecraft crash logs to identify problematic mods:

1. **Always look at `latest.log`** - Crash reports are useful as a starting point, but the biggest source of information is always the full log.
2. **Search for "Suspected Mods"** - The crash reporter performs heuristic analysis and lists likely culprits, and the user may have a list of possible culprits as well. Always grep for each mod that might be a culprit.
3. **Search for `FATAL`** - This indicates a fatal error, often pointing to the root cause.

Don't get tunnel-visioned on one error - a mod initialization failure earlier in the log can cause cascading errors that appear unrelated (like config loading failures).

## Memory Profiling and Analysis

**All memory profiling and analysis files should go in `./heap_analysis/`.**

### Taking Heap Dumps

Use JDK tools to capture memory state from a running Minecraft instance:

```bash
# Find Minecraft process ID
jps -l
# Look for cpw.mods.bootstraplauncher.BootstrapLauncher

# Take a heap dump
jcmd <PID> GC.heap_dump minecraft_heap.hprof

# Get a class histogram (quick overview without full dump)
jmap -histo <PID> > heap_histo.log
```

### Analyzing with Eclipse MAT

Eclipse Memory Analyzer (MAT) is essential for deep analysis:

1. **Download MAT** from https://eclipse.dev/mat/downloads.php
2. **Increase MAT memory** in `MemoryAnalyzer.ini` - set `-Xmx32g` for large dumps
3. **Run from command line**:
   ```bash
   ./ParseHeapDump.bat "path/to/heap.hprof" org.eclipse.mat.api:suspects
   ```
4. **Review the Leak Suspects report** - generates HTML in a zip file

### Attributing Memory to Mods

Memory attribution is challenging because most memory is in shared Minecraft classes, not mod-specific classes. Key approaches:

#### 1. Direct Attribution (from histogram)
Parse the histogram to group by module/mod:
- Classes contain module info like `(modname@version)`
- Sum bytes per mod to get direct memory usage
- This captures memory in mod's own classes only

#### 2. Content-Based Attribution
Mods register content that ends up in Minecraft's classes:
- **Blocks** → stored in `BlockState`, `BakedQuad`, `WeightedBakedModel`
- **Items** → stored in `ItemStack`, `PatchedDataComponentMap`
- **Entities** → stored in entity classes and component maps
- Count content registrations per mod and estimate proportional memory

#### 3. Dominator Tree Analysis (MAT)
MAT's dominator tree shows what's retaining memory:
- Identifies accumulation points
- Shows path from GC roots
- Reveals which objects are holding references

### Key Memory Consumers in Modded Minecraft

| Category | Typical Classes | Notes |
|----------|-----------------|-------|
| Block Models | `BakedQuad`, `MultiPartBakedModel`, `SimpleBakedModel`, `WeightedBakedModel` | Scales with block count; variant mods multiply this |
| Block States | `BlockState` | Each block can have many states |
| World Data | `PoiRecord`, `BlockPos`, `ChunkSection` | Scales with loaded chunks |
| Items | `ItemStack`, `PatchedDataComponentMap` | Items in world/inventories |
| Collections | `HashMap`, `ArrayList`, `Object[]` | Generic storage, hard to attribute |
| Textures | `byte[]`, `NativeImage` | Texture data |

### Common Issues

1. **Transient "leaks"** - Large object counts during loading that GC cleans up
2. **POI accumulation** - 100M+ PoiRecord indicates excessive POI data or large explored area
3. **FTB Backups memory** - Keeps backup data in RAM during operation

### Digging Into Game Data Files

When heap analysis shows suspicious data (like excessive POIs), one angle of attack is to go to the actual game files to understand what's in them:

#### POI Data (Point of Interest)
Located in `saves/<world>/poi/` as `.mca` region files:
```python
# Parse MCA file to find POI types
import zlib, struct, re
from collections import Counter

with open('poi/r.0.0.mca', 'rb') as f:
    locations = f.read(4096)  # Location table
    for i in range(1024):
        offset = struct.unpack('>I', b'\x00' + locations[i*4:i*4+3])[0]
        if offset > 0:
            f.seek(offset * 4096)
            length = struct.unpack('>I', f.read(4))[0]
            compression = f.read(1)[0]
            data = zlib.decompress(f.read(length - 1))
            # Search for POI type strings
            poi_types = re.findall(r'minecraft:[a-z_]+', data.decode('latin-1'))
            print(Counter(poi_types).most_common(10))
```

Normal POI counts per chunk: single digits (beds, workstations, beehives)
Abnormal: thousands per chunk indicates a mod bug
