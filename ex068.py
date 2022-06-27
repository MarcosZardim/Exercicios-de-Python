from random import randint
count = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    n = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar? ').upper().strip()
    computador = randint(0, 10)
    soma = n + computador
    if soma % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'ÍMPAR'
    print('-'*30)
    print(f'Você jogou {n} e o computador jogou {computador}. Total de {n + computador} DEU {pi}!')
    print('-' * 30)
    if escolha == pi:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
        count = count + 1
    else:
        print('Você PERDEU!')
        print('=-'*15)
        break
print(f'GAME OVER! Você venceu {count} vezes.')
