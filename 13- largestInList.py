def max(num1, num2):
    '''
    OBJECTIVE: To find the the maximum of two numbers.
    INPUTS:
        num1:   First number.
        num2:   Second number.
    OUTPUT:
        Returns maximum of num1 and num2.
    '''
    #APPROACH: Compare the numbers and return maximum.
    if num1 >= num2:
        return num1
    return num2

def largestInList(l):
    '''
    OBJECTIVE: To find the the largest number in given list.
    INPUTS:
         l:   A list of numbers.
    OUTPUT:
        Returns largest element of list l.
    '''
    #APPROACH: Use max() function to find largest element.
    if l == []:
        print("Invalid list!")
    elif len(l) == 1:
        return l[0]
    else:
        return max(l[0],largestInList(l[1:]))
