#Crie um programa que faça uma contagem regressiva de 10 até 0 e no final printe "FOGOS ESTOURANDO!!!"
from time import sleep#importa a função sleep do módulo time
for c in  range(10, -1, -1): #cria uma repetição de 10 até 0 voltando de 1 em 1
    print(c)#printa os númeross
    sleep(1)#usa a função sleep para esperar um segundo antes do próximo número
print('FOGOS ESTOURANDO!!!')#quando o laço termina, essa mensagem é imprimida