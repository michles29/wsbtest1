#tworzenie funkcji - zawsze dwukropek
liczba1 = 1
liczba2 = 2

# def f(liczba1,liczba2):
#     return liczba1 * liczba2

# print(f(9,2))
# print(f(0,1))
# print(f('10','10')) #nie pomnoży
# print(f('99',2)) # to pomnoży razy 2 i będzie 9999

def f(liczba1, liczba2, operator='+', *args, **kwargs): # możemy do funkcji dodać nieskończoną ilość parametrów
    '''
    Opis co robi funkcja

    Parameters
    ---------------
    '''
    
    print(args)
    wynik = 'brak'
    if operator == '+':
        return wynik == liczba1 + liczba2
    elif operator == '-':
        return wynik == liczba1 - liczba2
    elif operator == '*':
        return wynik == liczba1 * liczba2
    elif operator == '/':
        return wynik == liczba1 / liczba2
    
    return wynik, args, kwargs

print(f(1,10))
print(f(10,1, operator='/'))
print(9.102, 4.2312, '*', 0,1,2,3,liczba3=10)
wynik = f()
print(wynik[0])
