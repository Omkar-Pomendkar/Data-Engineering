class Employee:
    company = "Viza"
    ecode = 123
class Freelancer:
    company = "Fiver"
    level = 0

    def upgradelevel(self):
        self.level = self.level+1

class Programmer(Freelancer,Employee ):
    name = "omkar"

P = Programmer()

print(P.level)
P.upgradelevel()
print(P.level)
print(P.company)
