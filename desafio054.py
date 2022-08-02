#Crie um programa que peça a idade de 5 pessoas e no final printa quantas pessoas são maiores de idade e menores de idade.
from datetime import date
ano = date.today().year
print(ano)

maiores = 0
menores = 0

for c in range(5):
    nascimento = int(input('Digite sua data de nascimento: '))
    idade = ano - nascimento
    if idade <= 18:
     menores += 1
    else:
     maiores += 1
    
print('Há {} menores de idade'.format(menores))
print('Há {} maiores de idade'.format(maiores))

