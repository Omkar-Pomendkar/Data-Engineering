# Sets a collection of non-repetative items

s ={ 1,2,34,5,5,5,4}
print(type(s))
print(s)

# Important 
# se = {} # this will create empty dictionary
# An empty set will be created using the below Syntax
a = {1,}
print(type(a))

a.add(12)
print(a)
# a.add([1,2,3,5])    # No you cannot add list and Dictionary in Set
a.add((2,3,67,56,6))
print(a)