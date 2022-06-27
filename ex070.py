print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
cont = 0
soma = 0
menorp= ' '
controle = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    soma = soma + preco
    controle = controle + 1
    if preco > 1000:
        cont = cont + 1
    if controle == 1: # or preco < menor:
        menor = preco
        menorp = produto
    else:
        if preco < menor:
            menor = preco
            menorp = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('------FIM DO PROGRAMA------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorp} que custa R${menor:.2f}')
