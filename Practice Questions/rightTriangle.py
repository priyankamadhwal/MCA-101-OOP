def rightTriangle(n):

    for i in range(1, n+1):
        print('*' * i)
def main():

    n = int(input('Enter the value of n : '))
    rightTriangle(n)

if __name__ == '__main__':
    main()
        
