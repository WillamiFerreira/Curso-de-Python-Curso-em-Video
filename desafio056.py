#crie um programa leia nome, idade e sexo de 4 pessoas e depois printe
# A idade média de todos
# A soma de todas as idades
# A maior idade entre os homens
# O nome doo mais velho
# Quantas mulheres tem mais de 20 anos
mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('-----{}ª PESSOA-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
    
mediaidade = somaidade / 4
print('A média das idades é '.format(mediaidade))
print('O nome do homem mais velho é {} e sua idade é de {}'.format(nomevelho, maioridadehomem))
print('O total de mulheres menores de 20 anos é {}'.format(totalmulher20))
