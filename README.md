# minecraft-server-tools

A bunch of utilities for easily working with and managing minecraft servers, specifically aimed at managing minecraft forge servers with large numbers of manually-installed mods.

## Installing mods with this package

If I directed you here to install Minecraft mods, you'll need to follow the following steps:

1. Install [OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/download) and accept my invitation to access 'Minecraft Mods'.
2. Install [Python 3.9+](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads), and [Java 17](https://www.oracle.com/java/technologies/downloads/#jdk17-windows).
3. Install [Minecraft](https://www.minecraft.net/en-us/download), launch it at least once, then make sure Minecraft is closed.
4. Open a command prompt, `cd` to wherever you want to clone the repository, and run `git clone https://github.com/evhub/minecraft-server-tools.git`.
5. Open the `minecraft-server-tools` folder you just created and run `make-launcher.bat` on Windows or `make-launcher.sh` otherwise (you may need to run `chmod +x ./make-launcher.sh` first).
6. You should now have an `Evan's Modded Minecraft.bat` or `Evan's Modded Minecraft.sh` file on your Desktop. Whenever you want to launch modded Minecraft, just run that file (on non-Windows you may need to run `chmod +x "~/Desktop/Evan's Modded Minecraft.sh"` first).

_Alternatively, if you use the `install-client.bat`/`install-client.sh` scripts instead, those will just install the mods without creating a new launcher script, but you'll have to rerun the installation script every time I update the mods._
