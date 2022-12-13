
from BinarySearchTreeMap import *

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()

    if len(prefix_lst) == 0:
        return bst
    #bst.insert(prefix_lst[0])
    stack = []
    root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))
    stack.append(root)

    for i in range(1, len(prefix_lst)):
        item=None

        while len(stack) >0 and prefix_lst[i] > stack[-1].item.key:
            item = stack.pop()

        if item is not None:
            item.right = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[i]))
            stack.append(item.right)

        else:
            item = stack[-1]
            item.left = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[i]))
            stack.append(item.left)
    bst.root=root
    bst.size=len(prefix_lst)
    return bst



















