# Wayland Implementations for the LXQt Desktop

## Wayland Compositors

Needed files for a basic LXQt wayland session - beside the wayland compositor itself - are:

* `/usr/bin/startlxqt<compositor>`
* `/usr/share/wayland-session/<compositor>-lxqt.desktop`
* `swaybg` for background image
* `swayidle` idle settings
* `yatbfw` taskbar, clock, quicklaunch
* `waybar` tray, cpu/ram/temp monitor, can do much more
* `wlogout` leave option
* `wmctrl` for some keybindings



The first can be executed also directly on tty. In wayland-ready display managers like SDDM you should see the new session type.
Please note that this here is experimental and work in progress, meant for testing purposes.

### Main overall issues in wayland:
* window activation on clicks from other windows
* placement of submenus
* no support for keyboard variants like `*.pt_Br or de_CH`


### Wayfire (stacking)

![Screenshot](lxqt-wayfire.png)

[Source](https://github.com/WayfireWM/wayfire/wiki/Configuration), [docs](https://github.com/WayfireWM/)

Scripts and example configurations in `wayfire` folder.  Don't forget to chmod +x `startlxqtwayfire`.
Configuration file: `~/.config/lxqt/lxqt-wayfire/wayfire.ini`

The most usable atm for a traditional LXQt experience, notifications, lxqt-runner, pcmanfm-qt, multiple desktops, notifications all working; nice animations (remember compiz?)

 Editing config file(s) is mandatory for customizing.


### Labwc (stacking)

![Screenshot labwc](labwc.png)


[Source](https://github.com/labwc/labwc#readme), [Docs](https://labwc.github.io/index.html)


Scripts and example configurations in `labwc` folder.  Don't forget to chmod +x `startlxqtlabwc`.
Configuration path: `~/.config/labwc/`

* environment: keyboard layout
* rc.xml: old friend
* autostart: well...
* menu.xml: click on desktop menu, close session, reload configuration.
* openbox themes in `~/.local/share/themes`

A minimal editor for rc.xml is [labwc-tweaks](https://github.com/labwc/labwc-tweaks).

![labwc-tweaks](tweaks.png)

#### Things working

* Launchers:
  * `lxqt-runner` (Alt+Space)
  * PCmanFM-qt's application view as full menu in panel
  *  bemenu-run on top screen (Alt+F3)
* Desktop (titlebar has to be removed manually)
* Palettes, theming (affects atm only runner), other LXQt settings
* Notifications (only at center)
* Policykit
* Alt+Tab
* Panel/bar (yatbfw):
  * close on middle click, toggle maximize on click
  * Clock and calendar popup,
  * basic "Show Desktop"
  * Launchers
  * Battery (works also in tray)
  * Network (works also in tray)
  * Volume, Brightness
* Tray/Notification area (swaybar, only show if at least one app uses it)

#### Things missing or half working

* Window focus change on clicks from other apps (links)
* Desktop effects
* Multiple desktops (in next version 0.6)
* Window rules (no title bar for runner and desktop for example)
* autostart has some issues not starting all
* applications like Featherpad and Gimp running under xwayland are not starting when clicking associated files in PCmanFm-qt
* yatbwf and waybar not hiding in fullscreen
* window activations from notifications
* some general icons in taskbar (telegram, keepassxc)
* no keybord layout switching without restart

#### Application replacements:

* grim (screenshot)
* wf-recorder (screencasting)


### Hyprland (tiling)

![Screenshot Hyprland](hyprland.png)

[Source](https://github.com/hyprwm/Hyprland#readme), [Wiki](https://wiki.hyprland.org/Configuring/Basic-Config/)

Config file: `~/.config/lxqt/lxqt-hyprland/hyprland.conf`

Scripts and example configuration in `hyprland` folder. Don't forget to `chmod +x`  `/usr/bin/startlxqthyprland`.

#### Pro

Nice window effects like dim inactive, fading and other animations, opacity, desktop change gesture (3 finger swipe).

#### Contro

Needs many window rules, some windows (like "save, discard, close" when closing unsaved texts) need manual resizing (mod + right mouse button + drag) to see all. lxqt-runner cannot resize it's window. Tray menus open below windows, windows on the right open submenu on the left and will lose focus.


### Sway (tiling)

See [LXQt Sway](https://github.com/selairi/lxqt-sway).
## Panels

### Yatbfw

[Source](https://github.com/selairi/yatbfw)

See `yatbfw.json`, located in `~/.config/	`

#### Features

* taskbar/dock (close on middleclick, toggle maximize on click)
* launchers
* brightness and speakers
* clock

Note: for `startlxqthyprland` change  position to "top".

### Waybar

See `waybar` folder; used here _only_ for systray/notification area and cpu/ram/temp/disk/keyboard-state and idle-inhibitor, see screenshot wayfire.

For `keyboard-state` working make sure your user is member of the "input" group.

Some icons need "font-icon" and "font-awesome" to be displayed.




