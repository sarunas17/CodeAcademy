# Create a program, which takes 10 random numbers as user inputs.
# The program should produce list of input values what are less than 50 and tuple of all other values.
# After input is done, program should return the the mathematicaldiffernce between the highest and lowest number from non primary numbers, and sum of primary numbers from tuple.
 

number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
number_three = int(input("Enter number three: "))
number_four = int(input("Enter number four: "))
number_five = int(input("Enter number five: "))
number_six = int(input("Enter number six: "))
number_seven = int(input("Enter number seven: "))
number_eight = int(input("Enter number eight: "))
number_nine = int(input("Enter number nine: "))
number_ten = int(input("Enter number ten: "))

list_non_primary = []
tuple_list = []

if number_one < 50:
    list_non_primary.append(number_one)
else:
    tuple_list.append(number_one)
if number_two <50:
    list_non_primary.append(number_two)
else:
    tuple_list.append(number_two)
if number_three <50:
    list_non_primary.append(number_three)
else:
    tuple_list.append(number_three)    
if number_four <50:
    list_non_primary.append(number_four)
else:
    tuple_list.append(number_four)
if number_five <50:
    list_non_primary.append(number_five)
else:
    tuple_list.append(number_five)
if number_six <50:
    list_non_primary.append(number_six)
else:
    tuple_list.append(number_six)
if number_seven <50:
    list_non_primary.append(number_seven)
else:
    tuple_list.append(number_seven)
if number_eight <50:
    list_non_primary.append(number_eight)
else:
    tuple_list.append(number_eight)
if number_nine <50:
    list_non_primary.append(number_nine)
else:
    tuple_list.append(number_nine)
if number_ten <50:
    list_non_primary.append(number_ten)
else:
    tuple_list.append(number_ten)


print(list_non_primary)
print(tuple(tuple_list))

print(max(list_non_primary) + min(list_non_primary))

print(sum(tuple_list))

sum = 0
for numbers in tuple_list:
    sum = sum + numbers
print(sum)

