#!/usr/bin/env python3
#Adds space on the left
panel_size = 40

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, GtkLayerShell

if __name__ == '__main__':
	win = Gtk.Window()
	win.set_size_request(panel_size, -1)
	GtkLayerShell.init_for_window(win)
	GtkLayerShell.auto_exclusive_zone_enable(win)
	GtkLayerShell.set_anchor(win, GtkLayerShell.Edge.LEFT, True)
	GtkLayerShell.set_anchor(win, GtkLayerShell.Edge.TOP, True)
	GtkLayerShell.set_anchor(win, GtkLayerShell.Edge.BOTTOM, True)
	GtkLayerShell.set_layer(win, GtkLayerShell.Layer.BOTTOM)
	win.show()
	Gtk.main()
