#https://www.algorytm.edu.pl/wstep-do-python/operatory-w-python
#zmiene w python to int = liczba całkowita, float 1.1, str = '', bolean(true, false)
# a = 5
# b = 'TEST'
# #sprawdzanie typow zmiennych
# print(type(a)) # test sprawdzanie typu zmiennej
# print(isinstance(a, str)) # spraw czy jest stringiem
# print(isinstance('hello', (int,str))) # jeżeli wartość jest int lub str to true
# #używanie zmiennych
# print(f'Wartość {a}') #użycie funkcji, która wstawia w zmienna tekst
# print('Wartosć sfsdfs ' + b) # można też tak
# print('Name A:',a, 'Wartość B', b)
# c = None # to taki null
# print(c)

# #zawsze musi być wcięcie Tak jak wywołujemy funkcje
# if c is None:  
#     print( "zmienna 'c' hest None.") 
#     print("linia dwa")


# #input - w terminalu wyskoczy to co jest w input i możemy coś wpisać
# #user_input =input("Wprowadź dane: ")
# #print(user_input) #wyświetlni to co

# pole = 25.1213131
# print(f"Pole wynosi : {pole: .2f}") # ile chcemy wyświetlić po przecinku
# print(pole)

# print("Hello", end=" ")
# print("World")
# #wykorzystywanie biały znaków
# print('''
# test
#       test
#       test
#       ''')

#konwersja zmiennych
#print(str(42)), bool('true'), int('1.99'), floa('1') #alt+ shift

# a = 3
# b = 2
# print(f"{a + b}")
# print(f"{a - b}")
# print(f"{a * b}")
# print(f"{a / b}")
# print(f"{a % b}")
# print(f"{a - b}")

#operatory porównania
#== równe
#!= różne, >, <, >=, <=

#instrukcja warunkowa, zawsze dwukropek, potem wcięcie
# x = 10
# if x > 10:
#     print("x jest większe")
# elif x == 10:
#     print('x równa się 10')
# else:
#     print('x jest mniejsze od 10')

#pętla while lub for
# i = 1 
# while i<=5:
#     print(i)
#     i += 1
# print(i)
for x in range(1,6):
    print(x)