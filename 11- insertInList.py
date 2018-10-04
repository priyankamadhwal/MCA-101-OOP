def insertInSortedList(lst, val, tryLoc=0):
    '''
    OBJECTIVE: To insert an element in a sorted list.
    INPUTS:
         lst: A sorted list.
         val: Any number which is to be inserted in the list l.
         tryLoc: A try location in the lst where val can be inserted.  
    OUTPUT:
        The sorted list lst after inserting val at proper position.
    '''
    #APPROACH: Compare val with lst[tryLoc] and insert when correct position is found.
    if lst == []:
        lst.insert(0,val)
    elif lst[tryLoc:] == []:
        lst.append(val)
    elif val <= lst[tryLoc]:
        lst.insert(tryLoc,val)
    else:
        insertInSortedList(lst, val, tryLoc+1)

def insertInList(lst1, lst2, pos=0):
    '''
    OBJECTIVE: Given a sorted list of numbers, insert the numbers of another list into this list.
    INPUTS:
         lst1: A sorted list.
         lst2: Any list whose numbers are to be inerted in lst1.
         pos: The position of number in lst2 which is to be inserted.
    OUTPUT:
        The sorted list lst1 after inserting the elements of lst2.
        
    '''
    #APPROACH: use insertInSortedList() function.
    if lst2[pos:] == []:
        return
    else:
        insertInSortedList(lst1,lst2[pos])
        insertInList(lst1,lst2,pos+1)
