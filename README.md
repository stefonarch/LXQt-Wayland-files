# Wayland Implementations for the LXQt Desktop

## Wayland Compositors

Needed files for a basic LXQt wayland session - beside the wayland compositor itself - are:

* `/usr/bin/startlxqt<compositor>`
* `/usr/share/wayland-session/<session>.desktop`
* `swaybg` for background image

The first can be executed also on tty. In wayland-ready display managers like SDDM you should see the new session type.
Please note that this here is experimental and work in progress, meant for testing purposes.


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

#### Things missing or half working

* Desktop effects
* Multiple desktops (in next version 0.6)
* Window rules (no title bar for runner and desktop for example)
* autostart has some issues not starting all
* Featherpad not starting when clicking text files in PCmanFm-qt
* yatbwf and waybar not hiding in fullscreen

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

Needs many window rules, some windows (like "save, discard, close" when closing unsaved texts) need manual resizing (mod + right mouse button + drag) to see all. lxqt-runner cannot resize it's window.


### Sway (tiling)

See [LXQt Sway](https://github.com/selairi/lxqt-sway).
## Panels

### Yatbfw

[Source](https://github.com/selairi/yatbfw)

See `yatbfw.json`, located in `~/.config/	`

Note: for `startlxqthyprland` change  position to "top".

### Waybar

See `waybar` folder; used here _only_ for systray/notification area on labwc.




