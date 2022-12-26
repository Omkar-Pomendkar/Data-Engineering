class Person:
    country = "India"
    city = "Mumbai"

    def takeBreadth(self):
        print("I am breathing")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreadth(self):
        print("I am Employee so I am breathing.. ")

class Programmer(Employee):
    company = "fiverr"

    def getSalary(self):
        print("No Salary to Programmer")
    def takeBreadth(self):
        print("I am Programmer so I am breathing.. ")

p = Person()
p.takeBreadth()
e = Employee()
e.takeBreadth()
pr = Programmer()
pr.takeBreadth()