print('GERADOR DE PA')
print('=-' * 10)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
termo = a1
count = 1
while count <= 10:
    print('{} → '.format(termo), end='')
    termo = termo + r
    count = count + 1
print('FIM!')
