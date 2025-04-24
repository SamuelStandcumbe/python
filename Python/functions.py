def family_tree(fname):
    print(fname + " " + "Standcumbe")

def add_person(fname, lname):
    print(fname + " " + lname)

def add_siblings(*sibling):
    print("I love my sibling " + sibling[0])

family_tree("Samuel")
family_tree("John")
family_tree("Steve")

add_siblings("Steve", "John", "Matt", "Kyle")