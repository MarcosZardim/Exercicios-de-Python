dados = {}
lista = []
total = 0
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
dados['Gols'] = lista[:]
for c in lista:
    total = total + c #poderia ser feito com sum()
dados['Total'] = total
print('=-' * 30)
print(dados)
print('=-' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for c, i in enumerate(lista):
    print(f'   => Na partida {c}, fez {i} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
