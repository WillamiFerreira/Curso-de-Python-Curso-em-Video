#Crie um programa que lê o nome de quatro alunos e escolha um aleatoriamente.
from random import choice
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4] #adiciona os alunos em uma lista.
escolhido = choice(alunos)#usei a funcionalidade "choice" do módulo random para fazer uma escolha
print('O aluno(a) escolhido foi',escolhido)#printa o escolhido em uma f-string