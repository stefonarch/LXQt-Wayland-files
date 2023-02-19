#!/usr/bin/env python3
# Add reserved space at top fo screen
panel_size = 40

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, GtkLayerShell

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
