lista = []
listafim = []
maior = 0
menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso:')))
    if len(listafim) == 0:
        maior = lista[1]
        menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    listafim.append(lista[:])
    lista.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('=-' * 30)
print(f'Ao todo você cadastrou {len(listafim)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in listafim:
    if p[1] == maior:
        print(f'[{p[0]} ]', end='')
print()
print(f'O menor peso foi de {menor}. Peso de ', end='')
for p in listafim:
    if p[1] == menor:
        print(f'[{p[0]} ]', end='')
print()
