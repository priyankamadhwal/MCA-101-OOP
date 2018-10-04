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
