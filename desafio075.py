#Crie um programa que leia 4 números e no final mostre:
# Quantas vezes o número nove apareceu
# Se há o valor 3 na tupla
# Quantos valores pares foram digitados
from itertools import count
from operator import index


def valor9(va):
    print(f'O número 9 apareceu {va.count(9)} vezes')

def valor3(va):
    if 3 in va:
        print(f'O valor 3 apareceu na {va.index(3) + 1}º posição')
    else:
        print('Não há valor 3 na tupla')

def pares(va):
    pares = 0
    for valor in va:
        if valor % 2 == 0:
            pares += 1
    print('Os valores pares digitados foram', pares)
        
def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    n3 = int(input('Digite mais um número: '))
    n4 = int(input('Digite o último número: '))
    valores = (n1, n2, n3, n4)

    #Uma outra forma de criar uma tupla é adicionar os inputs diretamente dentro da tupla, assim não é preciso nem mesmo criar uma variável para cada input, pois ela já é criada dentro da tupla.
    '''valores = (
        int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: '))
    )'''
    print('Você digitou os valores ', valores)
    valor9(valores)
    valor3(valores)
    pares(valores)
if __name__ == "__main__":
    main()