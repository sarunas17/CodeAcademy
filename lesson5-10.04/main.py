# my_dictionary = {"name": "Tom", "surname": "Edison"}
# print(f"name: {my_dictionary['name']}")
# print(f"surname: {my_dictionary['surname']}")

# my_dictionary = {}
# my_dictionary["name"] = "Tom"
# print(my_dictionary["name"])

# d = {'a': 10, 'b': 20, 'c': 30}
# print(list(d.items()))

# d = {'a': 10, 'b': 20, 'c': 30}
# print(list(d.keys()))

# d = {'a': 10, 'b': 20, 'c': 30}
# print(list(d.values()))

# d = {'a': 10, 'b': 20, 'c': 30}
# d.pop('a')
# print(d)

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 200, 'd': 400}
# d1.update(d2)
# print(d1)

# d = {'a': 10, 'b': 20, 'c': 30}
# for key, value in d.items():
#     print(key, value)

# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)

my_dictionary = {"name": "Sarunas", "surname": "Staskevicius"}
another_dictionary = {"street": "Kalvariju"}
# my_list = ["Vytautas", "Petras"]

print(my_dictionary["surname"])
my_dictionary["phone"] = 1235464
print(my_dictionary["phone"])

print(type(my_dictionary["phone"]))

my_dictionary["address"] = another_dictionary

print(my_dictionary["address"]["street"])

my_dictionary["name"] = "Petriukas"
del my_dictionary["name"]

my_dictionary.pop("name")


my_set = {1, 2, 3, 1, 1, 1, 2}
len 