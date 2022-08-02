#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando tudo em um dicionário e os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. NO final, mostre:
#Quantas pessoas cadastradas;
#A média de idade;
#Uma lista com mulheres
#Uma lista com idade acima da média.
pessoas = list()
temp = dict()
idades = list()
mulheres = list()
while True:
    temp['Nome'] = input('Nome: ')
    temp['Sexo'] = input('Sexo: [M/F]')[0].upper().strip()
    while temp['Sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        temp['Sexo'] = input('Sexo [M/F]: ')[0].upper().strip()
    if temp['Sexo'] == 'F':
        mulheres.append(temp['Nome'])
    idade = int(input('Idade: '))
    temp['idade'] = idade
    idades.append(idade)
    pessoas.append(temp.copy())
    continuar = input('Deseja continuar? ')[0].upper().strip()
    if continuar == 'N':
        break
print('=-' * 20)
media_idade = (sum(idades) / len(idades))
print(f'A) Ao todo foram {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end=' ')
for m in mulheres:
    print(f'{m}',end=' ')
print( )
print('D) Lista de pessoas que estão acima da média: ')
for n in pessoas:
    if n['idade'] > media_idade:
        print(f'    Nome = {n["Nome"]}; sexo = {n["Sexo"]}; idade = {n["idade"]};')
print('<<ENCERRADO>>')