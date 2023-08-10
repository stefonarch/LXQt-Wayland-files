# LXQt Panel on Wayland Compositors

> Configuring tips and hacks for using `lxqt-panel` on wayland.

`lxqt-panel` starts if no "Desktop switcher" plugin is present in its configuration file. Recommended is using an alternative config file with `lxqt-panel -c /path/to/alternative/panel.conf`. Only position usable is "top" and/or "left". Positioning settings, taskbar and a few other plugins do not work. For a working configuration with a replacement for kbindicator-plugin see [panel.conf](lxqt-wayland/panel.conf).

* Window rules are needed until qt6.5 is fully implemented. See example config files in `lxqt-wayland` folder.
* Smaller width than 100% can lead to issues
* Usable in sway, hyrpland, kwin_wayland, wayfire and generally in all compositors with window rules
* custom command plugin can show/use commands from `hyprctl` and `swaymsg`, like display workspace name/switch.
* Reserved space (exclusive zone) can be reserved by `panelspace.py` if necessary (hyprland); a full version is `lxqt-panel-loader.py` which reads its width from `panel.conf`, reserves the space needed on top and starts the panel.


## Replacements for widgets

### Taskbar
waybar (wlr/waybar),yatbfw (icons only), wf-dock

### Desktop cycler/switcher
 Configure shortcuts for `go to left|right` and/or `go to <number>`, examples `C-A-left|right`;`C-A-1|2|3`
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

For numlock the value in `/sys/class/leds/input3::numlock/brightness` can be used in a customcommand plugin, similar for capslock. **Note**: The number (3) can be a different one on your system.

```
if [ "$(cat /sys/class/leds/input3\:\:numlock/brightness)" == "1" ]; then echo 'N';else echo ' ';fi
```
If you are using only 2 keyboard layouts and don't need a scrollock indicator a layout indicator can be added in the same way to the panel. in compositor configuration set the xkb_options :to `grp:alt_shift_toggle,grp_led:scroll` and in the custom command plugin:
```
if [ "$(cat /sys/class/leds/input3\:\:scrolllock/brightness)" == "1" ]; then echo ' DE';else echo ' US'; fi
```

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

### Show Desktop

On wayfire in `wayfire.ini`  configure a shortcut, add it as `wtype -M alt -P d` in a "custom command" widget, icon=desktop.
```
[wm-actions]
...
toggle_showdesktop = <alt> KEY_D
...
```

On labwc you can use `wlrctl toplevel minimize state:inactive` but it will minimize all applications and stop.
