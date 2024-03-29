# Wayland Implementations for the LXQt Desktop

> Files and dotfiles for a LXQt Wayland session. LXQt hasn't implemented yet wayland protocols (waiting for the release of `layer-shell-qt6`) but many components are full or partially working on wayland natively. Work in progress.

### Content

* `/usr/bin/startlxqt<compositor>` : ENV variables, import settings, start compositor
* `/usr/share/wayland-session/<compositor>_lxqt.desktop` : Entry in SDDM
* `scripts` and `autostart`: some tools  for autostart and else
* `lxqt-wayland`: settings for compositors


## Starting LXQt Session

Copy the `lxqt-wayland` folder to `~/.config/`. It contains the default settings for the compositors and an extra part for LXQt. The `startlxqt*` scripts will use the configuration in this location; copy the desired file(s) from `wayland-sessions` to `/usr/share/wayland-sessions/` (if using a display manager like SDDM to choose sessions). Copy the desired scripts from `startup_scripts` to `/usr/bin/` or `/usr/local/bin` and make them executable.

`startlxqt<compositor>` scripts can be executed also directly in tty; environment variables are set here before starting the compositor.


### Working LXQt components:

`lxqt-config`, `lxqt-notificationd`, `lxqt-runner`, `lxqt-config`, `lxqt-policykit-agent`, `lxqt-powermanagement`, `PCmanFm-qt`,`LXimage-qt`, `lxqt-archiver`, `QTerminal`,`Qps` `lxqt-about` - all running natively. Using the [wip branch](https://github.com/stefonarch/lxqt-notificationd/tree/wip_layer_shell_qt) for `lxqt-notificationd` is recommended for full working.

### Using lxqt-session in general

With LXQt 1.2.0  and later `lxqt-session` can be started in the autostart section of any compositors configuration files. For `kwin_wayland` the `startlxqtkwin` script will start the session. Recommended is the **latest LXQt version** or git checkout.

#### Notes

* Module`lxqt-globalshortcuts`  loads but fails to register shortcuts
* Some applications in autostart may not work under wayland and/or can cause high cpu usage - see "autostart" and "scripts" folder for a selective autostart of applications depending on session type x11/wayland.
* Lock settings are not applied in wayland.

### lxqt-panel

Recommended is using an alternative config file with `lxqt-panel -c /path/to/alternative/panel.conf`. Positioning settings, taskbar and a few other plugins do not work. For a working configuration with a replacement for kbindicator-plugin see  `lxqt-wayland/panel.conf`.

* Window rules are needed until both Qt 6.6 and layershell-qt are implemented.
* Smaller width than 100% can lead to issues
* Usable in sway, hyrpland, kwin_wayland and wayfire
* custom command plugin can show/use commands from `hyprctl` and `swaymsg`, like display workspace name/switch.

For more details see [lxqt-panel](lxqt-panel.md) page.

####  3rd party tools

* `swaybg` : background image (below desktop)
* `swayidle; swaylock` :  lock screen
* Panels/bars:
* `sfwbar` : [Source](https://github.com/LBCrion/sfwbar) taskbar and much more
* `yatbfw` [Source](https://github.com/selairi/yatbfw): taskbar, clock, quicklaunch
* `waybar` : taskbar, notification area, cpu/ram/temp monitor, keyboard layout display
* `wf-dock` (wayfire) dock/taskbar
For `keyboard-state` working make sure your user is member of the "input" group. Some icons need "font-icon" and "font-awesome" to be displayed.
* `lxqt-wlogout` : Close session, see [lxqt-wlogout](https://github.com/stefonarch/lxqt-wlogout)
* `wlrctr` and `wtype` : for some keybindings  - especially open applications menu in `lxqt-panel`
* `wdisplay`: Screen management GUI, see [wdisplay](https://github.com/artizirk/wdisplays)
* `clipman`, `dmenu`, `wl-clipboard` : cliboard manager (configuration see `wayfire.ini`)
* `grim`,`slurp` : screenshots [Example configuration](https://github.com/stefonarch/LXQt-Wayland-files/blob/3a7f36c8945eee874a5111ea3a425edbc7da9034/wayfire/wayfire.ini#L240)
* `wofi` alternative launcher
* `wshot` Qt GUI for screenshots, see [wshot](https://github.com/stefonarch/wshot)
* `wev` : xev for wayland
* wayfire plugin for [per application keyboard layout switch](https://github.com/AlexJakeGreen/wayfire-kbdd-plugin)
* `gammastep` replacement for redshift
* `wvkbd` virtual keyboard

## Labwc (stacking)

![Screenshot labwc](labwc.png)


[Source](https://github.com/labwc/labwc#readme), [Docs](https://labwc.github.io/index.html)

[LXQt-labwc-session](https://github.com/stefonarch/lxqt-labwc-session)

Old friend openbox in modern wayland clothes. Version 0.6.4 and later and latest LXQt offer a usable LXQt Session as there are implemented window rules. Desktop works perfectly. See [lxqt-wayland/labwc/rc.xml](https://github.com/stefonarch/LXQt-Wayland-files/blob/0ddf63261f4946ccf7b15837341fe611b7b357d7/lxqt-wayland/labwc/rc.xml#L59) for details.

* openbox themes in `~/.local/share/themes`

A minimal editor for rc.xml is [labwc-tweaks](https://github.com/labwc/labwc-tweaks).

![labwc-tweaks](tweaks.png) .


#### Pros

* Lightweight and snappy (no animations)
* xdg-activation protocol support (allow applications to activate
  themselves (e.g. raise to the top and get keyboard focus) if they
  provide a valid `xdg_activation token`.)
* Snapping, (custom) regions and tiling by shortcuts
* Config files and syntax following openbox standard
* Stable git master

#### Issues

* Notification window steals focus, settings not working (fixed in the [wip branch](https://github.com/stefonarch/lxqt-notificationd/tree/wip_layer_shell_qt) of `lxqt-notificationd`)
* `lxqt-runner` does not close on loosing focus (fixed in Git)


#### Useful tools

* Swipe to change workspace `~/.config/libinput-gestures.conf` (for shortcuts "C-A-left|right")
```
gesture: swipe left 3	wtype  -M ctrl -M alt -P right
gesture: swipe right 3 wtype  -M ctrl -M alt -P left
```
Add `libinput-gestures-setup start ` in autostart.

* Screensaver:

In `autostart`:

`swayidle before-sleep swaylock timeout 300 'feh -rzsZFD 8  --draw-exif --draw-tinted ~/path/to/folder' resume 'killall feh'`


## Wayfire (stacking)

![Screenshot LXQt wayfire](lxqt-wayfire.png)

[Source](https://github.com/WayfireWM/wayfire/wiki/Configuration), [docs](https://github.com/WayfireWM/)
Notifications, lxqt-runner, pcmanfm-qt (Desktop) and lxqt-panel (top or left, some plugins not working) did work perfectly with a previous version of [lxqt-desktop-shell](https://gitlab.com/wayfireplugins/lxqt-desktop-shell.git) plugin, changed settings are read and applied. In addition many resource-friendly desktop effects and animations. Using git version `0.8.*`  is mandatory for the plugin and `wayfire-plugins-extra` is recommended.

**Note** : because of API changes the plugin is broken actually on master, so compiling `git checkout 4faddbdb4d971a43546e1a9f2350d4fc51882850` is needed. **No other version is running** due to the plugin broken.


#### Issues
* Panel does not release focus (wayfire issue)
* Some window rules for app placing do not work (wayfire issue)
* Using CDS (client side decoration) Qt windows with the default Qt decoration will shrink at every reload, therefor using SSD is recommended.


#### Useful tools

* `wf-info` : get window information for creating window rules (wayfire only)
* `wcm` Wayfire configuration editor GUI (GTK). **Not** recommended if you also edit manually `wayfire.ini` (removes comments).
* `wf-kill` : kill windows

## Sway (tiling)

![Screenshot LXQt Sway](sway.png)

Configured with panels and lxqt-runner (alt+space),2 keyboard layouts (toggle: alt+shift) and some window rules.
Quite usable. See also [LXQt Sway](https://github.com/selairi/lxqt-sway).


#### Useful tools

* Mouse gestures (swipe to switch desktop): `~/.config//libinput-gestures.conf`
```
gesture: swipe left 3   swaymsg -t command workspace next_on_output
gesture: swipe right 3  swaymsg -t command workspace prev_on_output
```

* Dim inactive windows: see `autostart/sway_scripts.desktop` and `scripts`



### Hyprland (tiling)

![Screenshot Hyprland](hyprland.png)

[Source](https://github.com/hyprwm/Hyprlasettingsnd#readme), [Wiki](https://wiki.hyprland.org/Configuring/Basic-Config/)

Nice window effects like dim inactive, fading and other animations, opacity, desktop swipe gesture (3 finger swipe). Usable LXQt components are `lxqt-panel`,`-powermanagement`,`-policykit`, `-runner`, `-config`, `-notificationd` and with a workaround `lxqt-session` (see below).

#### Useful tools

* [different keyboard layout per application ](https://github.com/MahouShoujoMivutilde/hyprland-per-window-layout)
* `hyprshot` Screenshots
* `hyprpicker` (colorpicker)
*
#### Issues

* `lxqt-session` doesn't load session modules because Hyprland overwrites `XDG_CURRENT_DESKTOP=LXQt` with `XDG_CURRENT_DESKTOP=Hyprland`. Modules can be inserted manually with some delay in `hyprland.conf` or the `.desktop` files of the modules can be copied from `/etc/xdg/autostart/` to `~/.local/share/applications/` and then `OnlyShowIn=LXQt;` has to be removed.

## Kwin_wayland (stacking)

![Screenshot kwin_wayland](kwin_wayland.png)

The most similar to a LXQt x11 session, specially if already used with kwin. Needs some window rules for top/left panel, runner, notifications (import `kwin_wayland.rule` in KDE settings → Windowmanagement → Window rules). Not really usable until `lxqt-panel` implements  a wayland taskmanager, `cairo-wayland-dock-git` and `latte-dock-git` can be used instead.

#### Pros

* Working desktop on all outputs, always at bottom (needs `pcmanfm-qt` git version with title for it's desktop window.
* Lock screen
* Multiple sessions/switch user (to test)
* Spectacle screenshots (GUI)
* klipper for clipboard
* `lxqt-config-monitor`  working (to test multihead)
* no manual config files editing

#### Issues

* Big issue: No taskbar (waybar; yatbfw; swfbar) possible due to lack of support for foreign-toplevel-protocol.
Docks mentioned above can work.
* Same [issues to configure](https://github.com/lxqt/lxqt/wiki/ConfigWindowManagers#kwin) shortcuts when no full plasma-desktop is installed
* fullscreen window titlebar goes under the panel
* wlsunset and gammastep not working, `kcmshell5 kcm_nightcolor&` works.
* keys for brightness and volume are not working (sliders from panel work), manually shortcut assigning should work



### Yatbfw


See `lxqt-wayland/yatbfw.json`.

#### Features

* taskbar/dock (close on middle click, toggle maximize on click, minimize on right click)
* launchers
* brightness and speakers
* clock


### Waybar

See `waybar` folder and config; used for systray/notification area, cpu/ram/temp/disk/keyboard-state.

For `keyboard-state` working make sure your user is member of the "input" group.

Some icons need "font-icon" and "font-awesome" to be displayed.



## Main overall issues in compositors:

* Window activation on clicks from other windows or notifications
* Applications activated by shortcuts are not handled by `lxqt-session --logout` and therefor not gracefully closed. Workaround: using `*.desktop` files.

Example for labwc:

```  
    <keybind key="W-k">
      <action name="Execute" command="pcmanfm-qt '/usr/share/applications/org.keepassxc.KeePassXC.desktop'" />
    </keybind>
```


## Tipps & Tricks

### Screensaver with slideshow

Using `feh`, a window rule for "always-on-top" and under "autostart" settings:

`swayidle before-sleep swaylock timeout 300 'feh -rzsZFD 8  --draw-exif --draw-tinted ~/path/to/folder' resume 'killall feh'`

### Autostart scripts and .desktop files

If `lxqt-session` is used also with x11 session some scripts that will select the application to launch depending of `XDG_SESSION_TYPE` or `$wayland_compositor` can be useful. Examples in `autostart` folder.

### Telegram does not open multimedia files

If images and video do not open: unset "animation"" and eventually "opengl" in `Preferences > Advanced`.



