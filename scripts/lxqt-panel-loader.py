#!/usr/bin/env python3
import os
import subprocess
import gi
gi.require_version("Gtk", "3.0")
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, GtkLayerShell
import time

panel_size = 40  # set a default value in case the line isn't found
config_dir = os.getenv('XDG_CONFIG_HOME', os.path.expanduser('~/.config'))
config_path = os.path.join(config_dir, 'lxqt/panel.conf')

with open(config_path, 'r') as file:
    for line in file:
        if 'panelSize=' in line:
            panel_size = int(line.split('=')[1])
            break

if panel_size is not None:
    # do something with panel_size, such as printing it
	print(f'The panel size is {panel_size}. Starting...')
	subprocess.Popen(["/usr/bin/lxqt-panel"])
	time.sleep(2) # Sleep for 2 seconds → not show white space

else:
	# handle the case where the line wasn't found
	print('Error: could not find panel size in config file.')



if __name__ == '__main__':
	win = Gtk.Window()
	win.set_size_request(-1, panel_size)
	GtkLayerShell.init_for_window(win)
	GtkLayerShell.auto_exclusive_zone_enable(win)
	GtkLayerShell.set_anchor(win, GtkLayerShell.Edge.LEFT, True)
	GtkLayerShell.set_anchor(win, GtkLayerShell.Edge.RIGHT, True)
	GtkLayerShell.set_anchor(win, GtkLayerShell.Edge.TOP, True)
	GtkLayerShell.set_layer(win, GtkLayerShell.Layer.BOTTOM)
	win.show()

	Gtk.main()
