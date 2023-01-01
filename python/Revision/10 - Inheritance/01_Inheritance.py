class Car:
    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def milege(self):
        print("Mileage of this Car")


class tata(Car):
     pass

t = tata("solid","v6","aerial")
print(t.milege())
# c = Car()
print(t)