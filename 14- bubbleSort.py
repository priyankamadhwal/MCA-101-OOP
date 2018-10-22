def swap(lst, lowerIndex=0, pos=0):
    '''
    OBJECTIVE : To swap the elements of list so that the largest element goes at the lower index.
    INPUT     :
          lst        : A list of numbers.
          lowerIndex : The lower index upto which swapping is to be performed.
    OUTPUT    : List, with the correct element at lowerIndex.
    '''
    #APPROACH : Compare the 2 list elements: If lst[up] is greater than lst[low], then swap them.
    length = len(lst)
    up=length-1-pos
    low=up-1
    if low < lowerIndex:
        return
    if lst[up] > lst[low]:
        temp = lst[up]
        lst[up] = lst[low]
        lst[low] = temp
    swap(lst, lowerIndex, pos+1)

def bubbleSort(lst, lowerIndex=0):
    '''
    OBJECTIVE : To sort the given list using bubble sort.
    INPUT     :
        lst        : A list of numbers.
        lowerIndex : The lower index from which sorting should begin.
    OUTPUT    : List, sorted in descending order.
    '''
    #APPROACH : Make use of the swap() function.
    length = len(lst)
    if lowerIndex > length-2:
        return
    swap(lst, lowerIndex)
    bubbleSort(lst, lowerIndex+1)
