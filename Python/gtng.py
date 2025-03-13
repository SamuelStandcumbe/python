
import random


random_number = random.randint(1, 100)

print("The computer will generate a number betwenn 1 and 100, then you will guess that number. The amount of attempts will be recorded, so guess carefully!\n")
attempts = 0

while True:  
    guess = int(input("Make a guess: "))
    attempts += 1
    
    if guess < random_number:
        print("Too low")
       
    elif guess > random_number:
        print("Too high")
        
    elif guess == random_number:
        print(f"You win. It took you {attempts} attempts to guess the number.")
        break
   
