def succ(n):
    
    '''
    OBJECTIVE: To find the successor of a number.
    INPUT:
        n:  A non-negative integer.
    OUTPUT:
        Return the successor of the number n.
    '''
    #APPROACH: succ(n) = n+1
    
    if n < 0:
        print('Error: The given number, ',n, ', is less than 0.')
        return
    
    return n+1
