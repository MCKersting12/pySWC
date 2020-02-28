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
    label, radius = swc.node_label, swc.node_radius
    num_nodes = swc.num_nodes
    swelling_label = 18
    
    #set full of nodes that have been visited (includes entire swelling)
    checked_nodes = set()
    
    for node in range(0, num_nodes):
        
        swelling = []
        if swc.data[node, label] == swelling_label:
            break_var = False
        else:
            break_var = True
        
        while node not in checked_nodes and break_var == False:
            
            swelling.append(node)
            children = swc.find_children(node)
            checked_nodes.add(node)
            if children:
                child = -1
                if len(children) > 1:
                    for kido in children:
                        if swc.data[kido, label] == swelling_label:
                            child = kido    
                else:
                    child = children[0]
                
                if swc.data[child, label] == swelling_label:
                    node = child
                
                else:
                    break_var = True
            
            else:
                break_var = True
        
        if swelling:
            print(swelling)
        
        largest = 0.0
        for swelling_node in swelling:
            if swc.data[swelling_node, radius] > largest:
                largest = swc.data[swelling_node, radius]
        #print(largest)
                
            

if __name__ == "__main__":
    
    #if len(sys.argv) > 1:
    main('VCN_c09_Full.swc')
    #else:
    #    print('Usage: python record_swelings.py [swc file path]')
