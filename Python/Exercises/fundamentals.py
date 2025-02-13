print("Welcome to the Personalised User Profile Generator\n\nThis program collects and processes user information.")

# Taking the name from the user and making the begining of each name uppercase.
name = str(input("What is your full name?: "))
full_name = name.title()

# Splitting the name in to just the first name
fname = full_name[ :6]
len_full_name = len(full_name)


# Taking the age of the user and converting it to a float (from an int).
age_inp = int(input("What is your age?: "))
age_res = float(age_inp)

# Taking the height of the user and converting it to a int (from an float).
height_inp = float(input("What is your height in cm?: "))
height_res = int(height_inp)

# Taking the favourite programming language of the user.
pl = str(input("What is your favourite programming language?: "))
fpl = pl.replace("python" or "Python", "a powerful language")

# Taking the favourite number of the user and converting it to a str (from an int)
number = int(input("What is your favourite number?: "))
favourite_number = str(number)

# Taking the deascription of the user.
desc = str(input("Describe yourself: "))

print("\n\n\n")

# Printing the converted outputs

print(f"Hello {fname}. \nYour full name has {len_full_name} letter. \nYour favourite programming language is {fpl}.")