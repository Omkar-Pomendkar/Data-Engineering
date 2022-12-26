class Employee:
    company = "Camlin"
    salary = 100
    location = "Delhi"
    #
    # def changeSalary(self,sal):
    #     # This is called Dunder Method
    #     self.__class__salary = sal
    #
    #
    @classmethod
    def changeSalary(cls,sal):
        # This is called Dunder Method
        cls.salary = sal

e = Employee()

print(e.salary)
e.changeSalary(300)
print(Employee.salary)
print(e.salary)
print(Employee.salary)