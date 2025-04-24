age = int(input("Please enter your age: "))

def is_valid_age(age) :

    if  age < 18 :
        print("False")
    elif  age > 65 :
        print("False")

print(is_valid_age(age))