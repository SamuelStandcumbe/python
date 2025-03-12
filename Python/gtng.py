import random

random_number = random.randint(1, 100)

print("The computer will generate a number betwenn 1 and 100, then you will guess that number. The amount of attemptswuill be recorded, so guess carefully!\n")
attempts = 0

guess = int(input("Make a guess: "))

while True:
    if guess != random_number:
        attempts += 1
        if guess == random_number:
                print(f"You win. It took you {attempts} attempts to guess the number.")
                break
        elif guess > random_number:
            print("Too high")
            int(input("Make another guess: "))
        elif guess < random_number:
            print("Too low")
            int(input("Make another guess: "))

