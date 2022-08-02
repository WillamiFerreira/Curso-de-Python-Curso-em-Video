#Crie um programa que peça 5 números e mostre:
# A lista
# O maior valor e a sua posição 
# O menor valor e a sua posição
from operator import index
def main():
    numeros = []
    for _ in range(5):
        numeros.append(int(input('Digite um número: ')))

    
    maxv= max(numeros)
    minv= min(numeros)
    maxc = numeros.index(maxv)
    minc = numeros.index(minv)

    print('=-' * 20)
    print(f'você digitou os valores {numeros}')
    print(f'O maior valor é {maxv} e está na posição {maxc}')
    print(f'O menor valor é {minv} e está na posição {minc}')
        
if __name__ == "__main__":
    main()