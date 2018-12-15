def vowelsCount(string):

    vowels = 'aeiouAEIOU'
    total = 0

    for ch in vowels:
        total += string.count(ch)

    return total
