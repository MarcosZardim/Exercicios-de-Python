from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print("""      [ 1 ] somar
      [ 2 ] multiplicar 
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa""")
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
        print('=-=='*12)
    elif opcao == 2:
        multiplicar = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, multiplicar))
        print('=-==' * 12)
    elif opcao == 3:
        if n1 == n2:
            print('Os dois são iguais')
            print('=-==' * 12)
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
            print('=-==' * 12)
        elif n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
            print('=-==' * 12)
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-==' * 12)
    elif opcao == 5:
        print('Finalizando...')
        sair = True
    else:
        print('Opção ínvalida. Tente novamente')
        print('=-==' * 12)
