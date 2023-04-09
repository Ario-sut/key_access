import random

number = random.randint(1,99) 
guess = int(input("Enter an integer from 1 to 99 : "))


while True:
    if guess < number:
        print("The integer is too low")
        guess = int(input("Enter an integer from 1 to 99 : "))
    elif guess > number:
        print("The integer is too high")
        guess = int(input("Enter an integer from 1 to 99 : "))
    else:        
        print("That's the Right Answer")
        break

