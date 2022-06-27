maior = 0
menor = 0
cont = 0
média = 0
soma = 0
continuar = 'sS'
while continuar in 'sS':
    num = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N] ')
    cont = cont + 1
    soma = soma + num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
