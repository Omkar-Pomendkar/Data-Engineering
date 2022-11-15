"""
_ = protected
__ = private
   = public
"""

class Car:
    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def mileage(self):
        print("Mileage of this Car ")

c = Car("Solid","4 Stroke","MRF")
print(c)
class Tata(Car):
    pass
t = Tata("Solid", "2 Stroke","MRF")
print(t)
