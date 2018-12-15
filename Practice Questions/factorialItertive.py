def factorial(n):
    assert n > 0
    fact = 1
    for i in range(1 , n+1):
        fact*=i
    return fact

def main():
    n = int(input('Enter the value of n : '))
    print(factorial(n))

if __name__ == '__main__':
    main()
