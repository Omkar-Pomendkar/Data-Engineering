class Person:
    # Self is a pointer pointing to a class
    def __init__(self,name,surname,email,dob):
        self.name = name
        self.surname = surname
        self.email = email
        self.dob = dob
        # Try to calculte age of a Person
    def age (self ,current_year):
            return current_year - self.dob


omkar_var = Person("omkar", "pomendkar", "omkarpomendkar100@gmail.com", 2000)
print(omkar_var.name)
print(omkar_var.surname)
print(omkar_var.email)
print(omkar_var.dob)

sunil = Person("Sunil","Mane","sunil@gmail.com",1987)
print(sunil.name)
print(sunil.surname)
print(sunil.email)
print(sunil.dob)
print(type(sunil))
print(omkar_var.name + omkar_var.surname)

print(omkar_var.age(2022))
print(sunil.age(2022))