import pyswc
import os
import numpy as np


def isolate_type(swc, isolated_labels):
    """
    Returns a new swc file that is a copy of the input file with the selected
    node isolated and the rest deleted
    """
    if not isinstance(swc, pyswc.Swc):
        raise TypeError('Must be an instance of the Swc class')
    
    node_number = 0
    node_label = 1
    node_parent = 6

    isolated_nodes = []

    # Find all nodes to keep in the output file
    for node in range(0, swc.num_nodes):
        if swc.data[node, node_label] in isolated_labels:
            isolated_nodes.append(swc.data[node, :])

    if len(isolated_nodes) == 0:
        #print('There are no nodes of type ' + str(isolated_labels))
        return 0

    old_id = []
    new_id = []

    # Create two lists, one with the old IDs of the reminaing nodes and one
    # with the new IDs, this will be used to reference changes in node ID
    for i, node in enumerate(isolated_nodes):
        old_id.append(node[0])
        new_id.append(i+1)

    # If the node's parent had its ID changed then change the parent number
    # If the node's parent was deleted then make it origin (-1)
    for i, node in enumerate(isolated_nodes):
        node[node_number] = i+1
        if node[node_parent] == -1:
            node[node_parent] == -1
        elif node[node_parent] in old_id:
            node[node_parent] = new_id[old_id.index(node[node_parent])]
        else:
            node[node_parent] = -1

    new_file = 'temp.swc'
    f = open(new_file, "w")

    new_swc = pyswc.Swc(new_file)
    new_swc.data = np.asarray(isolated_nodes)
    new_swc.num_nodes = new_swc.data.shape[0]
    new_swc.surface_area = new_swc.find_surface_area()
    f.close()
    os.remove(new_file)
    
    return new_swc
