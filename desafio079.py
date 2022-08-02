#Crie um programa que peça números e os armazene em uma lista, no fim mostre a lista em ordem crescente.
def main():
    numeros = []
    while True:
        n = int(input('Digite um número: '))
        if n not in numeros:
            numeros.append(n)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado! não vou adicionar...')

        continuar = input('Deseja continuar: [S/N]: ')[0].upper()
        while continuar not in 'NS':
            continuar = input('Tente novamente: ')[0].upper()

        if continuar == 'N':
            break
    numeros.sort()
    print('=-' * 20)
    print('Você digitou os valores ',numeros)
if __name__ == '__main__':
    main()