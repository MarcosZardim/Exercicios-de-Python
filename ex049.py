num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for c in range(0, 10):
    print('{} x {:2} = {}'.format(num, c, num*c))
