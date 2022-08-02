#crie um programa que leia nome e duas notas e armazene tudo em uma lista composta, então mostre o nome e a média de cada aluno cadastrado, permita também mostrar as notas de cada aluno individualmente.

ficha = list() #lista onde será inserido o boletim de cada aluno, sendo essa uma lista com nome, uma lista com duas notas e a média.
#ficha = [[nome, [nota1, nota2], média],[nome, [nota1, nota2], media],[nome, [nota1, nota2], media]] exemplo de três alunos cadastrados.

while True:
    
    nome = input('Nome: ')
    nota1 = float(input('nota1: '))
    nota2 = float(input('Nota2: '))
    media = ((nota1 + nota2) / 2)

    ficha.append([nome, [nota1, nota2], media])
    cont = input('Deseja continuar: ')[0].upper()
    #------ Validação de dado para continuar
    if cont not in 'NS':
        cont = input('Deseja continuar: ')[0].upper()
    if cont == 'N':
        break
    #-----

print('-=' * 30)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')#nome dos campos com formatação

for i, a in enumerate(ficha): #para cada boletim na ficha...
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # É printado o índice, nome do aluno e sua média. Os valores estão formatados.

#parte que mostra as duas notas do aluno, caso seja pedido
while True:

    print('_' * 35)
    
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc ==  999:
        break
    if opc < len(ficha): #antes: <= len(ficha) - 1
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
