# Filter Syntax
def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

l = [1,2,3,4,5,67,78,88,99]
# Method 1
print(list(filter(greater_than_5 , l)))


# Method 2
a = lambda num : num>3
print(list(filter(a,l)))