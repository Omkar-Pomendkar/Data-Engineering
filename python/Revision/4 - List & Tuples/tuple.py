# You cannot update values of Tuple

# tuple can be change into list but cannot be modified
t = (1,2,3,5)
t = ()  # empty tuple
t = (1,)  # single item in tuples
print(type(t))
print(len(t))


d = (1,2,3,0,8,7,0)
print(d.count(0))