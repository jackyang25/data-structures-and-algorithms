
from BinarySearchTreeMap import *

def find_min_abs_difference(bst):
    sorted_array = []

    for node in bst:
        sorted_array.append(node)

    min_diff = sorted_array[-1]

    for i in range(len(sorted_array) - 1):
        if (sorted_array[i + 1] - sorted_array[i]) < min_diff:
            min_diff = sorted_array[i + 1] - sorted_array[i]

    return min_diff



# bst = BinarySearchTreeMap()
# bst.insert(9)
# bst.insert(7)
# bst.insert(4)
# bst.insert(1)
# bst.insert(6)
# bst.insert(20)
# bst.insert(17)
# bst.insert(25)
# print(find_min_abs_difference(bst))