
# Create a function to add 2 Numbers
def sum(a,b):
    c = a+b
    return c 

d = sum(9,8)
print(d)

# Function to print Hello World

def great():
    print("Hello Everybody")

great()

# Function with 2 Arguments

def fullname(firstname,lastname):
    print(firstname+lastname)

fullname("Omkar" , "Pomendkar")

# Function with more Arguments (*args Keyword)
# Function will receive a tuple of arguments

def cars(*args):

    print("My Favourite Car is" + args[1] + args[0]) 

cars("BMW","Mercedes")


# Function with more Arguments (*args Keyword)
# Function will receive a dictionary of arguments

def familyname(**kwargs):

    print("My First Name is "+ kwargs["lastname"] + kwargs["firstname"] )

familyname (firstname = "Omkar" , lastname = "Pomendkar")

# Function with Default Parameter

def country(city = "Mumbai"):
    print( city +" city is beautiful")

country("Banglore")
country()


# Passing a list as a Argument
fruits = ["Orange","Mango"]
def func(fruits):
    for i in fruits:
        print(i)

func(fruits)

# Passing a String as a Argument
fruits = "orange"
def func(fruits):
    for i in fruits:
        print(i)

func(fruits)

# Passing a Dictionary as a Argument
fruits = {1:"One",2:"Two"}
def func(fruits):
    for i in fruits:
        print(i)

func(fruits)


# Function returning Values 
def Mul(x):
    return x*5

s = Mul(10)
print(s)
