# Iterative vs Recursion
# Create a Multiplication recursive program
# Multiplication is nothing but Repeted Addition
def multiply(a,b):
    result = 0

    for i in range(b):
        result = result+a

    print(result)

r = multiply(2,3)
print(r)

# Base Case 
# How you break down your bigger problem in Smaller parts

multiply (3,4)
3+3+3+3
3+ 3*3
3 + 3 + 3*2
3 + 3 + 3 + 3*1

# if b = 1 , a*b => a
# over  here condition becomes if b = 1 return 3

def mul (a,b):
    if b == 1:
        return a
    else:
        return a+mul(a,b-1)

mul(3,4)


