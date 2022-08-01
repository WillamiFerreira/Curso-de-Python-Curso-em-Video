#crie um programa que leia a idade de um acleta e o classifique baseado em sua idade
# mirim - 9 ou menos
# infantil - 14 ou menos
# junior - 19 ou menos
# sênior - 25 ou menos
# master mais de 25
from datetime import date#importando a função date do módulo datetime
ano_atual = date.today().year #pegando o ano atual do sistema.
nascimento = int(input('Qual é o seu ano de nascimento? '))#pedindo o ano de nascimento
idade = ano_atual - nascimento #subtraindo a idade do ano de nascimento para saber a idade.
#sistema de if, elif e else para fazer a correta classficação baseada na idade.
if idade <=9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')