# WAP to guess a Number
import random
num = random.randrange(1,10)
print(num)
guess = int(input("Enter any Number"))
while num != guess:
    if guess < num:
        print("Too low")
        guess = int(input("Enter any Number"))
    elif guess > num:
        print("Too high")
        guess = int(input("Enter any Number"))
    else:
        break
print("you have guessed right")
