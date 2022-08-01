#crie um jogo de adivinhação, onde o usuário e computador escolher um número aleatório entre 0 e 5, se ambos escolherem o mesmo número, então jogador vence.
import random
lista = [0, 1, 2, 3, 4, 5]
selecionado = random.choice(lista)#Utiliza a função choice() para escolher um número aleatóriamente da lista de números.
n_user = int(input('Escolha um número de 0 a 5: '))#pede um número ao usuário
if n_user == selecionado:#usando if para comparar o número escolhido pelo usuário com o escolhido do computador.
    print('Parabéns, você acertou o número!')#esse é a mensagem printada se o os valores forem iguais.
else:
    print('Você errou! a máquina venceu! ')#Esse mensagem aparecerá se os valorem não forem iguais.

print(f'O número selecionado foi {selecionado}!')