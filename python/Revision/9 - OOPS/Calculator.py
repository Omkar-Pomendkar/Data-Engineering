class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The Value of {self.num} square is {self.num ** 2}")
    def squareRoot(self):
        print(f"The Value of {self.num} squareRoot is {self.num ** 3}")

    def cube(self):
        print(f"The Value of {self.num} Cube is {self.num ** 0.5}")

    @staticmethod
    def great():
        print("Hello and welcome to the best Calculator of the World ******")

a = Calculator(3)
a.square()
a.squareRoot()
a.cube()
a.great()