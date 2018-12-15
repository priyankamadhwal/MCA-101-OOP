def fib_rec(n):

    if n <= 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib(n):
    res = []
    count = 1
    while count <= n :
        t = fib_rec(count)
        res.append(t)
        count += 1

    return res
