#Crie um programa que pergunte quantos jogos o usuário deseja, e faça-o gerar o jogos pedidos, sendo eles conjuntos de 6 números aleatórios que nãoo se repetem
from random import randint
from time import sleep
print('=-'* 30)
print('JOGA NA MEGA SENA')
print('=-'* 30)

#criação das listas vazias
lista = list() # lista temporária, é nela que vai cada jogo, que será copiada para a jogos e depois apagada
jogos = list() # lista compostas onde estará cada jogo.
quant = int(input('Quantos jogos você deseja? ')) 
for jogo in range(quant):
    #parte que criar uma lista com 6 números aleatórios diferentes--------
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    # ---------------------
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    # parte que ordena os números de cad jogo a adiciona em uma lista maior, a jogos ------------
    # parte de apresentação dos resultados ------------
print('=-' * 3, 'Gerando jogos', '=-' * 3)
for i, jogo in enumerate (jogos):
    print(f'{i + 1}º jogo: {jogo}')
    sleep(1)
print('=-=' * 3,'BOA SORTE', '=-=' * 3)