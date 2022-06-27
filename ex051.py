print('='*15)
print('10 TERMOS DE UMA PA')
print('='*15)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
an = a1 + (10 - 1) * r
for c in range(a1, an + r, r):
    print('{}'.format(c), end='→')
print('ACABOU')
