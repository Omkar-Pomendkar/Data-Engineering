class Employee:
    def __init__(self,name,surname,email,dob):
        self.name = name
        self.surname = surname
        self.email = email
        self.dob = dob

    

e = Employee("Omkar","Pomendkar","omkarpomendkar100@gmail.com",2000)
print(e.name)
print(e.surname)
print(e.email)
print(e.dob)

