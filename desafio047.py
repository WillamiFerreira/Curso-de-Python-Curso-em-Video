#criar um programa que mostra todos os números pares de 1 até 50
for c in range(2, 51, 2):#criar uma repetição for que começa do 2, pois ele é o primeiro par da sequência, até o 51, pois o último é ignorado então 51 para ir até o 50. E pulando de 2 em 2 passar somente pelos pares.
    print(c, end=' ')#printa o valor atual de "c" e com o valor do parâmetro 'end' sendo uma string vazia para não quebrar linha.
print('ACABOU') #ao final do laço é printado esse mensagem.