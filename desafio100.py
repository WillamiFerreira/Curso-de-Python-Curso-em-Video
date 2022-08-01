#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia(), e somapar(). A primeria função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. 
from random import randint #importo a função randint do módulo random.
from time import sleep #importo a funçao sleep do módulo time.

def sorteia(l):
    print('Sorteando 5 valores da lista:', end=' ')
    for n in range(0, 5): #para cada número entre 0 e 4...
        b = randint(1, 10) #é sorteado um valor aleatório entre 1 e 10 e armazenado em 'b'.
        l.append(b) #então esse valor aletório é adicionado na lista com o método append()
        print(b, end = ' ', flush=True)#esse valor é printado, sem quebrar linha (end=' ') e sem armazenar os dados em buffer(flush= True)
        sleep(0.5) # dá um tempo de 0.5s entre cada número para aperecer na tela.
    print('PRONTO!')

def somapar(l):
    soma = 0 #recebe as somas dos números pares da lista.
    for n in l: #estrutura for, em que cada laço passa por um item da lista
        if n % 2 == 0: #se esse item for par...
            soma += n #então seu valor é somado ao valor da variável soma.
    print(f'A soma dos valores pares é {soma}.') #quando todos os item da lista forem verificados, a repetição acaba e é printado o resultado em uma f-string.

numeros = list() #cria a lista vázia.
sorteia(numeros) #chama a função 'sorteia' levando como parâmetro a lista vazia.
somapar(numeros) #chama a função 'somapar' agora preenchida com os números sorteados.
