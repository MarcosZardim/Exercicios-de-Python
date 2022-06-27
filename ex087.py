matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
maiorv = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {pares}')
tcol = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {tcol}') #poderia ter usado sum de somar
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    maior = matriz[1][0]
if matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
        maior = matriz[1][1]
if matriz[1][2] > matriz[1][1] and matriz[1][2] > matriz[1][0]:
    maior = matriz[1][2]
print(f'O maior valor da segunda linha é {maior}') #poderia ter usado o método max em matriz[1]