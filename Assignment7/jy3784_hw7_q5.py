
from LinkedBinaryTree import *


def create_expression_tree(prefix_exp_str):
    def create_expression_tree_helper(prefix_exp_lst, start_pos):
        key = prefix_exp_lst[start_pos]
        symbols = ["+","-","*","/"]

        if key not in symbols:
            node = LinkedBinaryTree.Node(int(key))
            return node, start_pos + 1

        left = create_expression_tree_helper(prefix_exp_lst, start_pos + 1)

        right = create_expression_tree_helper(prefix_exp_lst, left[1])
        node = LinkedBinaryTree.Node(key, left[0], right[0])

        return node, right[1]

    prefix_list = prefix_exp_str.split()

    return LinkedBinaryTree(create_expression_tree_helper(prefix_list, 0)[0])


def prefix_to_postfix(prefix_exp_str):
    postfix_tree = create_expression_tree(prefix_exp_str)
    postfix_string = " ".join(str(elem.data) for elem in postfix_tree.postorder())
    return postfix_string

