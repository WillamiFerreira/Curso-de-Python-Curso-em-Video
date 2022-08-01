#faça um programa que leia nome e a média de um aluno, guardando também a situação do aluno (Reprovado, Recuperação ou  Aprovado) em um dicionário. No fim, mostre o conteúdo da estrutura da tela.
aluno = dict()#criando dicionário vazio
aluno['Nome'] = input('Nome: ') #adicionando chave "Nome" e um valor para a chave, que será o nome do aluno
aluno['Média'] = float(input('Média: ')) #adicionando chave "Média" e um valor para a chave que será a média do aluno
#usando a estrutura condicinal if, elif e else, defino qual será o valor para a chave 'Situação' que dependerá de média do aluno.
if aluno['Média'] >= 7: 
    aluno['Situação'] = 'Aprovado'
elif 5<= aluno['Média'] <7:
    aluno['Situação'] = 'Recuparação'
else:
    aluno['Situação'] = "Reprovado"

print('=-' * 30)
for k, v in aluno.items(): #usando o método .item(), extraio a chave e o seu valor podendo printa-los em uma f-string. Uso a estrutura for, pois há várias chaves no dicionário e cada uma(com seu valor) será printada em um laço.
    print(f'{k} é igual a {v}')