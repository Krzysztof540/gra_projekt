import random
import os

tabela = []
wybraneLiczby = []

for i in range(9):
    tabela.append(' ')


def plansza(tabela):
    board = f"""
   {tabela[0]} | {tabela[1]} | {tabela[2]}       1 | 2 | 3  
  ---|---|---     ---|---|---
   {tabela[3]} | {tabela[4]} | {tabela[5]}       4 | 5 | 6 
  ---|---|---     ---|---|---
   {tabela[6]} | {tabela[7]} | {tabela[8]}       7 | 8 | 9 
  """
    print(board)


def ruch(numerPola):
    try:
        numerPola = int(numerPola)
    except:
        return "Nie podano liczby"
    numerPola = int(numerPola)
    numerPola -= 1
    print(numerPola)
    if 0 <= numerPola <= 8:
        if numerPola in wybraneLiczby:
            return f'Na tym miejscu już stoi {tabela[numerPola]}'

        wybraneLiczby.append(numerPola)
        return numerPola
    return 'Podano liczbę z poza zakresu'


def ruchGracza():
    while True:
        x = input("Podaj liczbę z zakresu od 1 do 9:")
        y = ruch(x)
        if type(y) != int:
            print(y)
            continue
        if 0 <= y <= 8:
            return y


def ruchKomputera():
    while True:
        x = random.randint(1, 9)
        y = ruch(x)
        if type(y) != int:
            continue
        if 0 <= y <= 8:
            return y


def wynik(tabela):
    if tabela[0] == tabela[1] == tabela[2] == 'X' or tabela[1] == tabela[4] == tabela[7] == 'X' or tabela[0] == \
            tabela[4] == tabela[8] == 'X' or tabela[2] == tabela[5] == tabela[8] == 'X' or tabela[3] == tabela[4] == \
            tabela[5] == 'X' or tabela[2] == tabela[4] == tabela[6] == 'X' or tabela[6] == tabela[7] == tabela[8] == \
            'X' or tabela[0] == tabela[3] == tabela[6] == 'X':
        input('Gracz 1 (X) wygrał! Wciśnij dowolny przycisk aby zakończyć')
        quit()

    elif tabela[0] == tabela[1] == tabela[2] == 'O' or tabela[1] == tabela[4] == tabela[7] == 'O' or tabela[0] == \
            tabela[4] == tabela[8] == 'O' or tabela[2] == tabela[5] == tabela[8] == 'O' or tabela[3] == tabela[4] == \
            tabela[5] == 'O' or tabela[2] == tabela[4] == tabela[6] == 'O' or tabela[6] == tabela[7] == tabela[8] == \
            'O' or tabela[0] == tabela[3] == tabela[6] == 'O':
        input('Gracz 2 (O) wygrał! Wciśnij dowolny przycisk aby zakończyć')
        quit()
    else:
        return


def startGry():
    print("Kółko i krzyżyk")
    while True:
        wybor = input("Wybierz 1 jeśli chcesz być pierwszy lub 2 jeśli drugi:")
        try:
            wybor = int(wybor)
        except:
            print("Nie podano liczby")
            continue
        if wybor != 1 and wybor != 2:
            print("Podana liczba to nie 1 ani 2")
        else:
            break
    print("Gracz 1 - X")
    print("Gracz 2 - O")
    plansza(tabela)
    for i in range(0, 9):
        if i % 2 == wybor - 1:
            index = ruchGracza()
            tabela[index] = 'X'
        else:
            index = ruchKomputera()
            tabela[index] = 'O'
        os.system('cls')
        plansza(tabela)
        wynik(tabela)

    input("Remis! Wciśnij dowolny przycisk aby zakończyć")
    quit()


startGry()
