maiores = 0
homens = 0
mulheres = 0
while True:
    print('_'*20)
    print('CADASTRE UMA PESSOA')
    print('_'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').strip().upper())
    print('_'*20)
    continuar = str(input('Quer continuar? [S/N] ').strip().upper())
    if idade > 18:
        maiores = maiores + 1
    if sexo[0] == 'M':
        homens = homens + 1
    if sexo[0] == 'F' and idade < 20:
        mulheres = mulheres + 1
    if continuar[0] == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
