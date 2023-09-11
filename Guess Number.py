import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print("You guessed correct")


def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f"is {guess} too high(H), too low(L) or correct (C)    ").lower()
        if feedback == 'h':
            high = guess - 1 #Adjust upper bound
        elif feedback == 'low':
            low = guess + 1

    print("Computer guessed correctly")

computer_guess(10)