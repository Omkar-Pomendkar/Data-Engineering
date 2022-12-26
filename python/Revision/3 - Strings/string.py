a = "omkar Pomendkar"
print(a)
print(a[:])
print(a[0:6])   # n-1
print(a[0::2])   # n-1  1 Skip
print(a[::-1])   # reverse
print(a[:9])     # till 9-1 = 8


# String Concatenation
b = "Hello"
c = " Good Morning Everybody"
print(b+ c)


# String Functions

story = "johnny johnny yes papa eating suger no papa"

print(story.capitalize())
print(story.upper())
print(story.lower())


# Escape Sequence
s = "Hello ,\n good morning Everybody \t \n Live Happy Life"
print(s)


# F String
a = "Omkar Pomendkar"
print(f"Hello Everybody {a}")


# Format String

age = 23
txt = "Hello , Everybody my Name {} and age is {}"
print(txt.format("OMKAR POMENDKAR" , age))


