from LinkedBinaryTree import *


def is_height_balanced(bin_tree):
    def node_helper(node):
        if node == None:
            return True, 0
        else:
            left = node_helper(node.left)
            right = node_helper(node.right)
            height = 1 + max(left[1], right[1])

        if (left[0] and right[0]) and \
                abs(left[1] - right[1] <= 1):
            return True, height

        else:
            return False, height

    return node_helper(bin_tree.root)[0]

# def is_height_balanced(bin_tree):
#     def node_helper(node):
#         if node.left is None and node.right is None:
#             return True
#
#         left = node_helper(node.left)
#         right = node_helper(node.right)
#
#         if node.left is not None and node.right is not None:
#             is_balanced = (left is True and right is True) and (
#                     abs(node.left.height - node.right.height) <= 1)
#         else:
#             return True
#         return is_balanced
#
#     if bin_tree.root is None:
#         raise Exception("Empty Tree")
#
#     return node_helper(bin_tree.root)
