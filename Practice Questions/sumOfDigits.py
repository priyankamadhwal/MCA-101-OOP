def sumOfDigits(num):

    digsum = 0

    num = abs(num)

    while num > 0:

        digsum += num % 10
        num = num // 10

    return digsum
