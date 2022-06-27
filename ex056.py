media = 0
hvelho = 0
contm = 0
nomevelho = ''
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ').strip())
    if p == 1 and sexo in 'Mm':
        hvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > hvelho:
        hvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contm = contm + 1
    media = media + idade
media = media / p
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} e se chama {}.'.format(hvelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contm))
