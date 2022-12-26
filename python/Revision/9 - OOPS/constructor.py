class Employe:
    company = "Google"


    def __init__(self ,name,salary):
        self.name = name
        self.salary = salary
        print("Employee is created")


    def getDetails(self):
        print(f"the Name of the Employee is {self.name}")
        print(f"the Name of the Employee is {self.salary}")

    def getSalary (self):
        print(f"Salary of this emplyee working in {self.company} is {self.salary}")
    @staticmethod
    def great():
        print("Good Morning everybody")

    @staticmethod
    def time():
        print("The Time is 14:34 pm")

omkar = Employe("omkar",1000)
omkar.getDetails()
print(omkar.salary)