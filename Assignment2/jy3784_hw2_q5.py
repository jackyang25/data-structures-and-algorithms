def split_parity(lst):

    length = len(lst)
# 1 for loop - O(n)
    for i in range(0, length):
        if i != length - 1:

            if lst[i] % 2 == 0:

                x = lst[i+ 1]

                lst[i + 1] = lst[i]

                lst[i] = x