#Crie um programa que peça números inteiros e no final mostre a média dos valores lidos, o menor e o maior valor.
def ler():
    numeros = []
    while True:
        n = int(input('Digite um número: '))
        numeros.append(n)
        continuar = input('Deseja continuar(S/N): ')[0].upper() == "S"
        if continuar:
            pass
        else:
            break
    print('=-' * 20)
    print('A média entre os valores é', sum(numeros) / len(numeros) )
    print('O maior valor lido foi', max(numeros))
    print('O menor valor lido foi', min(numeros))

def main():
    ler()
if __name__ == "__main__":
    main()