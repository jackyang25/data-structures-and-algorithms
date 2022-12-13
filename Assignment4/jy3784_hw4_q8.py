def flat_list(nested_lst, low, high):

    if isinstance(nested_lst[low], int):

        data = [nested_lst[low]]
    else:

        data = (flat_list(nested_lst[low], 0, len(nested_lst[low])-1))
    if (high >= low + 1) == True:

        temp = (flat_list(nested_lst, low + 1, high))

        return data + temp
    return data

