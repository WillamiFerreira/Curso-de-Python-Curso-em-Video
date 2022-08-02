#Crie um programa crie uma progreção aritimética de 10 números. O programa pede o número inicial e a razão. Utilize um estrutura de repetição
def progressao(i, r):
    decimo = i + 9 * r
    for c in range(i, decimo + r, r):
        print(c, end=' ')
    print('Acabou')
    

def main():
    inicio = int(input('Digite um número inteiro qualquer que será o inicio: '))
    razao = int(input('Digite o número que será a razão: '))
    progressao(inicio, razao)
if __name__ == "__main__":
    main()