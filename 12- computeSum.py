def succ(n):
    '''
    OBJECTIVE: To find the successor of a number.
    INPUT:
        n:  A non-negative integer.
    OUTPUT:
        Return the successor of the number n.
    '''
    #APPROACH: succ(n) = n+1
    
    return n+1

def pred(n, m=0):
    '''
    OBJECTIVE: To find the predecessor of a number.
    INPUT:
        n:  A non-negative integer.
        m:  A candidate for predecessor of n.
    OUTPUT:
        Return the predecessor of the number n.
    '''
    #APPROACH: Use function succ(n) and comparison operators only.
    #          If succ(m) is equal to n, then pred(n)=m.
    
    if succ(m) == n:
        return m

    else:
        return pred(n, succ(m))

def computeSum(m, n):
    '''
    OBJECTIVE: To find the sum of two numbers.
    INPUT:
        m:  Any non-negative integer.
        n:  Any non-negative integer.
    OUTPUT:
        Return the sum of numbers m and n.
    '''
    #APPROACH: Use functions succ, pred and comparison operations to compute the sum.
    
    if m == 0:
        return n
    
    if n == 0:
        return m
    
    if m >= n:
        return computeSum(succ(m), pred(n))
    return computeSum(pred(m), succ(n))
