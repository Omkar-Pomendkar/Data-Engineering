class Person2:
    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

omkar = Person2("Omkar","Pomendkar",2000)

print(omkar._name)
print(omkar._Person2__surname)
print(omkar.yob)

# single underscore means protected
# Double inderscore means private