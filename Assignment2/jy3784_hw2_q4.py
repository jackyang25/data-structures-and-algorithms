def e_approx(n):
    e = 1
    fact = 1

    for i in range(1, n+1):
        fact = fact * i
        e = e + (1 / fact)

    return str(e)
