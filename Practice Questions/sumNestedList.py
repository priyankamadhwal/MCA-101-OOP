def sumNestedList(lst,length):
    if length == 0:
        return 0
    t = 0
    if type(lst[length-1]) == list:
        t += sumNestedList(lst[length-1],len(lst[length-1]))
    else:
        t += lst[length-1]

    t += sumNestedList(lst,length-1)

    return t

a = [1,4,[5,3],[2,[3,[4]]]]
print(sumNestedList(a,len(a)))
        
