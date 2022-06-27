print('GERADOR DE PA')
print('=-' * 10)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
termo = a1
count = 1
onze = 11
while count < onze:
    print('{} → '.format(termo), end='',)
    termo = termo + r
    count = count + 1
    if count == onze:
        print('Pausa')
        tmais = int (input('Quantos termos você quer mostrar a mais? '))
        onze = onze + tmais
print('Progressão finalizada com {} termos mostrados'.format(onze - 1))