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
# name = "John Doe"
# print(len(name))
# if len(name) > 20:
#     print(f'Name "{name}"is more than 20 chars long')
#     length_description = "long"
# elif len(name) > 15:
#     print(f'Name "{name}"is more than 15 chars long')
#     length_description = "semi long"
# elif len(name) > 15:
#     print(f'Name "{name}"is more than 10 chars long')
#     length_description = "semi long"
# elif len(name) in range (8,11): #zakres
#     print(f'Name "{name}"is 8, 9 or 10 chars long')
#     length_description = "semi short"
# else:
#     print(f'Name "{name}"is a short name')
#     length_description = "short"
# # Sprawdźmyczy otrzymaliśmy poprawnywynik
# assert length_description == "semi short"

#zadanie 1.3.2

# words = ["PYTHON", "JOHN", "chEEse","hAm", "DOE", "123"]
# # upper_case_words= []
# # for x in words:
# #     if x.isupper():
# #         upper_case_words.append(x)
# # # Sprawdźmyczy otrzymaliśmy poprawnywynik
# # print(upper_case_words)
# # assert upper_case_words == ["PYTHON","JOHN", "DOE"]

# #alternatywne rozwiązanie
# upper_case_words = [x for x in words if x.isupper()] # alternatywa bez else
# upper_case_words = [x if x.isupper() else 1 for x in words ] # alternatywa bez else

# print(upper_case_words)

#zadanie 1.3.3
# magic_dict =dict(val1=44, val2="secretvalue", val3=55.0, val4=1)
 
# # Twoja implementacja
# sum_of_values = 0
# for x in magic_dict.keys():
#     if isinstance(magic_dict[x],(int, float)):
#         sum_of_values += magic_dict[x]
 
# # Sprawdźmyczy otrzymaliśmy poprawnywynik
# assert sum_of_values == 100
 
##sum_of_values1 = sum([magic_dict[key] for key in magic_dict.keys() if isinstance(magic_dict[key],(int, float))])

#zadanie 1.3.4

# numbers =[1, 3, 4, 6, 81,80, 100, 95]
#  # Twoja implementacja
# my_list = []

# for x in numbers:
#     if x % 5 == 0 and x % 2 != 0:
#         my_list.append('five odd')  
#     elif x % 5 == 0 and x % 2 == 0:
#         my_list.append('five even') 
#     elif x % 2 != 0:
#         my_list.append(odd)
#     elif x % 2 == 0:
#         my_list.append(even)

# # Sprawdźmyczy otrzymaliśmy poprawnywynik
# assert my_list== [
# "odd",
# "odd",
# "even",
# "even",
# "odd",
# "five even",
# "five even",
# "five odd",
#  ]

#zadanie 1.2.1

# score = {
#     (90, 100): 5.0,
#     (75, 89): 4.5,
#     (65, 74): 4.0,
#     (60, 64): 3.5,
#     (50, 59): 3.0,
#     (0, 49): 2.0
# }

# punkty = int(input("Podaj liczbę punktów: "))

# ocena = None
# for przedzial, ocena_wynik in score.items():
#     if przedzial[0] <= punkty <= przedzial[1]:
#         ocena = ocena_wynik
#         break


# print(f"Liczba punktów: {punkty}")
# if ocena >= 3.0:
#     print(f"Uzyskana ocena: {ocena}")
#     print("Student zaliczył zadanie")
# else:
#     print(f"Uzyskana ocena: {ocena}")
#     print("Student nie zaliczył zadania")

# zadanie 2.2

# seasons = {
# '1': 'zima', 'styczeń': 'zima',
# '2': 'zima', 'luty': 'zima',
# '3': 'zima', 'marzec': 'zima',
# '4': 'wiosna', 'kwiecien': 'wiosna',
# '5': 'wiosna', 'maj': 'wiosna',
# '6': 'wiosna', 'czerwiec': 'wiosna',
# '7': 'lato', 'lipiec': 'lato',
# '8': 'lato', 'sierpień': 'lato',
# '9': 'lato', 'wrzesień': 'lato',
# '10': 'jesień', 'październik': 'jesień',
# '11': 'jesień', 'listopad': 'jesień',
# '12': 'jesień', 'grudzień': 'jesień'
# }
 
# print(seasons[month] if month in seasons.keys() else "Podano miesiąc poza zakresem")

# month = input("Wprowadź miesiąc: ")
# seasons = {
#     ('1', '2', '3', 'styczeń', 'luty', 'marzec'): "zima",
#     ('4', '5', '6', 'kwiecień', 'maj', 'czerwiec'): "wiosna",
#     ('7', '8', '9', 'lipiec', 'sierpień', 'wrzesień'): "lato",
#     ('10', '11', '12', 'październik', 'listopad', 'grudzień'): "jesień",
# }
# season = None
# for key, value in seasons.items():
#     if month in key:
#         season = value
#         break
 
# #season = [value for key, value in seasons.items() if month in key][0]
 
# print(f'Pora roku dla miesiąca {month}: {season}')
 
 
 # Zadanie 2.3
# lista = ['tekst', 1, 1.5, True, [0]]
# print(len(lista))
# print(lista[0])
# print(lista[len(lista)//2])
# print(lista[len(lista)-1]) # print(lista[-1])
# print(lista)
# lista.insert(0, 'Pierwszy')
# lista.append('Ostatni')
# print(lista)
 
