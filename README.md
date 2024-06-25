# minecraft-server-tools

A bunch of utilities for easily working with and managing minecraft servers, specifically aimed at managing minecraft Forge servers with large numbers of manually-installed mods.

## Installing mods with this package

If I directed you here to install Minecraft mods, you'll need to follow the following steps:

1. Install [OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/download) and accept my invitation to access "Minecraft Mods".
2. Install the latest [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads).
3. Install the Minecraft Legacy Launcher ([Windows Download](https://aka.ms/minecraftClientWindows); [Mac Download](https://aka.ms/minecraftClientMac)).
4. In the Minecraft launcher, run "Minecraft: Java Edition" at least once on the latest version, then make sure Minecraft is closed.
5. Open a command prompt, `cd` to wherever you want to clone the repository, and run `git clone https://github.com/evhub/minecraft-server-tools.git`.
   1. Alternatively, if you'd prefer, you can use [GitHub Desktop](https://desktop.github.com/) to clone this repository instead.
6. Open the `minecraft-server-tools` folder you just created and run `install.bat` on Windows or `install.sh` otherwise (on non-Windows you may need to run `chmod +x ./install.sh` first).
7. You should now have an `Evan's Modded Minecraft.bat` or `Evan's Modded Minecraft.sh` file on your Desktop. Whenever you want to launch modded Minecraft, just run that file.
8. Once you're in the Minecraft launcher, just select the "Evan's Modded Minecraft" profile (to the left of the "Play" button) and press "Play"!

## Additional performance optimizations

_The guide below is Windows-only._

If you want to maximize your Minecraft performance, there are some additional steps you can perform:

1. Ensure you always use discrete graphics for Graal `javaw`.
   1. Type "Graphics settings" in the Start bar and open it up.
   2. Under "Custom options for apps" and "Add an app", ensure "Desktop app" is selected, then press "Browse".
   3. In the browser, navigate to and select `<wherever you cloned this repository>/graal/graalvm-jdk-<some numbers>/bin/javaw.exe`. **Make sure you select `javaw.exe` and not `java.exe`.**
   4. "Java(TM) Platform SE binary" should be added to the list on the Graphics settings page. Select it and press "Options".
   5. Select "High performance" and press "Save".
2. Adjust your video settings in-game. Consult me and I will help you with this.
<!-- 3. **(DON'T DO THIS; THIS ONE SUCKS)** Ensure Graal `javaw` has the privilege to lock pages in memory.
   1. Type "cmd" into the Start bar, right-click on "Command Prompt", and select "Run as administrator".
   2. Run the following two commands in sequence:
      1. `FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")`
      2. `FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")`
   3. Restart your computer.
   4. Press Windows+R and enter "gpedit.msc".
   5. Navigate to "Local Computer Policy" > "Computer Configuration" > "Windows Settings" > "Security Settings" > "Local Policies" > "User Rights Assignment".
   6. Double-click on "Lock pages in memory" and select "Add User or Group".
   7. Under "Enter the object names to select" enter both "Administrator" and the email address associated with your Microsoft account. Press "Check Names" and make sure that works.
   8. Press "OK" and "OK".
   9. Restart your computer.
   10. Open file explorer and navigate to `<wherever you cloned this repository>/graal/graalvm-jdk-<some numbers>/bin/`. Make sure you do not accidentally open `graalvm-jdk-<some numbers>.zip`.
   11. Right-click on `javaw.exe` (make sure it is `javaw.exe` and not `java.exe`) and select "Properties".
   12. Select "Compatibility", check "Run this program as an administrator", and press "OK".
   13. Whenever you want to launch Minecraft, instead of launching normally, right-click and select "Run as administrator". -->
