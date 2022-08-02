#Crie um programa que lê números e no final mostre a soma dos números e quantos números foram digitados.
#Digitar 999 termina
def main():
    soma = 0
    cont = 0
    while True:
        n = int(input('Digite um número: [999 para] '))
        soma += n
        cont += 1
        if n == 999:
            break
    print('A soma dos números lidos é ', soma)
    print('A quantidade de numero lidos foi ', cont)
if __name__ == "__main__":
    main()