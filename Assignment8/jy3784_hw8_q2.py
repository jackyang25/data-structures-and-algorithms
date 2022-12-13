# passes through POSITIVE integer n
# function returns a binary search tree with n nodes
# containing the keys 1, 2, 3 , ..., n

from BinarySearchTreeMap import *

def create_chain_bst(n):
    tree = BinarySearchTreeMap()
    for elem in range(n):
        tree.insert(elem + 1)
    return tree

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    mid = (low + high) // 2
    bst.insert(mid)
    if low is not high:
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)


