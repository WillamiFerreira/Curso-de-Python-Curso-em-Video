#Crie um programa que tenha uma função chamada voto() que vai receber com parâmetro o ano de nascimento de pessoa retornando um valor literal indicando se uma pessoa tem voto NEGADO , OPCIONSL ou OBRIGATÓRIO nas eleições.
from datetime import datetime
def voto(nasc):
    ano = datetime.now().year
    if ano - nasc > 18 and ano - nasc < 70 :
        return 'VOTO OBRIGATÓRIO'
    elif ano - nasc >= 70:
        return 'VOTO NÃO OBRIGATÓRIO'
    else:
        return 'NÃO VOTA'
print('')
nasc = (int(input('Em que ano você nasceu? ')))
resul = voto(nasc)
idade = datetime.now().year - nasc
print(f'com {idade} anos: {resul}')