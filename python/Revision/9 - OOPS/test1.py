# Access Modifiers
'''
1) Public  - name
2) Private - __name
3) Protected - _Protected

'''

class Person :
    def __init__(self,name,surname,yob):
        self.name = name
        self.__surname = surname
        self.yob = yob

p = Person("Omkar","Pomendkar",2000)
print(p.name)
print(p._Person__surname)
print(p.yob)