#zadanie 2.4
# Stwórz listę liczb od 1 do 10 włącznie, następnie posortuj ją malejąco. Pierwsze pięć elementów
# przypisz do nowej listy, następnie usuń z nowej listy element środkowy oraz posortuj rosnąco.
# Wyświetl listę po każdej modyfikacji. Dodatkowo sprawdź czy istnieje element o wartości 8, w
# jednej i drugiej liście, wyświetlając stosowny komunikat w przypadku jego istnienia, bądź braku.
# # Na końcu usuń obie listy.
# Przydatne: .sort(), sorted(), instrukcje warunkowe, len(), range(), del
# lista = [x for x in range(1,11)]
# print(lista)
# lista.sort(reverse = True)
# print(lista)
# nowa_lista = lista[:5]
# print(nowa_lista)
# nowa_lista.remove(nowa_lista[len(nowa_lista)//2])
# print(nowa_lista)
# nowa_lista.sort()
# print(nowa_lista)
# element = 8
# if element in lista:
#   print(f'W pierwszej liście występuje element {element}')
# if element in nowa_lista:
#   print(f'W nowej liście występuje element {element}')
# del lista
# del nowa_lista

 #zadanie 2.5

# a = int(input("Podaj liczbę: "))
# b = int(input("Podaj liczbę: "))
# inf3 = input("Podaj wartość do obliczeń (+, -, *, /): ")

# # Lista dozwolonych operatorów
# lista = ['*', '/', '+', '-']

# if inf3 in lista:
#     try:
#         expression = f"{a} {inf3} {b}"
#         result = eval(expression)
#         print(f'Wynik {a} {inf3} {b} to {result}')
#     except ZeroDivisionError:
#         print("Błąd: nie można dzielić przez zero.")
# else:
#     print("Nieprawidłowy operator.")

#zadanie 2.6
# inf3 = input("Podaj dwie liczby po przecinku i operator do obliczeń (+, -, *, /): ")

# wart = inf3.split(",")
# print(wart)
# x = wart[-1]
# lista = ['*', '/', '+', '-']

# if x in lista:
#     try:
#      expression = f"{wart[0]} {x} {wart[1]}"
#      result = eval(expression)
#      print(f'Wynik {wart[0]} {x} {wart[1]} to {result}')
#     except ZeroDivisionError:
#         print("Błąd: nie można dzielić przez zero.")
# else:
#     print("Nieprawidłowy operator.")

#zadanie 2.7 [value for key, value in dzialania.items() if k in key]
# lista = [-4, -3, -2, -1, 0, 3, 6, 9, 12]
# print([value for value in lista if value > 0])

#zadanie 2.8 - potęgowanie od 0 do 10
# wynik = [(i, 1, i, i**2, i**3) for i in range(11)]
# print(wynik)

#zadanie 2.9
# lista = [22, 19, 24, 25, 26, 24, 25, 24]
# zbior = set(lista)
# print(len(lista),len(zbior))

#zadanie 2.10 podaj tabliczkę dla podanej liczby
# x = int(input('Podaj liczbę: '))
 
# for y in range(1, 11): #pętla
#   print(f'{x} * {y} = {x * y}')

#zadanie 2.11
# parz = []       
# nieparz = []    

# for x in range(1, 101): 
#     if x % 2 == 0:
#         parz.append(x)  
#     else:
#         nieparz.append(x)  

# print(f'Suma parzystych: {sum(parz)}, Suma nieparzystych: {sum(nieparz)}')
# #alternatywa
# suma_parzyste = sum(i for i in range(101) if i % 2 == 0)
# suma_nieparzyste = sum(i for i in range(101) if i % 2 == 1)
 
# print(f'Suma liczb parzystych: {suma_parzyste}')
# print(f'Suma liczb nieparzystych: {suma_nieparzyste}')
 
#zadanie 2.12

# tekst = '"Uczę się Pythona, aby móc tworzyć aplikacje. Dużą zaletą Pythona jest to że jest bardzo zbliżony do języka angielskiego. Posiada prostą składnię, ale czasami potrafi być skomplikowany przez wysoki poziom abstrakcji. Jednak dobrze jest się nauczyć Pythona, aby dalej rozwijać się w stronę programowania."'
# zdania = tekst.split('. ')
# for zdanie in zdania:
#     print(zdanie)
#     slowa = zdanie.split(' ')
#     print(f'Liczba unikalnych słów: {len(set(slowa))}')
#     print(f'Liczba słów: {len(slowa)}')

#zadanie 2.13
# X = [
#     [12,9,3],
#     [4,5,6],
#     [7,8,3]
# ]
# Y = [
#     [9,8,1],
#     [6,7,3],
#     [4,5,9]
# ]
 
# result = []
# for i in range(len(X)):
#     row = []
#     for j in range(len(X[i])):
#         row.append(X[i][j] + Y[i][j])
#     result.append(row)
 
# assert result == [[21, 17, 4], [10, 12, 9], [11, 13, 12]]
 
#zadanie 2.14
X = [[12,9],
[7 ,3],
[5 ,6]]
result = [[0, 0, 0],
[0, 0, 0]]
 
for i in range(len(result)):
    for j in range(len(result[i])):
        result[i][j] = X[j][i]
 
assert result == [[12, 7, 5], [9, 3, 6]]
 