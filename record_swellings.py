# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:43:34 2020

Goal is to identify all swellings within a dendrite and record/graph their
characteristics. Goals: 1- find the ratio of the largest node to the proximal
and distal for each swelling 2- record total number of swellings 
"""

import pySWC
import sys
import csv

def main(input_swc):
    
    swc = pySWC.Swc(input_swc)
    parent = swc.node_parent
    label, radius = swc.node_label, swc.node_radius
    num_nodes = swc.num_nodes
    swelling_label = 18
    
    #set full of nodes that have been visited (includes entire swelling)
    checked_nodes = set()
    with open('current.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        for node in range(0, num_nodes):
            
            swelling = []
            if swc.data[node, label] == swelling_label:
                break_var = False
            else:
                break_var = True
            
            #collect all nodes in a swelling into a list
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
            
            #find largest node in swelling, proximal and distal nodes
            if swelling:
                
                largest_radius = 0.0
                for swelling_node in swelling:
                    if swc.data[swelling_node, radius] > largest_radius:
                        largest_radius = swc.data[swelling_node, radius]
                        largest_index = swelling_node
                        
                swelling_children = swc.find_children(swelling[-1])
                distal_radius = 0.0
                if len(swelling_children) == 0:
                    distal_node = -1
                    
                elif len(swelling_children) > 1:
                    for kido in swelling_children:
                        if swc.data[kido, radius] > distal_radius:
                            distal_node = kido
                            distal_radius = swc.data[kido, radius]
                else:
                    distal_node = swelling_children[0]
                    distal_radius = swc.data[distal_node, radius]
                
                parent_node = int(swc.data[swelling[0], parent] - 1)
                proximal_radius = swc.data[parent_node, radius]
                
                if distal_radius == 0:
                    largest_to_distal = -999
                else:
                    largest_to_distal = largest_radius / distal_radius
                largest_to_proximal = largest_radius / proximal_radius
                
                x_coord = swc.data[largest_index, 2]
                y_coord = swc.data[largest_index, 3]
                z_coord = swc.data[largest_index, 4]

                writer.writerow([x_coord, y_coord, z_coord, largest_to_proximal, largest_to_distal])

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('Usage: python record_swelings.py [swc file path]')
