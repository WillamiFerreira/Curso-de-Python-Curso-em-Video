#Crie um jogo de Jokenpo onde o usuário joga com a máquina, e no final mostre a escolha do user e da máquina e quem venceu.
from random import randint #importando a função randint do modulo random
from time import sleep #iportando a função sleep do módulo time.
itens = ('pedra', 'Papel', 'Tesoura') #tupla com as opções possíveis
computador = randint(0, 2) #usando a função randint para fazer a escolha do computador, entre 0 e 2 que corresponde aos itens da tupla 'itens'.
jogador = int(input('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
'''))#O jogador escolhe um número para fazer a sua jogada.
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.7)
print('=-' * 11)
#vizualização dos resultados
print('O computador jogou',itens[computador])
print('O jogador jogou',itens[jogador])
print('=-' * 11)

#estrutura condicional com if, elif e else para determinar corretamente quem venceu ou se foi empate.
if computador == 0: #Se o computador escolheu 0(pedra), há três combinações possíveis, que são...
    if jogador == 0:#O jogador também ter escolhido 0(pedra)...
        print('EMPATE')#printado um "EMPATE"

    elif jogador == 1:#O Jogador ter escolhido 1(papel)
        print('JOGADOR VENCE')#então o jogador vence

    elif jogador == 2:#O jogador ter escolhido 2(tesoura)
        print('COMPUTADOR VENCE')#então o computador vence
    else:#Esse else é usado quando o jogador não escolhe nem 0, 1 ou 2
        print('JOGADA INVÁLIDA')
 #essa mesma ideia se repete para caso computador escolha 1(papel) ou 2(tesoura)
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')