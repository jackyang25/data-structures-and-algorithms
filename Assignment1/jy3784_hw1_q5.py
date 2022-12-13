def fibs(n):
    fib = []
    for i in range(n):
        if i == 1 or i == 0:
            fib.append(1)
            yield 1
        else:
            fib.append(fib[i-1] + fib[i-2])
            yield fib[i]
