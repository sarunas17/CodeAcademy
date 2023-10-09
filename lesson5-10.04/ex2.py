#Try creating structure like one here: link from an empty dictionary: my_dict = {}

my_dict = {}
my_dict["name"] = "Sarunas"
my_dict["surname"] = "Staskevicius"
my_dict["phone"] = 6874125635


address_dict = {}
address_dict["street"] = "Kalvariju"
address_dict["number"] = 15
address_dict["zip code"] = "LT-898989"
address_dict["city"] = "Vilnius"
address_dict["country"] = "Lithuania"

my_dict["address"] = address_dict

hoby_dict = {}
hoby_dict["inside"] = "basketball"
hoby_dict["outside"] = "tennis"

my_dict["hobbies"] = hoby_dict

my_occupation = {"role": "proffesor", "workplace": "University"}
my_dict["occupation"] = my_occupation

print(my_dict)