def shift(lst, k, shift_val = "left"):
    if shift_val == "left":
        for i in range(k):
            temp = lst[0]
            for j in range(len(lst)):
                if j+1 == len(lst):
                    lst[j] = temp
                else:
                    lst[j] = lst[j+1]
    if shift_val == "right":
        for i in range(k):
            temp = lst[-1]
            for j in range(len(lst)-1,-1,-1):
                if j == 0:
                    lst[j] = temp
                else:
                    lst[j] = lst[j-1]