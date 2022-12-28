def run():
    while True:
        try:
            value = int(input("Enter the Number"))
            break
        except:
            print("looks like you have entered a String")
            continue
    return value
r = run()
print(r)