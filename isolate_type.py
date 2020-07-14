import pySWC
import os

    #|    Current Labels
    #|    0 = Undefined
    #|    1 = soma
    #|    2 = Myelinated_Axon
    #|    3 = Basal_Dendrite
    #|    4 = Apical_Dendrite
    #|    5 = Custom
    #|    6 = Unspecified_Neurites
    #|    7 = Glia_Processes
    #|    8 = Blank
    #|    9 = Blank
    #|    10 = Axon_Hillock
    #|    11 = Unmyelinated_Axon
    #|    12 = Dendritic_Hub
    #|    13 = Proximal_Dendrite
    #|    14 = Distal_Dendrite
    #|    15 = Axon_Initial_Segment
    #|    16 = Axon_Heminode
    #|    17 = Axon_Node
    #|    18 = Dendritic_Swelling

#Enter node types to be isolated
isolated_labels = [1, 3, 4, 12, 13, 14, 18] 

#Enter targeted swc file
input_file = 'C:/Users/Owner/Desktop/pySWC-isolate_dendrite/test_files/VCN_c30_Full.swc'


def isolate_type(input_file, isolated_labels):
    """
    Returns a new swc file that is a copy of the input file with the selected 
    node isolated and the rest deleted
    """
    
    filename, file_extension = os.path.splitext(input_file)
    
    swc = pySWC.Swc(input_file)
    
    node_number = 0
    node_label = 1
    node_parent = 6

    isolated_nodes = []
    
    
    #Find all nodes to keep in the output file
    for node in range(0, swc.num_nodes):
        if swc.data[node, node_label] in isolated_labels:
            isolated_nodes.append(swc.data[node, :])
    
    old_id = []
    new_id = []
    
    #Create two lists, one with the old IDs of the reminaing nodes and one
    #with the new IDs, this will be used to reference changes in node ID
    for i, node in enumerate(isolated_nodes):
        old_id.append(node[0])
        new_id.append(i+1)
    
    #If the node's parent had its ID changed then change the node parent number
    #If the node's parent was deleted then make it origin (-1)
    for i, node in enumerate(isolated_nodes):
        node[node_number] = i+1
        if node[node_parent] == -1:
            node[node_parent] == -1
        elif node[node_parent] in old_id:
            node[node_parent] = new_id[old_id.index(node[node_parent])]
        else:
            node[node_parent] = -1
    
    new_file = filename + '_Isolated.swc'
    f = open(new_file, "w")
    
    new_swc = pySWC.Swc(new_file)
    new_swc.data = isolated_nodes
    
    new_swc.save_file(new_file)
    f.close()

    
isolate_type(input_file, isolated_labels)
