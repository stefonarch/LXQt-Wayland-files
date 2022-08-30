# Wayland Implementations for the LXQt Desktop

## Wayland Compositors

Needed files for an LXQt wayland session - beside the wayland compositor - are:

* `/usr/bin/startlxqt<compositor>`
* `/usr/share/wayland-session/<session>.desktop`
* `swaybg` for background image
* `wofi` for the menu

The first can be executed also on tty. In wayland-ready display managers like SDDM you should see the new session type.


### Hyprland (tiling)

[Source](https://github.com/hyprwm/Hyprland#readme), [Wiki](https://wiki.hyprland.org/Configuring/Basic-Config/)

Config file: `~/.config/lxqt/lxqt-hyprland/hyprland.conf`

Scripts and example configuration in `hyprland` folder. Don't forget to `chmod +x`  `/usr/bin/startlxqthyprland`.

#### Pro

Nice window effects like dim inactive, fading and other animations, opacity, desktop change gesture (3 finger swipe).

#### Contro

Needs many window rules, some windows (like "save, discard, close" when closing unsaved texts) need manual resizing (mod + right mouse button + drag) to see all. lxqt-runner cannot resize it's window.


### Sway (tiling)

See [LXQt Sway](https://github.com/selairi/lxqt-sway).

### Labwc (stacking)


[Source](https://github.com/labwc/labwc#readme), [Docs](https://labwc.github.io/index.html)


Scripts and example configurations in `labwc` folder.  Don't forget to chmod +x `startlxqtlabwc`.
Configation path: `~/.config/labwc/`

* environment: keyboard layout
* rc.xml: old friend
* autostart: well...
* menu.xml: click on desktop menu, close session, reload configuration.
* openbox menu themes


#### Pro

Familiar experience (openbox).

#### Contro

No window effects. Some conflicting shortcuts to fix (Alt + up).

## Panels

### Yatbfw

[Source](https://github.com/selairi/yatbfw)

See `yatbfw.json`, located in `~/.config/	`




