def voto(nascimento):
    from datetime import date
    atual =date.today().year
    idade = atual - nascimento
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: voto obrigatório'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))