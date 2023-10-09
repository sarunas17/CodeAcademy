# lowerlimit_weight: float = 40.5 
# higherlimit_weight: float = 100.0

# weight = float(input("Enter your weight: "))

# if weight > higherlimit_weight:
#     if weight > 125.5:
#         print("What the fuc?")
#     print("Mindaugas is kebab")
# elif weight < lowerlimit_weight:
#     print("Mindaugas is hungry")
# else:
#     print("Mindaugas is cool")

# if weight > higherlimit_weight:
#     print("Mindaugas is kebab")
# print("Test is sucssesfull")

# a = 50
# b = int(input("Enter number: "))
# if b >= a:
#     print(b)
# else:
#     print(a)

# a = int(input("Enter number one:"))
# b = int(input("Enter numer two:"))
# c = int(input("Enter number three:"))
# d = int(input("Enter number four:"))
# if a < b and b < c:
#     print(f"first condition met - {b}")
# elif a > c:
#     print(f"second condition met - {d}")
# else:
#     print(f"third condition met. First number - {a}, second number - {b}, third numer - {c}, fourth number- {d}")

#Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# name = (input("Please anter your name: "))
# surname = (input("Please enter your surname: "))
# age = int(input("Please enter your age: "))
# if age >= 21:
#     print("User is allowed to enter an online casino")
# else:
#     print("User is not allowed to enter an online casino")

#allow user to enter two numbers, print out which one is higher than the other, or are they equal?

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print(f"Number one {a} is higher than number two {b}")
# elif a == b:
#     print(f"Number one {a} equal number two {b}")
# else:
#     print(f"Number two {b} is higher than number one {a}")

#Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

# name = input("Please enter yuor name: ")
# priv_users = ["Antanas", "Petras", "Jonas", "Kazys", "Rimas"]
# if name in priv_users:
#     print(f"Hello dear, {name}")
# else:
#     print("Welcome")

#Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.

# a = int(input("Please enter numer one: "))
# b = int(input("Please enter number two: "))
# c = input("Please enter mathematical symbol: ")
# if c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# elif c == "*":
#     print(a*b)
# elif c == "/":
#     print(a/b)
# else:
#     print(f"We do not support this symbol {c}")

#create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)

import random

#from random import randint

 

random_number = random.randint(1, 10)

#random_number = randint(1, 10)

guess_number = int(input("Guess the number from 1 to 10: "))

 

if guess_number == random_number:

    print(f"You've guessed it! It is {random_number}")

else:

    print(f"You haven't guessed, the right answer is {random_number}")