print("Welcome to the multiplication table generator. The user will input a number and the table will be generated based on .\n\n")

def multiplication_table(number, limit):

    if number < 0:
        print("Invalid number. Try again")
        

    for x in range(1, limit + 1):
            print (f"{number} * {x} = {x * number}")
            if limit == 5:
                break
    else:
        print("Table done")

number = int(input("Please enter a number: "))
limit = int(10)
multiplication_table(number, limit)
