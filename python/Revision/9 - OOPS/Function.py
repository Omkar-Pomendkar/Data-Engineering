# This is a Function which prints good morning

def greet():
    print("Hello Good Morning")

happy = greet()
print(happy)


# Function with Arguments
def fullname(fname = "Omkar"):
    print(fname+"Pomendkar")

fullname()

# Function with multiple Arguments
def Car(*args):
    print("Types of Cars"+args[1])

Car("BMW"," Mercedes","Totyota")

def Sum(a,b):
    return a+b

d = Sum(10,20)
print(d)

# Passing a list to Function as an Argument

def func1(food):
    """ Passing a list to Function as an Argument"""
    for i in food:
        print(i)
fruits = ["Apple","Mango","Banana"]
func1(fruits)

s = "Omkar Pomendkar"

def read(x):
    for i in x:
        print(i)

read(s)