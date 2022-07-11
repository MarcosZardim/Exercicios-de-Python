from random import randint
from time import sleep


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista:', end='')
    for i in lista:
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    spar = 0
    for c in lista:
        if c % 2 == 0:
            spar = spar + c
    print(f'Somando os valores pares de {lista}, temos {spar}')

números = list()
sorteia(números)
somapar(números)
