from time import sleep
def sistema(bibfunction):
    print('\033[1;107m')
    return help(bibfunction)


def ajuda(msg):
    print('\033[1;42m~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))
    print('\033[0;0m', end='')


def acessando(msg):
    print('\033[1;44m~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print('\033[0;0m', end='')

while True:
    ajuda('Sistema de ajuda Pyhelp')
    funcaobib = input('Função ou Biblioteca > ').strip().lower()
    if funcaobib == 'fim':
        print('\033[1;41m~' * (len('Até Logo') + 4))
        print('  Até Logo')
        print('~' * (len('Até Logo') + 4))
        print('\033[m')
        break
    acessando(f'Acessando o manual do comando {funcaobib}')
    sleep(1)
    sistema(funcaobib)
