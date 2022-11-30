num1 = int(input("Enter Number1"))
num2 = int(input("Enter Number2"))
num3 = int(input("Enter Number3"))
num4 = int(input("Enter Number4"))

# if (num1 > num2 > num3 > num4):
#     print(num1)
# elif (num2 > num1 > num3 > num4):
#     print(num2)
# elif (num3 > num1 > num2 > num4):
#     print(num3)
# else:
#     print(num4)

if(num1 > num4):
    f1 = num1
else:
    f2 = num4

if (num2 > num3):
    f1 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1))
else:
    print(str(f2))