#criar um programa que ler quatro nomes de alunos, os adiciona em uma lista e printa de forma embaralhada.
from random import shuffle #importa a função shuffle do módulo random
#cada variável pede o nome de um aluno
n1 = input('Primeiro Aluno: ') 
n2 = input('Segundo ALuno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto ALuno: ')
lista = [n1, n2, n3, n4] #a lista é criada
shuffle(lista) #a lista é adicionada como parâmetro da função shuffle e embaralhada
print('A ordem de apresentação será:', lista) #a lista agora embaralhada é imprimida com uma formatação.