# -*- coding: utf-8 -*-
"""
Scale and find surface area
"""
import pySWC

in_file = pySWC.Swc('test_file.swc')

in_file.scale(0.1)
in_file.rotate(180, 0, 0)

in_file.adjust_surface_area(4000)
print(in_file.surface_area)
in_file.save_file("test_scaled.swc")