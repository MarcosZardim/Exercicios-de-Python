lista = []
while True:
    num = int(input('Digite um valor : '))
    lista.append(num)
    continuar = input('Quer continuar? [S/N] ').lower()[0].strip()
    while continuar not in 'ns':
        continuar = str(input('Quer continuar ? [S/N] ')).lower()[0].strip()
    if continuar not in 's':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem descrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')
    