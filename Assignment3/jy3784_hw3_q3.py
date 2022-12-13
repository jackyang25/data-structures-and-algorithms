
def find_duplicates(lst):

    x = 0
    for elem in lst:
        if elem > x:
            x = elem

    temp = [0] * (x+1)

    dup = []

    for elem in lst:
        temp[elem] += 1

    for i in range(len(temp)):
        if temp[i] > 1:
            dup.append(i)

    print(temp)

    return dup