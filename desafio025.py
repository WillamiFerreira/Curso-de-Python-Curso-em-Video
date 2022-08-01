#crie um programa que pede seu nome completo e verifica se há o nome silva no nome.
nome = input('Qual é o seu nome completo? ').strip()#pede o nome e retira os espaços vazios no final e começo
print('{}'.format('SILVA' in nome.upper()))#verifica se há a string "SILVA" dentro da string nome.upper().