def reverseString(string):

    reverse = ''

    for i in range(len(string)):
        reverse = string[i] + reverse

    return reverse
