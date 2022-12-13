import math

def factors(num):

    x = int(math.sqrt(num) + 1)

    # search algo
    for i in range(1, x):

        if num % i is 0:
            
            yield i

    for i in range(x - 1, 0, -1):

        if (num % i is 0):

            yield (num // i)




