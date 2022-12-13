
def list_min(lst, low, high):
    if low >= high:
        return lst[high]

    comparison = list_min(lst, low + 1, high)

    if comparison < lst[low]:
        return comparison

    else:
        return lst[low]


#     if low >= high:
#         return lst[high]
#
#     if lst[low] == lst[high]:
#         lst.pop(high)
#         return list_min(lst, low, high - 1)
#
#     elif lst[low] > lst[high]:
#         lst.pop(low)
#
#         return list_min(lst, low, high - 1)
#
#     elif lst[low] < lst[high]:
#
#         lst.pop(high)
#         return list_min(lst, low, high - 1)


