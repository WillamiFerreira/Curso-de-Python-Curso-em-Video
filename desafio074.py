#Crie um progrma  que sorteia 5 números aleatórios entre 1 e 100, no fim mostre o maior e o menor lido.
from random import *
def main():
    numeros = (randint(0, 101), randint(0, 101), randint(0, 101), randint(0, 101), randint(0, 101) )
    print('Os valores sorteados foram:', end=' ')
    for numero in numeros:
        print(f'{numero}', end=' ')
    print('\nO maior valor sorteado foi', max(numeros)) #Usando \n para pular para a linha de baixo
    print('O menor valor sorteado foi', min(numeros))
        

if __name__ == "__main__":
    main()