# Fibonnaci Number
# 0 1,2,3,5,8
def fibo(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fibo(m-1)+fibo(m-2)

print(fibo(12))

# Over Here time is getting Exponrntially Increase