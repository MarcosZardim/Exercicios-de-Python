dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']


filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
locadora = [filme]
locadora.append(filme)
print(locadora[:])


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
pessoas['nome'] = 'Leandro'
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')


estado = dict()
brasil = list()
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
