#Crei um programa que peça o sexo de uma pessoa, mas somente se for M ou F, caso não seja, o sexo é pedido novamennte.
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informa seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))