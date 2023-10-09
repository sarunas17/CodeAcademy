name = "code academy"
# print(name[::2])
# print(name.capitalize())

# print(name.replace("code", "music"))
# print(name[0:11])

# greeting = "Hello my name is"
# name = "Tom"
# completed_greeting = greeting + " " + name
# print(completed_greeting)

# print(type("labas"))

# number = 1

# string_number = str(number)
# print(type(string_number))

# excercise1

# my_name = input("enter your name:")
# my_age = input("enter your age:")
# int_age = int(my_age)
# year = 2023
# born_year = str(year - int_age)
# result = my_name + " " + my_age + " " + born_year
# print(result)

# excercise 2

# sentence = input("Enter sentence:")
# print(sentence [::-1])
# print(sentence[::2])

# excercise 3

# number_one = input("enter number one:")
# number_two = input("enter number two:")
# int_number_one = int(number_one)
# int_number_two = int(number_two)
# print(int_number_one * int_number_two)

#exercise 4


# text = input('Enter some text: ')
# print(text.replace('a', '4').replace('b','8').replace('c', '<').replace('d', '|)').replace('e', '3').replace('f', '7').replace('g','9').replace('h','|-|').replace('i','1').replace('j','_|').replace('k','|<').replace('l','|_').replace('m','|V|'))


text = input('Enter some text: ')
lowercase_text = text.lower()
replaced_text = lowercase_text.replace('a', '4').replace('b', '8').replace('c', '<').replace('d', '|)').replace('e', '3').replace('f', '7').replace('g', '9').replace('h', '|-|').replace('i', '1').replace('j', '|_').replace('k', '|<').replace('l', '|_').replace('m', '|V|').replace('n', '|\|').replace('o', '0').replace('p', '|o').replace('r', '|2').replace('s', '5').replace('t', '+').replace('u', '|_|').replace('v', '\/').replace('w', '\/\/').replace('x', '}{').replace('y', '\|/').replace('z', '7_')
print(replaced_text)

# text = input('Enter some text: ')
# mapping_table = str.maketrans({'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '|_|'})
# output_string = text.translate(mapping_table)
# print(output_string)