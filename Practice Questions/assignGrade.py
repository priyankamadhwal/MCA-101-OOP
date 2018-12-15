def assignGrade(marks):
    
    assert marks >= 0 and marks <=100

    if marks >= 90:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    elif marks >= 40:
        grade = 'D'
    elif marks >= 30:
        grade = 'E'

    return grade

def main():

    marks = float(input('Enter marks : '))
    print('Grade :', assignGrade(marks))

if __name__ == '__main__':
    main()
