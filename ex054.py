from datetime import date
cont = 0
contmi = 0
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade =atual - nasc
    if idade >= 21:
        cont = cont + 1
    else:
        contmi = contmi + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('Ao todo tivemos {} pessoas menores de idade'.format(contmi))

