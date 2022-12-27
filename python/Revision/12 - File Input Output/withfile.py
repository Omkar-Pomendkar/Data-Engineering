with open("test.txt","x") as f:
    f.write("This is using with function which helps us to close the file automatically")

with open("test.txt","r") as f:
    a = f.read()
    print(a)
