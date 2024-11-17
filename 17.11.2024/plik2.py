#Zadanie 1.1
# Stwórzmy pustą listę
# my_list = []
#  # Dodajmy wartości
# my_list.append("Python")
# my_list.append("is ok")
# my_list.append("sometimes")
 
# # Usuńmy 'sometimes'
# my_list.remove("sometimes")
 
# # Zmieńmy drugi element listy
# my_list[1] = "is neat"
 
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == ["Python", "is neat"]

#Zadanie 1.2
# #v0
# original = ["I","am", "learning","hacking", "in"]
# modified = original.copy()
# modified[3] = "lists"
# modified.append("Python")
# print(original)
# print(modified)
# # v2
# # modified = original.copy()
# # modified.append("Python")
# # modified[3] = "lists"
# # v3
# modified = [*original, 'Python']
# modified[3] = "lists"

#Zadanie 1.3
# list1 = [6,12,5]
# list2 = [6.2,0,14,1]
# list3 = [0.9]

# lista = sorted([list1, list2, list3], reverse=True)
# print(lista)

#Zadanie 1.2.1
# first_name ="John"
# last_name ="Doe"
# favorite_hobby= "Python"
# sports_hobby ="gym"
# age = 82
 
# # Twoja implementacja
# my_dict = {"name": f"{first_name} {last_name}", "age": age, "hobbies": [favorite_hobby,sports_hobby]}
# print(my_dict)
 
# # Sprawdźmyczy otrzymaliśmy poprawnywynik
# assert my_dict== {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}
 
#zadanie 1.2.2
# dict1 = dict(key1="This is not that hard", key2="Python isstill cool")
# dict2 = {"key1": 123, "special_key":"secret"}
# dict3 = dict([("key2", 456), ("keyX","X")])

# my_dict = {**dict1, **dict2, **dict3}
# print(my_dict)
# special_value = my_dict.pop("special_key")
# print(special_value)

#zadanie 1.3.1
name = "John Doe"
print(len(name))
if len(name) > 20:
    print(f'Name "{name}"is more than 20 chars long')
    length_description = "long"
elif len(name) > 15:
    print(f'Name "{name}"is more than 15 chars long')
    length_description = "semi long"
elif len(name) > 15:
    print(f'Name "{name}"is more than 10 chars long')
    length_description = "semi long"
elif len(name) in range (8,11): #zakres
    print(f'Name "{name}"is 8, 9 or 10 chars long')
    length_description = "semi short"
else:
    print(f'Name "{name}"is a short name')
    length_description = "short"
# Sprawdźmyczy otrzymaliśmy poprawnywynik
assert length_description == "semi short"