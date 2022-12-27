
# Use Open Function to read the File
# BY default the mode is r
f = open("Sample.txt","a")
# data = f.read()
# print(data)
# print(f.read(5))
# print(f.readlines())
# for i in f:
#     print(i)
f.write("My name is Omkar Pomendkar")
f.close()

# w - Overwriting the File
# a - Appending it in the Back

f = open("Sample.txt","r")
print(f.read())