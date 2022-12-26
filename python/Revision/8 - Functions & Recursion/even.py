def is_even(num):
    """ To Check whether number is even or Odd"""
    # print("Number is Even")
    # return num%2 == 0
    if type(num) == int:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Not a Number")