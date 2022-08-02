#Crie um programa que peça nome, ano de nascimento e carteira de trabalho, armazene essas informações em um dicionário e depois informe. Caso não tenha carteira de trabalho o valor é 0
from datetime import * 

dataatual = datetime.now()
data = dataatual.date()
ano = int(data.strftime("%Y"))

d = dict()
d['nome'] = input('Nome:')
nascimento = int(input('Ano de Nascimento: '))
d['idade'] = ano - nascimento
d['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if d['ctps'] != 0:
    d['contratacao'] = int(input('Ano de Contratação: '))
    d['salario'] = int(input('Salário: R$'))
    d['aposentadoria'] = (d['contratacao'] - nascimento) + 35

print('=-' * 25)
for k, v in d.items():
    print(f' - {k} tem valor {v}')
print()