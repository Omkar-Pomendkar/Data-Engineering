class Car:
    print("Omkar Pomendkar")
    x = 5

c = Car()
print(c.x)


# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Omkar",22)

print(p.name)
print(p.age)