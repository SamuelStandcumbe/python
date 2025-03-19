import random
random_number = random.randint(1, 100)

print("The computer will generate a number betwenn 1 and 100, then you will guess that number. The amount of attempts will be recorded, so guess carefully!\n")
attempts = 0

while True:  
    guess = int(input("Make a guess: "))
    attempts += 1
    
    if guess < random_number:
        if guess <= 0:
            attempts -= 1
            print("invalid guess. Number must be 1 or higher.")
        else:
            print("Too low.")
       
    elif guess > random_number: 
        if guess > 100:
            attempts -= 1
            print("Invalid guess. Number must be 100 or lower.")
        else:
            print("Too high.")
        
    elif guess == random_number:
        print(f"You win. It took you {attempts} attempts to guess the number.")
        if attempts == 1:
            print("Amazing! You managed to guess the number first try!")
        if random_number == 69:
            print("69. nice.")
        else:
            pass
        break
