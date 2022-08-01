nome = str(input('Qual é o seu nome completo? ')).strip() #Pede o nome e armazena na variável nome
print('Seu nome em maiúsculas é',nome.lower())#usa o método .lower para deixar todas as letras em minúsculo.
print('Seu nome em maiúsculas é',nome.upper())#usa o méodo .upper() para deixar todas as letras em maiúsculo.
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' '))) #usando a função len para contar todos os caractéres do nome, e usando a função conunt() para contar todos os espaços vazios e substituir, assim sobra o total de algarismos do nome.
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #usa o método find() para achar a quantidade de alagerismos antes.

