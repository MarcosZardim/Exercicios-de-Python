def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor.
    :param b: O segundo valor.
    :param c: O terceiro valor.
    """
    s = a + b + c
    #print(f'A soma vale {s}', end='\n')
    return s


r1 = somar(b=4, c=2)

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c 
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')