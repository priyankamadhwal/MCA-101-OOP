def succ(n):
    '''
    OBJECTIVE: To find the successor of a number.
    INPUT:
        n:  A non-negative integer.
    OUTPUT:
        Return the successor of the number n.
    '''
    #APPROACH: succ(n) = n+1
    
    assert n >= 0
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

    if n <= 0:
        print ("ERROR: The given number, ",n,", is a not a positive number.")
    
    elif succ(m) == n:
        return m

    else:
        return pred(n, succ(m))
