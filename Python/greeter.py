def greet_user(name):
    print(f"Hello {username}! Welcome back.")

username = input("Please enter your name: ")
name = username.capitalize()

def get_favourite_subject():
    fsi = input("Please enter your favourite subject: ")
    if fsi == "Python" or "python":
        print("Great choice! Python is awesome!")
    global subject
    subject = fsi.capitalize()
    
def print_summary(name, subject):
    print(f"{name}'s favourite subject is {subject}.")

greet_user(name)
get_favourite_subject()
print_summary(name, subject)