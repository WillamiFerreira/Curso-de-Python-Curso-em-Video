#Crie um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar em dicionário com as seguintes informações:
# Quantidade de notas;
# A maior nota;
# A menor nota;
# A média da turma;
# A situação também as docstrings
#Adicione 
def notas(*n, sit=False):
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = round((sum(n))/ dados['total'], 2)
    if sit == False:
        return dados
    else:
        if dados['média']<=5:
            dados['situação'] = 'RUIM'
            return dados
        elif 5< dados['média']<=6:
            dados['situação'] = 'RAZOÁVEL'
            return dados
        else:
            dados['situação'] = 'BOA'
            return dados

resp = notas(4.5, 6, 9.7, 5.5, sit=True)
print(resp)