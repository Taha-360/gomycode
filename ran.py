import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    secret_number = random.randint(1, 100)
    guessed = False
    
    while not guessed:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Your guess is too low. Guess again.")
        elif guess > secret_number:
            print("Your guess is too high. Guess again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            guessed = True

guess_the_number()
