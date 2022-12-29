import test1
pf = test1.Person("Sanjay","Pomendkar",2022)
print(pf)
class person:

    _name = "omkar"
    __surname = "pomendkar"
    dob = 2000

    # Protected
    def _age(self,current_year):
        return current_year-self.dob
    # Private
    def __age(self,current_year):
        return current_year-self.dob



p = person()
# Caling protected function
print(p._age(2023))
print(p._person__age(2023))
# print(p)

class employee(person):
    _name = "surbhi"
    __surname = "pomendkarrrrrrr"
    dob = 2006

e = employee()
# print(e)

print(e.dob)
print(e._employee__surname)
print(e._name)
print(e._age(2022))