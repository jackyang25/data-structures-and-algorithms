def two_sum(srt_lst, target):
    right = len(srt_lst) - 1
    left = 0


    while (srt_lst[left] + srt_lst[right]) != target:
        #check conditions
        if (srt_lst[left] + srt_lst[right]) < target:
            left = left + 1


        else:
            right = right - 1

        if left is right:

            return None
        #tuple
    return left,right



