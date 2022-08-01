nome = str(input('Digite seu nome completo: '))
nomes = nome.split()#o método splite conta a string que está em 'nome' em vários pedaços. Um novo pedaço é feito a cada espaço em branco da string. Os pedaços são armazenados em uma lista.
print('Seu primeiro nome é',nomes[0])#printa o primeiro item da lista, que corresponde ao primeiro nome. Para isso é usado o índice 0.
print('Seu último nome é',nomes[-1])#printa o último item da lista, que corresponde ao último nome. Para isso é usado o índice -1, que corresponde ao último item de uma lista ou tupla.
