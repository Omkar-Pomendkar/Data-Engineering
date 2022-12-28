# Try - Blocks execute block of code of Error
# Except - Lets you handle the Exception
# else - The else block lets you execute code when there is no error.
# finally - The finally block lets you execute code, regardless of the result of the try- and except blocks.

a = 10
#print(a/0)

try:
    f = open("ant.txt","r")
    print("Hello Everybody")

except FileNotFoundError as f:
    print(f)
#
# try:
#     a = 10
#     a/0
# except Exception as e:
#     print(e)