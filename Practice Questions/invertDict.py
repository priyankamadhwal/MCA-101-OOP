def invertDict(d):
    meanings = list(set(d.values()))
    words=list(d.keys())
    newDict = {}
    for currm in meanings:
        new = []
        for currw in words:
            if (d[currw] == currm):
                new.append(currw)
        newDict.update({currm:new})
    return newDict

print(invertDict({1:'one', 2:'two', 3:'one'}))


