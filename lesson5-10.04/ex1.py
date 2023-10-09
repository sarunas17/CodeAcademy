#Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary

name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
age = input("Please enter your age: ")

# my_dictionary = {}
# my_dictionary["name"] = name
# my_dictionary["surname"] = surname
# my_dictionary["age"] = age

my_dictionary = {"name": name, "surname": surname, "age": age}

# my_dictionary.update([("name", name), ("surname", surname), ("age", age)])

print(my_dictionary)

print(f"User name is {my_dictionary['name']}, user surname is {my_dictionary['surname']}, user age is {my_dictionary['age']}")