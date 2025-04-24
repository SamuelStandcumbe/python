print("Welcome to the multiplication table generator. The user will input a number and the table will be generated based on .\n\n")

def multiplication_table(number, limit):

    if number < 0:
        print("Invalid number. Try again")
    
    for x in range(1, limit + 1):
            print (f"{number} * {x} = {x * number}")

number = int(input("Please enter a number: "))
if number == str:
    print("Invalid Number")

limit = int(input("Please enter a second number: "))
if limit == 0:
    print("Invalid limit, please enter a positive number greater that 0")

multiplication_table(number, limit)