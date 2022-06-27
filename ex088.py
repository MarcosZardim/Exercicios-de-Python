from random import randint
from time import sleep
print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
cont = 0
outer = 0
alea = 0
for c in range(jogos):
    lista.append([])
    cont = jogos
for a in lista:
    cont = cont - 1
    for l in range(0, 6):
        alea = randint(1, 60)
        if alea in lista[cont]:
            alea = randint(1, 60)
        else:
            lista[cont].append(alea)
print(f'=-=-=-  SORTEANDO {jogos} JOGOS  -=-=-=')
lista[cont].sort()
for u in lista:
    lista[outer].sort()
    outer = outer + 1
    print(f'jogo {outer} {lista[outer-1]}')
    sleep(1)
print('=-=-=-=-=- < BOA SORTE! > -=-=-=-=-=')