import math
def computeValue(d,n, prev=0,pwr=0):
    if n == 0:
        return 0

    curr = d*math.pow(10,pwr)+prev
    return curr+computeValue(d,n-1,curr,pwr+1)
    
