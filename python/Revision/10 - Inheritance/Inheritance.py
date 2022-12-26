# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname (self):
        print(self.firstname,self.lastname)


p = Person("Omkar","Pomendkar")
p.printname()

class Student(Person):
    pass

s = Student("Sanjay","Pomendkar")
s.printname()