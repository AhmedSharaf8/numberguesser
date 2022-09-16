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

#Computer Guesser
def computer_guesser(x):
    low = 1
    high = x
    feedback = ''
    guess = random.randint(low, high)
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The computer guessed {guess} correctly')
#Calling the function
# guess(10)
computer_guesser(10)
