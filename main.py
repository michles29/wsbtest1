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

# jak dodamy trzeci argument, np. -1 to liczymy od kończa, gdy zrobię ranch(6,1,-1) to leci od 6 w dół,
# bez ostatniej wartosći
# for x in range(1,6): 
#     print(x)

#tablice, listy    
lista_liczb = [1,2,3,4,5, 'tekst']
#print(lista_liczb[5])
#print(lista_liczb[-1]) #ostatnia wartość z tablic
#print(lista_liczb[:2]) #zaczyna od poczatku do 
#print(lista_liczb[1:]) # od elementu 1 do końca

# my_list = list(range(5))
# print(my_list)
# for i in range(len(lista_liczb)): # wykorzystuje tablice - # tożsame z funkcja enumeratywna
#     print(i,lista_liczb[i])

# #cfor i in range(len(lista_liczb)):
# for i in lista_liczb:
#     print(i)    

#funkcja enumeratywna - zwraca pare, indeks i jego wartość w liście
# for iterator, value in enumerate(lista_liczb):
#     print(iterator, value)
# #funkcja zip    - łączy listy, tyle wartosci pokaże ile jest w obu
# lista_tekstu = ['a','b', 'c','d','e']
# for value1, value2 in zip(lista_liczb, lista_tekstu):
#     print(value1, value2)
# #dodanie do listy lista.append
# print(lista_tekstu)
# lista_tekstu.append('f')
# print(lista_tekstu)
# #extend - mogę dodać do listy inna listę
# #insert - wstawia element w konkretny indeks lista.insert(2,10)
# #remove - wstawia element w konkretny indeks lista.insert(3) - usunie 3 liste z pozycji
# #pop 
# z = lista_tekstu.pop() # usuwa ostatnią wartość oraz ją wyświelta, dodaje do zmiennej
# print(z)
#index
#count
#sort lista_liczb.sort, lista_liczb.sort(reverse=true)
#reverse lista_liczb.reverse

# krotka - listy można modyfikować, krotek nie
# lista_krotek = (1,2,3,4,5,6,0)
# print(lista_krotek)

# #słownik - struktura danych, która przechowuje pary klucz, wartosc
# slownik ={
#     'klucz1': 'wartosc 1',
#     'kluucz2':'wartosc2'}
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())
# #funkcja get
# print(slownik.get('klucz1'))
# print(slownik.pop('klucz1'))
# print(slownik.popitem())
#print(slownik.update({'klucz1': 'wartosc sdfsdfs'}))
# print(slownik.clear())

#zbiór - set empty_set = {()} - utworzenie pustego zbioru

#String
# text = "Python jest ciekawy"
# words = text.split()
# print(words) #domyślnie dzieli po spacji
# sentance = 'TEST'.join(words)
# print(sentance)
#Capitalize - 
#obsługa błędów - analogicznie do try catch
# try:
#       10/0 
# except ZeroDivisionError as e:
#      print('Obsługa błędu')
#      print(e)
# except:
#      print('Błąd ogólny')
# finally: #uruchomi się zawsze, bez względu czy wystąpi błąd czy nie
#      print('na końcu')
#nie działa mi to poniżej
# age = 19
# def calcualte_age(age):
#     if age < 18:
#         raise ValueError ("Nie mniejszy niż 18 wiek")
        
#     if age > 18:    
#         print('Wiek podany jest poprawnie')

#otwieranie plików - konstrukcja f
#f = open('file.txt', 'w', encoding="utf-8") - trzeba pamiętać o zamykaniu pliku f.close(), tak
#ab zamknąć połączenie z plikiem
#otwierania w open() i czytanie zawartości pliku, z automatu zamykamy plik
# with open('file.txt', 'r',encoding="utf-8") as plik:
#     #operacja na pliku
#     dane = plik.read() # jeżeli chcemy mieć tekst linijka po linijce to .redlines()
#     print(dane)

# with open('file.txt', 'a',encoding="utf-8") as plik:
#     #operacja na pliku
#     dane = plik.write('Nowy tekst') # jeżeli chcemy mieć tekst linijka po linijce to .redlines()
#     print(dane)

#IMOPRT PLIKÓW Z OS - systemu
# import os

# current_path = os.path
# print(current_path)

#JSON w Python
#csv - csv.reader

# original = " Python string are COOL"
# lower_cased = original.lower()
# stripped = original.strip()

# ugly = "TiTle of MY new Book\n\n"
# print(ugly)
# pretty = ugly.strip().title()
# print(pretty)

a = 2
b = 3
c = 2

result = 6*(a**3) - (8*(b**2))/