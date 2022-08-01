#Crie um programa que le um número de 0 a 9999 e retorna as unidades, dezenas, centenas e milhares.
numero = int(input('Digite um número de 0 a 9999: '))

print('Unidade:', numero // 1 % 10)
print('Dezena:', numero // 10 % 10)
print('Centena:', numero // 100 % 10)
print('Milhar:', numero // 1000 % 10)