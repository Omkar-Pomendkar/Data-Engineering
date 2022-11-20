# WAP to print table of 5

num = int(input("Enter a Number whose number you want to print the Table"))

def table(num):
    for i in range(1,11):
        print(f"{num}X{i}={num*i}")
    # 5X1=5


table(num) 