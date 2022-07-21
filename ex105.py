def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :para n : uma ou mais notas dos alunos (aceita várias).
    para sit: valor opcional, indicando se deve ou não adicionar a situação.
    return: Um dicionário com várias informações sobre a situação da turma.  
    """
    aluno = {}
    soma = 0
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    for c in n:
        soma = soma + c
    aluno['média'] = soma / len(n)      #Tem a função sum() para somar
    if sit:
        if 6 <= aluno['média'] < 7:
            aluno['situação'] = 'Razoável'
        elif aluno['média'] >= 7:
            aluno['situação'] = 'Boa'
        else:
            aluno['situação'] = 'Ruim'
    return aluno
    

resp = notas(3.5, 2, 6.5, sit=True)
print(resp)
