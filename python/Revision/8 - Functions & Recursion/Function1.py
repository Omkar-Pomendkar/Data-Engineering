def is_even(num):
    """ To Check whether number is even or Odd"""
    # print("Number is Even")
    # return num%2 == 0
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


is_even(10)


for i in range(1,10):
    print(is_even(i))

print(is_even.__doc__)