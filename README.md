# Wayland Implementations for the LXQt Desktop

> Files and dotfiles for a LXQt Wayland session

* `/usr/bin/startlxqt<compositor>` : ENV variables, import settings, start compositor
* `/usr/share/wayland-session/<compositor>-lxqt.desktop` : Entry in SDDM
* `swaybg` : background image
* `swayidle` : idle settings
* `yatbfw` : taskbar, clock, quicklaunch
* `waybar` : notification area, cpu/ram/temp monitor, keyboard layout display
* `lxqt-wlogout` : Close session, see [lxqt-wlogout](https://github.com/stefonarch/lxqt-wlogout)
* `wmctrl` : for some keybindings
* `wdisplay`: Screen management GUI, see [wdisplay](https://github.com/artizirk/wdisplays)


## Starting LXQt Session

Copy the `lxqt-wayland` folder to `~/.config/`. The `startlxqt*` scripts will use the configuration in this location; copy the desired file(s) from `desktop_files` to `/usr/share/wayland-sessions/` if using a display manager like SDDM to choose session type. Copy the desired scripts from `startup_scripts` to `/usr/bin/` and make them executable.

`startlxqt<compositor>` scripts can be executed also directly in tty; environment variables are set here before starting the compositor.

Please note that this here is experimental work in progress.

### Working LXQt components:

`lxqt-config`, `lxqt-notificationd`, `lxqt-runner`, `lxqt-config`, `lxqt-policykit-agent`, `lxqt-powermanagement`, `PCmanFm-qt`,`LXimage-qt`, `lxqt-archiver`, `QTerminal`,`Qps` `lxqt-about` - all running natively. For `lxqt-panel` see [#lxqt-panel](https://github.com/stefonarch/LXQt-Wayland-files#lxqt-panel).

### Using lxqt-session

From LXQt 1.2.0 on `lxqt-session` can be started in the autostart section of the compositors configuration file.

* Systray/Notification area (using waybar or lxqt-panel) should start first (= `sleep 2 && lxqt-session`) (fixed in git)
* Module`lxqt-globalshortcuts`  loads but  fails to register shortcuts
* Some applications in autostart may not work under wayland and/or can cause high cpu usage - see "autostart" folder for a selective autostart of applications depending on session type.
* Lock settings are not applied in wayland.

## Kwin_wayland (stacking)

![Screenshot kwin_wayland](kwin_wayland.png)

The most similar to a LXQt x11 session, specially if already used with kwin. Needs some window rules for top/left panel, runner, notifications (see `kwin_wayland.rule`). Needs more testing.

#### Highlights

* Working desktop on all outputs, always at bottom (this needs `pcmanfm-qt` compiled with title for it's desktop window. Note: a better method needed as the rule will apply to all window with that title)
* Lock screen
* Multiple sessions/switch user (to test)
* Spectacle screenshots working
* klipper for clipboard
* `lxqt-config-monitor`  working (to test multihead)

#### Issues

* Taskbar only provided by swaybar, yatbfw segfaults
* Same [issues to configure](https://github.com/lxqt/lxqt/wiki/ConfigWindowManagers#kwin) shortcuts when no full plasma-desktop is installed
* QTerminal crashes when try to split (only on kwin_wayland)
* More easier to experience full session crash
* fullscreen window titlebar goes under the panel
* Element (xwayland) segfaults


## Wayfire (stacking)

![Screenshot LXQt wayfire](lxqt-wayfire.png)

[Source](https://github.com/WayfireWM/wayfire/wiki/Configuration), [docs](https://github.com/WayfireWM/)

Usable stacking compositor for a traditional LXQt experience: notifications, lxqt-runner, pcmanfm-qt,
multiple desktops and lxqt-panel with some limits and quirks do work. In addition many resource-friendly desktop effects and animations.

#### Issues

* `lxqt-notificationd` steals focus
* `PCmanFm-qt --desktop` can be used, windows can go under it, sticky needs a window rule.
* With yatbfw and lxqt-panel in fullscreen both are visible (middle click on the icon to close lxqt-panel)

## Sway (tiling)

![Screenshot LXQt Sway](sway.png)

Configured with panels and lxqt-runner (alt+space),2 keyboard layouts (toggle: alt+shift) and some window rules.
Quite usable. See also [LXQt Sway](https://github.com/selairi/lxqt-sway).

* Mouse gestures (swipe to switch desktop): `~/.config//libinput-gestures.conf`
```
gesture: swipe left 3   swaymsg -t command workspace next_on_output
gesture: swipe right 3  swaymsg -t command workspace prev_on_output
```
See `autostart/sway_scripts.desktop`.


#### Issues

* Panel volume popup opens at 0,0 (fixed in git)

## Labwc (stacking)

![Screenshot labwc](labwc.png)


[Source](https://github.com/labwc/labwc#readme), [Docs](https://labwc.github.io/index.html)

Old openbox in wayland mode. Usable LXQt components are `lxqt-session`,`-powermanagement`,`-policykit`, `-runner`, `-config` and `pcmanfm-qt`.

* openbox themes in `~/.local/share/themes`

A minimal editor for rc.xml is [labwc-tweaks](https://github.com/labwc/labwc-tweaks).

![labwc-tweaks](tweaks.png).

#### Issues

* No window rules with version 0.6, lxqt-panel not usable (manual placement)
* `lxqt-notificationd` window steals focus and has title bar
* `lxqt-runner` and others have title bar

### Hyprland (tiling)

![Screenshot Hyprland](hyprland.png)

[Source](https://github.com/hyprwm/Hyprlasettingsnd#readme), [Wiki](https://wiki.hyprland.org/Configuring/Basic-Config/)

Nice window effects like dim inactive, fading and other animations, opacity, desktop swipe gesture (3 finger swipe). Usable LXQt components are `lxqt-panel`,`-powermanagement`,`-policykit`, `-runner`, `-config`, `-notificationd` and with a workaround `lxqt-session` (see below).

#### Issues

* `lxqt-session` doesn't load session modules because Hyprland overwrites `XDG_CURRENT_DESKTOP=LXQt` with `XDG_CURRENT_DESKTOP=Hyprland`. Modules can be inserted manually with some delay in `hyprland.conf` or the `.desktop` files of the modules can be copied from `/etc/xdg/autostart/` to `~/.local/share/applications/` and then `OnlyShowIn=LXQt;` has to be removed.

## Panels

### lxqt-panel

`lxqt-panel` can be started if no "Desktop switcher" is present in its configuration file. Positioning, taskbar and some few other plugins do not work automatically For a working configuration with replacement for kbindicator see  `lxqt-wayland/panel.conf`, add a window rule for placing at top, other positions are not usable atm. Usable only in sway and wayfire.

### Yatbfw

[Source](https://github.com/selairi/yatbfw)

See `lxqt-wayland/yatbfw.json`.

#### Features

* taskbar/dock (close on middleclick, toggle maximize on click, minimize on right click)
* launchers
* brightness and speakers
* clock


### Waybar

See `waybar` folder; used here _only_ for systray/notification area, cpu/ram/temp/disk/keyboard-state - see screenshot hyprland.

For `keyboard-state` working make sure your user is member of the "input" group.

Some icons need "font-icon" and "font-awesome" to be displayed.

#### Accessories

* `clipman`, `dmenu`, `wl-clipboard` : cliboard manager (configuration see `wayfire.ini`)
* `grim`,`slurp` : screenshots [Example configuration](https://github.com/stefonarch/LXQt-Wayland-files/blob/3a7f36c8945eee874a5111ea3a425edbc7da9034/wayfire/wayfire.ini#L240)
* `wf-info` : get window information for creating window rules (wayfire only)
* `wofi` alternative launcher
* `wcm` Wayfire configuration editor GUI (GTK). **Not** recommended if you also edit manually `wayfire.ini`.
* `wf-dock` dock/taskbar
* `wev` : xev for wayland
* wayfire plugin for [per application keyboard layout switch](https://github.com/AlexJakeGreen/wayfire-kbdd-plugin)


## Main overall issues in compositors:

* Window activation on clicks from other windows or notifications.
Fixed for browser in [Tipps & Tricks](https://github.com/stefonarch/LXQt-Wayland-files#tipps--tricks).

## Tipps & Tricks

### Activate browser window on links clicked

Example for Firefox, similar approach should work for all browser:

Executable `/usr/bin/firefox_wayland`:
 ```
#!/bin/sh
wlrctl toplevel focus firefox
exec /usr/lib/firefox/firefox "$@"
```

Copy  `firefox.desktop` file from  `/usr/share/applications/` to  `~/.local/share/applications/` :

```
#Exec=/usr/lib/firefox/firefox %u
Exec=/usr/bin/firefox_wayland %u
```

### Autostart scripts and .desktop files

If `lxqt-session` is used scripts that select the application to launch depending of `XDG_SESSION_TYPE` or `$wayland_compositor` can be useful. Examples in `autostart` folder.

### Telegram does not open multimedia files

If images and video do not open: unset "animation"" and eventually "opengl" in `Preferences > Advanced`.



