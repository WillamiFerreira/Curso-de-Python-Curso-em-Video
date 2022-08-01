#Escreva um programa que pede uma frase e:
#a) O total de letras a
#b) A posição da primeira letra a
#c) A posição da última letra a
frase = input('Digite uma frase: ').strip().upper()#pede uma frase e retira todos os todos espaços vazios com strip e deixa toda a frase em caixa alta.
print('A frase tem {} letras a'.format(frase.count('A')))#usa o método count() para contar a quantidade de letras 'a'.
print('A primeira letra a está na posição {}'.format(frase.find('A')+1))#usa o método find() para encontra a ocorrencia do primeiro a
print('A última letra a está na posição {}'.format(frase.rfind('A')+1))#usando o método rfind() para encontrar a primeira ocorrencia do a, porém começando do final da frase.