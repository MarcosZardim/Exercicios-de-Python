def área():
    larg = float(input('Largura (m): '))
    comp = float(input('Comprimento (m): '))
    mult = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {mult}m²')


print('Controle de Terrenos')
print('-' * 30)
área()

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')


#Programa principal
print('Controle de Terrenos')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)