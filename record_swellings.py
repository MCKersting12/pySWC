# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:43:34 2020

Goal is to identify all swellings within a dendrite and record/graph their
characteristics. Goals: 1- find the ratio of the largest node to the proximal
and distal for each swelling 2- record total number of swellings 
"""

import pySWC
import sys


def main(input_swc):
    
    swc = pySWC.Swc(input_swc)
    number, parent = swc.node_number, swc.node_parent
    label, radius = swc.node_number, swc.radius
    num_nodes = swc.num_nodes
    swelling_label = 18
    
    #set full of nodes that have been visited (includes entire swelling)
    checked_nodes = set()
    
    for node in range(0, num_nodes):
        
        swelling = [node]
        
        if node not in checked_nodes and swc.data[node, label] == swelling_label:
            child = swc.find_children(node)
            if swc.data[node, label] === swelling_label:
                swelling.append(child)
            
    
    

if __name__ == "__main__":

    main(sys.argv[1])
