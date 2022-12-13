
def remove_all(lst, value):
    times = 0

    for i in range(len(lst)):

        if lst[i] != value:
            times += 1
            lst.append(lst[i])

        if lst[i] == value:
            times += 1

    lst.reverse()

    for i in range(times):
        lst.pop()

    lst.reverse()

    return lst


