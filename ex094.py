lista = []
pessoa = {}
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    media = media + pessoa['idade']
    lista.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print('=-' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = media / len(lista)
print(f'B) A média de idade é de {media:5.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print(f'    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
