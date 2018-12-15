def fib(n):

    if n == 0:
        return []

    elif n == 1:
        return [1]

    elif n == 2:
        return [1,1]

    else:
        t1 = 1
        t2 = 1
        count = 3
        res = [1,1]
        while count <= n :
            t3 = t1 + t2
            res.append(t3)
            t1 = t2
            t2 = t3
            count += 1
        return res
