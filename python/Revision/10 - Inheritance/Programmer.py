class Programmer:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def printDetails(self):
        print(f"Programmer name is {self.name} and his salary is {self.salary} ")


p = Programmer("omkar" ,1000)
p.printDetails() 