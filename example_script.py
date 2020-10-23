# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:51:00 2020

@author: Owner
"""

import pyswc

swc = pyswc.Swc('C:/Users/Owner/Desktop/pySWC-isolate_dendrite/test_files/VCN_c02_Full.swc')

swc.rotate(0, 90, 0)

new_swc = pyswc.isolate_type(swc, [0,])

new_swc.save_file('rotated_2swc')
