def sumListElements(L):
    '''
    Objective: To find the sum of all the elements of a given list.
    Input:
        L: A list of integers.
    Output:
        The sum of all the elements of the list.
    '''
    # Approach: sumListElements(L) = L[0] + sumListElements(L[1:])
    if L == []:
        return 0; 
    else:
        return L[0] + sumListElements(L[1:])
