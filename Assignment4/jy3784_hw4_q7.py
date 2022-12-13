def split_by_sign(lst, low, high):

    if (high <= low) == True:
        return lst

    elif (lst[high] < 1 and lst[low] > 0):

        (lst[high], lst[low]) = (lst[low], lst[high])

        return split_by_sign(lst, low + 1, high - 1)

    elif (lst[low] < 1):
        return split_by_sign(lst, low + 1, high)

    elif (lst[high] > 0):
        return split_by_sign(lst, low, high - 1)

    return lst
