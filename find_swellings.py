import pySWC
import sys
import os


def main(input_swc):

    in_file = pySWC.Swc(input_swc)
    radius = in_file.node_radius
    label = in_file.node_label
    swelling_label = 18

    for node in range(0, in_file.num_nodes):
        if in_file.data[node, label] == 14:
            old_branch = []
            branch = find_branch(in_file, node, 0, old_branch)
            smallest_1 = 999
            smallest_index_1 = 0
            smallest_2 = 999
            smallest_index_2 = 0
            largest = 0
            largest_index = 3

            if branch is not None:
                for current_node in branch:

                    """
                    We are grabbing swellings!! It seems to grab too many nodes around the swelling and It overwrites hubs.
                    """
                    #code.interact(local=locals())

                    if in_file.data[current_node, radius] > largest:
                        largest = in_file.data[current_node, radius]
                        largest_index = current_node

                    if in_file.data[current_node, radius] < smallest_1 and current_node <= largest_index:
                        smallest_1 = in_file.data[current_node, radius]
                        smallest_index_1 = current_node

                    if in_file.data[current_node, radius] < smallest_2 and current_node > largest_index:
                        smallest_2 = in_file.data[current_node, radius]
                        smallest_index_2 = current_node

            print(str(smallest_1) + " " + str(largest) + " " + str(smallest_2))
            if smallest_index_1 < largest_index < smallest_index_2:
                if largest / smallest_1 > 1.5:
                    if largest / smallest_2 > 1.5:
                        for swelling_node in range(smallest_index_1+1, smallest_index_2):
                            in_file.data[swelling_node, label] = swelling_label

            if smallest_index_2 < largest_index < smallest_index_1:
                if largest / smallest_1 > 1.5:
                    if largest / smallest_2 > 1.5:
                        for swelling_node in range(smallest_index_2+1, smallest_index_1):
                            in_file.data[swelling_node, label] = swelling_label

    name, ext = os.path.splitext(input_swc)
    in_file.save_file(name + "_edited.swc")


def find_branch(swc, node, count, branch):
    number, parent, label = swc.node_number, swc.node_parent, swc.node_label
    replaced_label = 14

    if count == 0:
        branch = [node]

    if count <= 6:
        for other_node in range(0, swc.num_nodes):

            if swc.data[other_node, parent] == swc.data[node, number]:
                if swc.data[other_node, label] == replaced_label:
                    branch.append(other_node)
                    count += 1
                    find_branch(swc, other_node, count, branch)

                return(branch)


if __name__ == "__main__":

    main(sys.argv[1])
