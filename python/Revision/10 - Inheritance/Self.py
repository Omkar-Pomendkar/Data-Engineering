class Employe:
    company = "Google"
    def getSalary (self):
        print(f"Salary of this emplyee working in {self.company} is {self.salary}")
    @staticmethod
    def great():
        print("Good Morning everybody")

    @staticmethod
    def time():
        print("The Time is 14:34 pm")

omkar = Employe()
omkar.salary = 100000
omkar.getSalary()
print(omkar.company)
omkar.great()
omkar.time()
#Employe.great()

