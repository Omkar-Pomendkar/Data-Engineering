# Python contains 4 Types of Arguments
'''
1) Default Arguments
2) Positional Arguments
3) Keyword Arguments
4) Arbitary Arguments
'''

# Parameters Vs Arguments
# Parameters - When you create a function at that time parameters are given
# Arguments - When you give agruments as number to a function

# Default Arguments
def power(a =3 ,b = 2):
    return a**b

d = power(5)
print(d)

# positional Arguments this behaviour is called
#  power(2,3)

# Keyword Arguments
t = power(a=3,b=2)
print(t)

# Arbitary Arguments
def flexi(*args):
    product = 1
    # print(args)
    for i in args:
       
        product = product*i

    print(product)

flexi(1,2,3,4,5,6,7,8,9,10)


# What all functions can do ?
#


f = flexi
d = f(5,9)

d(5,8)