#generates a random number
import random
random_number = random.randint(1, 100)

#prints a welcome message and creates the attempts variable.
print("The computer will generate a number between 1 and 100, then you will guess that number. The amount of attempts will be recorded, so guess carefully!\n")
attempts = 0

#a while loop that creates the game.
while True:  
    #allows the user to guess and adds one to the total number of attempts with every guess.
    guess = int(input("Make a guess: "))
    attempts += 1
    
    #if the guess is too small it tells the user, also includes validation that takes away an invalid guess and tells the user if a guess is invalid.
    if guess < random_number:
        if guess <= 0:
            attempts -= 1
            print("invalid guess. Number must be 1 or higher.")
        else:
            print("Too low.")
       
    #if the guess is too large it tells the user, also includes validation that takes away an invalid guess and tells the user if a guess is invalid .
    elif guess > random_number: 
        if guess > 100:
            attempts -= 1
            print("Invalid guess. Number must be 100 or lower.")
        else:
            print("Too high.")

    #if the guess is the same as the random number, it tells the user the number of attempts, and prints unique messages based on number of guesses and certain numbers.
    elif guess == random_number:
        print(f"You win. It took you {attempts} attempts to guess the number.")
        if attempts == 1:
            print("Amazing! You managed to guess the number first try!")
        elif attempts >= 10:
            print("More than 10? Really?")
        if random_number == 69:
            print("69. nice.")
        else:
            pass
            break