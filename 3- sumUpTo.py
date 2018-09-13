def sumUpTo(n):
    '''
    Objective: To find the sum of all the numbers from 1 to n.
    Input:
        n: A non-negative integer.
    Output:
        The sum of all numbers from 1 to n.
    '''
    # Approach: sumUpTo(n) = n + sumUpTo(n-1)
    if n == 0:
        return 0
    else:
        return n + sumUpTo(n-1)
