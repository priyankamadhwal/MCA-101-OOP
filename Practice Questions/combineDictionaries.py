def combineDictionaries(d1,d2,d3={},i1=0):
    
    if i1 >= len(d1) and len(d2) <= 0:
        return d3

    if i1 < len(d1):
        
        find = list(d1.keys())[i1]

        if find in d2:
            lst = []
            lst.append(d1[find])
            lst.append(d2[find])
            del d2[find]
            new = {find:lst}
            d3.update(new)

        else:
            new = {find:d1[find]}
            d3.update(new)

        return combineDictionaries(d1,d2,d3,i1+1)

    else: 
        d3.update(d2)
        return d3
