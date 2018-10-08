def insertInSortedList(lst, value, tryLoc):
    '''
    OBJECTIVE: To insert an element in a given sorted list at its correct position.
    INPUTS:
       lst     :  A list of numbers which is to be sorted.
       value   :  Value which is to be inserted in the given list.
       tryLoc  :  The candidate location to insert the value.
    OUTPUT:
            A sorted list.
    '''
    #APPROACH: Compare the value with previous elements and shift the elements until correct position is found.
    if tryLoc == 0:
        return
    if value < lst[tryLoc-1]:
       lst[tryLoc] = lst[tryLoc-1]
       lst[tryLoc-1] = value
       insertInSortedList(lst, value, tryLoc-1)
    else:
        return

def insertionSort(lst, index=0):
    '''
    OBJECTIVE: To sort the given list.
    INPUTS:
       lst    :   Any list of numbers.
       index  :   The index upto which the list is to be sorted. 
    '''
    #APPROACH: Make use of insertInSortedList() funcion.
    if index==len(lst):
        return
    tryLoc = index
    value = lst[index]
    insertInSortedList(lst, value, tryLoc)
    insertionSort(lst, index+1)
