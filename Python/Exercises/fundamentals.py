print("Welcome to the Personalised User Profile Generator\n\nThis program collects and processes user information.")

# Taking the name from the user and making the beginning of each name uppercase.
name = str(input("What is your full name?: "))
full_name = name.title()

# Splitting the name into just the first name
fname = full_name.split()[0]
len_full_name = len(full_name)

# Taking the age of the user and converting it to a float (from an int).
age_inp = int(input("What is your age?: "))
age_res = float(age_inp)

# Taking the height of the user and converting it to an int (from a float).
height_inp = float(input("What is your height in cm?: "))
height_res = int(height_inp)

# Taking the favourite programming language of the user.
fpl_inp = str(input("What is your favourite programming language?: "))
fpl_res = fpl_inp.replace("python", "a powerful language").replace("Python", "a powerful language")

# Taking the favourite number of the user and converting it to a str (from an int)
number_inp = int(input("What is your favourite number?: "))
number_res = str(number_inp)

# Taking the description of the user.
desc = str(input("Describe yourself: "))

# Spacing the input from the outputs
print("\n\n\n\n")

# Performing calculations & conditional logic

# Calculating the current date and time
from datetime import datetime
what_year_when_100 = 100 - age_inp + datetime.now().year

# Converting number_res to an integer and performing the calculation
number_res = int(number_res)  # Convert the number string to an integer
age_plus_number = age_res + number_res  # Now you can add them

def of_age():
    if age_inp >= 18:
        return "You are an adult"
    elif age_inp < 18:
        return "You are a minor"
    
# Reversing the user's name
rname = full_name[::-1]

# Spacing the user's name (adding a space between each character)
spaced_name = " ".join(full_name)

# Printing the users first name, the length of their full name, and their favourite programming language.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
print(f" * Hello {fname}. \n * Your full name has {len_full_name} letters. \n * Your favourite programming language is {fpl_res}.")
# Printing the calc+logic
print(f" * You will turn 100 in the year {what_year_when_100}. \n * Your age plus your favourite number is {age_plus_number}. \n * { of_age()}.")
# Printing the reversed name and the name with spaces after each letter
print(f" * Your name reversed in {rname}. \n * Your name spaced out is {spaced_name}")
print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
