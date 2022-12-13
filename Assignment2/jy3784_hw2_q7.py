
def findChange(lst01):

    #set variables
    upp = len(lst01) - 1

    low = 0

    mid = (low + upp) // 2

    while upp > low:

        #condition statements
        if lst01[mid] is 1 and lst01[mid - 1] is 0:

            return mid

        elif lst01[mid] == 1:

            upp = mid -1

        else:

            low = mid + 1

        mid = (upp + low) // 2

    return mid

