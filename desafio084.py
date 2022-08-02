#faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. e no final mostre quantas pessoas foram cadastradas, umas listagem das mais pesadas e uma listagem das mais leves.

princ = list()
temp = list()
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    conti = input('Continuar?: [S/N] ')[0].upper().strip()
    #-------
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1]< menor:
            menor = temp[1]
    #-------
    princ.append(temp[:])
    temp.clear()
    if conti not in 'NS':
         conti = input('Continuar?: [S/N] ')[0].upper().strip()
    if conti == 'N':
        break
print('=-' * 20)
print(f'Você registrou {len(princ)} pessoas.')
print(f'O maior peso é de {maior}Kg. Peso de', end = ' ')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end = ' ')
print()
print(f'O menor peso foi de {menor}Kg. O peso de', end =' ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end = ' ')
