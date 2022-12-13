
from LinkedBinaryTree import *

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        if root == None:
            return "End"

        else:
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)

            curr_min = root.data
            curr_max = root.data

            if left != "End":
                curr_min = min(curr_min, left[0])
                curr_max = max(curr_max, left[1])

            if right != "End":
                curr_min = min(curr_min, right[0])
                curr_max = max(curr_max, right[1])

            return curr_min, curr_max

    if bin_tree.root is None:
        raise Exception("Minimum and Maximum not defined")

    return subtree_min_and_max(bin_tree.root)