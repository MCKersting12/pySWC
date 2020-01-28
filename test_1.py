# -*- coding: utf-8 -*-
"""
Scale and find surface area
"""
import pySwc

test_cell = pySwc.Swc('test_file.swc')

print(test_cell.surface_area)

test_cell.scale(0.5)

print(test_cell.surface_area)

test_cell.adjust_surface_area(5000, error_rate = 0.00001)

print(test_cell.surface_area)