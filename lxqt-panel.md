# LXQt Panel on Wayland Compositors

>Hacks and workarounds for `lxqt-panel` on wayland.

The lxqt-panel v.2.0 doesn't include yet a taskbar plugin for wayland.
It's recommended to compile the work-in progress [lxqt-panel-wlroots-taskbar](https://github.com/LXQt-Marcus-Fork/lxqt-panel/tree/wlroots-taskbar). For Arch the PKGBUILD in [AUR](../AUR)can be used. At the moment copying `lxqt-panel.desktop` to `/etc/xdg/autostart` is needed as it's missing in the building.

## Replacements for widgets

### Desktop cycler/switcher
Completely working with kwin_wayland.
Under sway or Hyprland 'swaymsg` or `hyprctl dispatch` commands can be used.

 Workaround: Configure shortcuts for `go to left|right` and/or `go to <number>`, examples `C-A-left|right`;`C-A-1|2|3`
  and make sure to have `wtype` installed.
  
![screenshot desktop switcher](desktopcycler.png)
  

 * First method, cycling:
    * Create `desktop_left.desktop`  in `~/.local/share/applications/`
    * Add a "quicklaunch" widget to the panel and drag this file into it, and again the same for  "right" values.
```
[Desktop Entry]
Name=Desktop left
GenericName=Switch to left workspace
Comment=
Exec=wtype -M ctrl -M alt -P left
Type=Application
Icon=/usr/share/lxqt/themes/Arch-Colors/arrow-left.svg
Terminal=false
```
  
  
 * Second method, workspace cycling:
      * Add 2 or more "custom command" widgets to the panel and configure them like that:
      * echo → (or > or some text)
      * left click or mouse wheel command `wtype  -M ctrl -M alt -P right`
      * no repeat
  
 * Second method, workspace switcher:
     * command: `echo workspacename` or `echo 1`
     * left click: `wtype  -M ctrl -M alt -P 1`
  


### Keyboard state/layout indicator

For numlock the value in `/sys/class/leds/input3::numlock/brightness` can be used in a customcommand plugin, similar for capslock. **Note**: The number (3) can be a different one on your system. This needs

```
XKB_DEFAULT_LAYOUT=us,de
XKB_DEFAULT_OPTIONS=grp:alt_shift_toggle,grp_led:scroll
```
in `labwc/environment` or other compositors config files.

```
if [ "$(cat /sys/class/leds/input3\:\:numlock/brightness)" == "1" ]; then echo 'N';else echo ' ';fi
```
If you are using only 2 keyboard layouts and don't need a scrollock indicator a layout indicator can be added in the same way to the panel. in compositor configuration set the xkb_options :to `grp:alt_shift_toggle,grp_led:scroll` and in the custom command plugin:
```
if [ "$(cat /sys/class/leds/input3\:\:scrolllock/brightness)" == "1" ]; then echo ' DE';else echo ' US'; fi
```

For more than 2 layouts see [togglelayout](https://github.com/stefonarch/LXQt-Wayland-files/blob/main/scripts/togglelayout) (labwc only but could be adapted to others).


###  Colorpicker

Install [hyprpicker](https://github.com/hyprwm/hyprpicker) and create a `colorpicker.desktop` file in  `~/.local/share/applications:

```
[Desktop Entry]
Name=colorpicker
GenericName=Pick color from screen
Comment=
Exec=bash -c "hyprpicker -a && notify-send -a colorpicker -i colorpicker -t 3000 'Color value copied to clipboard'"
Type=Application
Categories=Graphics;Utility;
Icon=colorpicker
Terminal=false
```

Call it from runner/mainmenu or add it to a "quicklaunch" widget on the panel.

### Show Desktop Button

Full working with kwin_wayland

On wayfire in `wayfire.ini`  configure a shortcut, add it as `wtype -M alt -P d` in a "custom command" widget, icon=desktop.
```
[wm-actions]
...
toggle_showdesktop = <alt> KEY_D
...
```

On labwc you can use `wlrctl toplevel minimize state:inactive && wlrctl toplevel minimize state:active` as command in the custom command widget but this will just minimize all applications but not toggle it.
