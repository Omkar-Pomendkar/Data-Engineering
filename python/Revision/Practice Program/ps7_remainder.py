# Write a program to print even odd Number
num = int(input("Enter a number"))
def even (num):
    if num%2 == 0:
        print(f"Number is even {num}")

def odd (num):
    if num%2 != 0:
        print(f"Number is odd {num}")

result = even(num)
result = odd(num)