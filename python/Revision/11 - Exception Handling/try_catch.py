
while(True):
    print("Enter q to Exit")

    a = input("Enter a number : ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6 :
            print("Number enter is greater then 6 ")
    except Exception as e :
        print("Your input resulted in ")

print("Thanks for playing this game")