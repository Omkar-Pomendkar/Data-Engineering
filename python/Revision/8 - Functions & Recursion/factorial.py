# 3! = 3 x 2!
# 2! = 2 x 1!
# 1! = 1
def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)

result = fact(3)
print(result)