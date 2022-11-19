try:
    a = int(input("Enter a Number"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a Valid Value")
    
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")
except Exception as e:
    print(e)
print("Thanks for using this code")
