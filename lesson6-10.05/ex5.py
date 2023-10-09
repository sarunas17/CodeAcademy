#write a program that allows user to write in any float number and then round it.


# float_number = float(input("Please enter the number: "))
# round_number = round(float_number)
# if float_number == round_number:
#     print("Please enter FLOAT number!!!")
# else:
#     print(f"Rounded number: {round_number}")



# number = input("Please enter float number: ")
# sub = "."
# index = number.find(sub)
# if index > 0:
#     float_number = float(number)
#     float_rounded_number = round(float_number)
#     print(f"Rounded number: {float_rounded_number}")
# else:
#     print("Please enter correct value")





number = input("Please enter float number: ")
round_digits = int(input("Please eneter decimal numbers: "))

if round_digits == '':
    round_digits = 0

replace_dot = number.replace(".","")
replace_comma = number.replace(",","")
is_true_dot = replace_dot.isnumeric()
is_true_comma = replace_comma.isnumeric()


# print(is_true_dot)
# print(is_true_comma)

if is_true_comma == True:
    rep_number = number.replace(",",".")
    float_number = float(rep_number)
    float_rounded_number = round(float_number, round_digits)
    print(f"Rounded number: {float_rounded_number}")
elif is_true_dot == True:
    float_number = float(number)
    float_rounded_number = round(float_number, round_digits)
    print(f"Rounded number: {float_rounded_number}")
else:
    print("Please eneter correct value")

# number = input("Please enter float number: ")
# sub = "."
# sub_two = ","
# index = number.find(sub)
# index_two = number.find(sub_two)
# replace_dot = number.replace(".","")
# replace_comma = number.replace(",","")
# is_true_dot = replace_dot.isnumeric()
# is_true_comma = replace_comma.isnumeric()

# print(is_true_dot)
# print(is_true_comma)

# if is_true_comma == True and index > -1 or index_two > -1:
#     rep_number = number.replace(",",".")
#     float_number = float(rep_number)
#     float_rounded_number = round(float_number)
#     print(f"Rounded number: {float_rounded_number}")
# elif is_true_dot == True and index > -1 or index_two > -1:
#     float_number = float(number)
#     float_rounded_number = round(float_number)
#     print(f"Rounded number: {float_rounded_number}")
# else:
#     print("Please eneter correct value")



#  number.isdecimal() == True:
#      float_number = float(number)
#      float_rounded_number = round(float_number)
#      print(f"Rounded number: {float_rounded_number}")
# else: 
#      print(by)


# elif number.isdigit() == False:
#      print("Please enter a float number, not a text!!!!!")

    