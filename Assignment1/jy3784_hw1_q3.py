n = 5

#a
def func1(n):
    if n > 0:
        x = 0
        for i in range(n):
            x += i**2
        return x

#b
sum1 = sum([i**2 for i in range(n)])

#c
def func2(n):
    if n > 0:
        x = 0
        for i in range(n):
            if i % 2 == 1:
                x += i**2
        return x

#d
sum2 = sum([i**2 for i in range(n) if i % 2 == 1])




