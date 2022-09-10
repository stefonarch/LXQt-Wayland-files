# Wayland Implementations for the LXQt Desktop

Needed files and components for a LXQt wayland session - beside the wayland compositor itself - are:

* `/usr/bin/startlxqt<compositor>` : ENV variables
* `/usr/share/wayland-session/<compositor>-lxqt.desktop` : Entry in SDDM
* `swaybg` : background image
* `swayidle` : idle settings
* `yatbfw` : taskbar, clock, quicklaunch
* `waybar` : tray, cpu/ram/temp monitor, can do much more
* `wlogout` : leave options
* `wmctrl` for some keybindings

#### Optional

* `clipman`, `dmenu` : cliboard manager
* `grim`,`slurp` : screenshots
* `wf-info` : get window information for creating window rules (wayfire only)
* `wofi` alternative launcher
* `wcm` Wayfire configuration editor GUI (GTK). Not recommended if you also edit manually `wayfire.ini`.


`startlxqt<compositor>` can be executed also directly in tty. In wayland-ready display managers like SDDM you should see the new session type. Please note that this here is experimental and work in progress, meant for testing purposes.

### Working LXQt components:

`lxqt-notificationd`, `lxqt-runner`, `lxqt-config`, `lxqt-polkit-agent`, `lxqt-powermanagement`, `PCmanFm-qt`,`LXimage-qt`, `lxqt-archiver`, `QTerminal`,`Qps` `lxqt-about` - all running natively.


#### Main overall issues in those compositors:

* window activation on clicks from other windows or notifications.
Fixed in [Tipps & Tricks](https://github.com/stefonarch/LXQt-Wayland-files#tipps--tricks) )
* placement of submenus
* no support for keyboard variants like `pt_Br or de_CH`


## Wayfire (stacking)

![Screenshot](lxqt-wayfire.png)

[Source](https://github.com/WayfireWM/wayfire/wiki/Configuration), [docs](https://github.com/WayfireWM/)

Scripts and example configurations in `wayfire` folder.  Don't forget to chmod +x `startlxqtwayfire`.
Configuration file: `~/.config/lxqt/lxqt-wayfire/wayfire.ini`

The most usable atm for a traditional LXQt experience: notifications, lxqt-runner, pcmanfm-qt, multiple desktops, notifications all working; many resource-friendly desktop effects and animations.

Editing config file(s) is mandatory for customizing.

## Labwc (stacking)

![Screenshot labwc](labwc.png)


[Source](https://github.com/labwc/labwc#readme), [Docs](https://labwc.github.io/index.html)


Scripts and example configurations in `labwc` folder.  Don't forget to chmod +x `startlxqtlabwc`.
Configuration path: `~/.config/labwc/`

* environment: keyboard layouhttps://github.com/stefonarch/LXQt-Wayland-files#things-workingt
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
* yatbwf and waybar not hiding in fullscreen
* no keybord layout switching without restart

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


## Tipps & Tricks

### Activate browser window on links clicked

Example for Firefox, similar approach should work for all browser:

Executable `/usr/bin/firefox_wayland`:
 ```
#!/bin/sh
wlrctl toplevel focus firefox
exec /usr/lib/firefox/firefox "$@"
```

Local `firefox.desktop` file in `~/.local/share/applications/` :

```
#Exec=/usr/lib/firefox/firefox %u
Exec=/usr/bin/firefox_wayland %u
```




