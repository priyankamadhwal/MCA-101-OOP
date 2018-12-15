def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def main():
    n = int(input('Enter n : '))
    print(str(n)+'! = ',factorial(n))

if __name__ == '__main__':
    main()
