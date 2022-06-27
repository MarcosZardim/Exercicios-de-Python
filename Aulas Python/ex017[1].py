lanche = [1, 2, 3, 4]
lanche.remove(3)
lanche.pop()
del lanche[3]
print(lanche)
lanche.sort()
lanche.sort(reverse=True)
len(lanche)
lanche.append(7)
lanche.insert(2, 0)
lanche.clear()


valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

valores.append(5)
valores.append(9)
valores.append(4)
for c ,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a   # b = a[:] jeito de copiar uma lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
