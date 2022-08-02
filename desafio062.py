#Melhore o desafio 061 com a possibilidade de aumentar o número de elementos na PA
def progressao(i, r):
    decimo = i + 9 * r
    decimoau = decimo
    for c in range(i, decimo + r, r):
        print(c, end=' ')
    continuar = int(input('Deseja adicionar mais quantos termos: '))
    if continuar != 0:
        decimo = decimoau + (continuar - 1) * r
        for c in range(decimoau, decimo + r, r):
            print(c, end=' ')
    else:
        pass

def main():
    inicio = int(input('Digite um número inteiro qualquer que será o inicio: '))
    razao = int(input('Digite o número que será a razão: '))
    progressao(inicio, razao)
    
if __name__ == "__main__":
    main()