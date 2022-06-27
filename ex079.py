lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar ? [S/N] ')).lower()[0].strip()
    while continuar not in 'ns':
        continuar = str(input('Quer continuar ? [S/N] ')).lower()[0].strip()
    if continuar not in 's':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

