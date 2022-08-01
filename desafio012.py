#crie um programa que lê um valor real de um produto e calcula o seu valor com 5% de desconto.
sem_desconto = float(input('O preço sem desconto: R$'))#Lê o valor e armazena na variável.
com_desconto =  sem_desconto * 0.95 #Multiplica por 0.95 para calcular o valor comm 5% de desconto
print('O valor do produto com desconto é R${:.2f}'.format(com_desconto))#printa o novo valor em uma f-string.

