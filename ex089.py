ficha =[]
while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]')).strip().lower()
    if continuar == 'n':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    mnotas = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if mnotas == 999:
        print('FINALIZANDO...')
        break
    if mnotas <= len(ficha) - 1:
        print(f'Notas de {ficha[mnotas][0]} são {ficha[mnotas][1]}')
