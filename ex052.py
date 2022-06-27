count = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1, 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        count = count + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, count))
if count == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')
