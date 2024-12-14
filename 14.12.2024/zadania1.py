import random
#zadanie 3.1
# def fz1 (r):
#     return r**2 + 4*r - 3
# print(fz1(0))
# print(fz1(1))
# print(fz1(2))
# print(fz1(3))
# print(fz1(4))

# #zadanie 3.2

# def fz2(a,b=2):
#     return a + b
# print(fz2(1))
# print(fz2(1, b=2))
# print(fz2(1,2))
# print(fz2(a=1, b=2))
# print(fz2(b=2,a=1))

# #zadanie 3.3
# '''
# Napisz funkcję, która przyjmuje jako argument listę liczb całkowitych, tworzy kopie tej listy i modyfikuje jej
#  kopie w następujący sposób:
#  • Usuwa wszystkie podzielne przez 3 liczby,
#  • Wkleja wartość-1 przed każdą liczbą parzystą.
#  Po dokonaniu modyfikacji zmodyfikowana wersja listy ma być zwrócona z funkcji. Przy tym funkcję należy
#  napisać tak, żeby lista, podana jako argument została niezmieniona. Zademonstruj działanie funkcji na liście
#  liczb losowych z zakresu od 0 do 10.
# '''
# def f3(lista):
#     nowaLista = lista.copy()
#     nowaLista = [x for x in nowaLista if x % 3 != 0]
#     wynik = []
#     for liczba in nowaLista:
#         if liczba % 2 == 0:  # jeżeli liczba jest parzysta
#             wynik.append(-1)
#         wynik.append(liczba)
#     return wynik
# # Lista losowych liczb z zakresu 0-10
# lista_oryginalna = [2, 3, 1, 5, 6, 3, 2, 4]
# # Wywołanie funkcji
# lista_zmodyfikowana = f3(lista_oryginalna)
# # Wyświetlanie wyników
# print("Oryginalna lista:", lista_oryginalna)
# print("Zmodyfikowana lista:", lista_zmodyfikowana)
# #zadanie 4
# '''
#  Utwórz funkcję, która przyjmuje trzy argumenty n, a, b i zwraca listę o długości n, wypełnioną losowymi
#  liczbami całkowitymi z zakresu od a do b. Argument n ma mieć wartość domyślną 10, argument a wartość
#  domyślną 0 i argument b wartość domyślną 10.
#  Użyteczne wyrażenia: def, return, random.randrange().
# '''

# def f4(n=10,a=0,b=10):
#     return [random.randrange(a,b) for i in range(n)]
       
# # print(f4()) 
# #zadanie 5
 
# def f5(n1):
#     listaLosowa = f4()
#     wylosowanaLiczba = random.choice(listaLosowa)
#     najwiekszaLiczba = max(listaLosowa)
#     indeksMin = listaLosowa[min(listaLosowa)]
#     sumaListy = sum(listaLosowa)
#     count5 = listaLosowa.count(5)
#     unikalne_liczby = list(set(listaLosowa))
#     return(listaLosowa,wylosowanaLiczba, najwiekszaLiczba,indeksMin, sumaListy,count5)

# print(f5(1))

# def iloczyn_kartezjanski(a, b):
#     wynik = [(x, y) for x in a for y in b]
#     return wynik

# # Przykład działania programu
# lista1 = [1, 2, 3]
# lista2 = ['a', 'b']

# iloczyn_kartezjanski_wynik = iloczyn_kartezjanski(lista1, lista2)

# print("Lista 1:", lista1)
# print("Lista 2:", lista2)
# print("Iloczyn kartezjański:", iloczyn_kartezjanski_wynik)

#zadanie 9
# def licz(a):
#     if isinstance(a, int):
#         wynik = a**2
#     elif isinstance(a, list):
#         wynik = [i ** 2 for i in a]
#     return wynik

# print(licz([1, 2, 3, 4, 5]))
# print(licz(2))    

#zadanie 10
# s = 'Ala ma kota'
 # def zamien(s):
#     return [ord(x) for x in s]
 # zamien(s)
def porownaj(a,b):
    zbior1 = set(a)
    zbior2 = set(b)

    unikalne = zbior1.union(zbior2)
    wspolneLiczby = zbior1.intersection(zbior2)
    tylko1Lista = zbior1.difference(zbior2)
    return unikalne, wspolneLiczby, tylko1Lista

lista1 = [random.randint(0, 10) for _ in range(10)]
lista2 = [random.randint(0, 10) for _ in range(10)]

# Wywołanie funkcji
unikalne_liczby, wspolne_liczby, tylko_w_a = porownaj(lista1, lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Zbiór wszystkich liczb unikatowych:", unikalne_liczby)
print("Zbiór liczb występujących jednocześnie:", wspolne_liczby)
print("Zbiór liczb występujących w pierwszej liście, ale nie w drugiej:", tylko_w_a)