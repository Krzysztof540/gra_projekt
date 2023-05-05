import random

tabela = []

for i in range(9):
    tabela.append(' ')


def plansza (tabela):
    board = f"""
   {tabela[0]} | {tabela[1]} | {tabela[2]}       1 | 2 | 3  
  ---|---|---     ---|---|---
   {tabela[3]} | {tabela[4]} | {tabela[5]}       4 | 5 | 6 
  ---|---|---     ---|---|---
   {tabela[6]} | {tabela[7]} | {tabela[8]}       7 | 8 | 9 
  """
    print(board)


index_list = []


def ruch(numerPola):
    while True:
        numerPola -= 1
        if 0 <= numerPola <= 8:
            if numerPola in index_list:
                print(f'Na tym miejscu już stoi {tabela[numerPola]}')
                continue
            index_list.append(numerPola)
            return numerPola
        print('Podano liczbę z poza zakresu')

def ruchGracza():
    x = int(input("Podaj liczbę z zakresu od 1 do 9:"))
    ruch(x)

def ruchKomputera():
    x = random.randint(0,9)
    ruch(x)
