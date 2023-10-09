#create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

my_list = [1.569, 9.897, 10.458, 5.217, 8.154, 6.489, 4.501, 3.098]

rounded_list = []

for numbers in my_list:
    rounded_list.append(round(numbers, 2))

print(rounded_list)