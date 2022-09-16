#Importing liberaries
import random

#The function
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print(f"Sorry, {guess} is too low guess again")
        elif guess > random_number:
            print(f"Sorry, {guess} is too high guess again")
    print(f"You got it {guess} is just the number you are looking for")

#Calling the function
guess(10)
