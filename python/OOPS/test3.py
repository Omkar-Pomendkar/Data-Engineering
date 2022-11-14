import test2

p1 = test2.Person1("omkar","sanjay","pomendkar")
print(p1.yob)

class Person:
    _name = "omkar"             # private
    __surname = "Pomendkar"     # protected
    yearofbirth = 2000          # public

    def _age(self, current_year):
        return current_year-self.yearofbirth

    def __age1(self, current_year):
        return current_year-self.yearofbirth

p = Person()
print(p)

print(p._age(2022))
print(p._Person__age1(2019))



class Employee(Person):
    _name = "Surbhi"  # private
    __surname = "Poooomendkar"  # protected
    yearofbirth = 2016

e = Employee()
print(e)
print(e.yearofbirth)
print(e._name)
print(e._Employee__surname)

print(e._age(2022))
print(e._Person__age1(2022))
