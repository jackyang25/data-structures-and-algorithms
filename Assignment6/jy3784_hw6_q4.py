from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    shallow_copy = DoublyLinkedList()
    for elem in lnk_lst:
        shallow_copy.add_last(elem)
    return shallow_copy


def deep_copy_linked_list(lnk_lst):
    deep_copy = DoublyLinkedList()
    for elem in lnk_lst:
        if isinstance(elem, int):
            deep_copy.add_last(elem)
        elif isinstance(elem, object):
            deep_copy.add_last(deep_copy_linked_list(elem))
    return deep_copy

