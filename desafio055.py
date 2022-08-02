#Crie um programa que lê o peso de 5 pessoas e depois printa o maior e o menor preço.
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
        
print('O maior peso lido foi o de {} kilos'.format(maior))
print('O menor peso lido foi o de {} kilos'.format(menor))

    