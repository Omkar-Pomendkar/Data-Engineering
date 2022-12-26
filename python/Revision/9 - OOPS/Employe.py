class Employe:
    company = "Google"
    salary = 100

omkar = Employe()
sunil = Employe()
# omkar.salary = 400
# sunil.salary = 2000
print(omkar.company)
print(sunil.company)
# Ths is Class Attribute
Employe.company = "Youtube"
print(omkar.company)
print(sunil.company)
print(omkar.salary)
print(sunil.salary)
