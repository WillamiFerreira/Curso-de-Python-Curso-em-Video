#Crie um programa que recebe um valor e retorna com 15% de aumento.
sem_desconto = com_desconto = float(input('O salário sem desconto em reais é: '))#Cria duas variáveis que recevem o mesmo valor, o salário sem desconto.
com_desconto += (sem_desconto * 0.15)#é somado à variável "com_desconto" o resultado de 15% do salário sem desconto.
print('O salário com 15% de aumento é: {:.2f} Reais'.format(com_desconto))#print com o resultado.