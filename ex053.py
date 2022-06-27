txt = input('Digite uma frase: ').strip().upper().replace(' ', '')
txti = txt[::-1]
print('O inverso de {} é {}'.format(txt, txti))
if txt == txti:
    print('Temos um Palídromo')
else:
    print('A frase digitada não é um palídromo')

