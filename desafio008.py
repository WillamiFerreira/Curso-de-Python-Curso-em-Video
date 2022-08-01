#Faça um programa que leia um valor em metros e converte para centimetros e milímetros.
valor_metros = int(input('Valor em metro:'))#recebe o valor em metros
valor_centimetros = valor_metros * 100 #multiplica o valor em metros lido, converte para centímetros e armazena em uma variável.
valor_milimetros = valor_metros * 1000 #multiplica o valor em metros lido, converte para milímetros e armazena em uma variável.
print('O Valor {} em centimetros é {} cm e em milímetros é {} mn'.format(valor_metros, valor_centimetros, valor_milimetros)) #printa todas as variáveis em uma f-string.