# # Simple print
# print("hello world")

# # Gets the same result but slightly different:
# print("hello", "world", 8)

# # Gets the same result but is even more different:
# print(*["hello", "world"])

# # let's play with separator:
# print("hello", "world", "byebye", sep=", ")

# # some more
# print("hello", "world", sep=" amazing ")

# print("hello", "world", sep=" amazing ", end = ".\n", flush=False )

# greet = "Hello World"
# print(type(greet))

# number = 2022
# print(type(number))

# my_list = [1, 2, 3]
# print(type(my_list))

# print(type(my_list[0]))

# print(round(1.999))

# print(round(1.5555, 2))

# print(round(1.5))
# print(round(2.5))
# print(round(3.5))
# print(round(4.5))
# print(round(5.5))


# my_digits = [1.5, 2.9, 3.4, 9.8]

# rounded_stuff = []
# for number in my_digits:
#     rounded_stuff.append(round(number, 3))

# print(rounded_stuff)

my_list = [45, 20, 14, 55]
sorted_list = sorted(my_list)

print(*sorted_list, sep=" - ")

sorted_reverse_list = sorted(my_list, reverse=True)

print(sorted_reverse_list)

my_list = ["Albert", "Nicola", "Thomas"]
sorted_list = sorted(my_list)

print(sorted_list)

sorted_reverse_list = sorted(my_list, reverse=True)

print(sorted_reverse_list)