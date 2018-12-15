def reverseString(string):
    if len(string) <= 0:
        return ''
    return string[len(string)-1] + reverseString(string[0:len(string)-1]) 
