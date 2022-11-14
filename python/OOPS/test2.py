import Util.util
from Util.util import Person2

p2 = Person2("Omkae","Pomendkar",2000)
print(p2.yob)
class Person1:
    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

omkar = Person1("Omkar","Pomendkar",2000)

print(omkar._name)
print(omkar._Person1__surname)
print(omkar.yob)

# single underscore means protected
# Double inderscore means private
