class Person:
    count = 0
    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address
        Person.count+=1

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob

    def getAddress(self):
        return self.address

    def getCount(self):
        return Person.count

    def __str__(self):
        return self.name+', '+self.dob+', '+self.address

    def __del__(self):
        print('Deleted')
        Person.count-=1

def main():
    p1 = Person('Amir','24-10-1990','38/4, IIT Delhi 110016')
    print(p1)
    print(Person.count)
    print(Person.getName(p1))
    del p1
    print(p1)
    
