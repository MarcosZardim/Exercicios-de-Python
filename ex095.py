time = list()
jogador = dict()
lista = []
while True:
    jogador.clear()
    lista.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        lista.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
    time.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print('=-' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! não existe jogador com código {busca}')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for n, i in enumerate(time[busca]['gols']):
            print(f'No jogo {n + 1} fez {i} gols.')
        print('-' * 40)
