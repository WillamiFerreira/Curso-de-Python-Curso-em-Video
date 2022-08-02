#Crie um programa que lê números e no final mostra a soma de todos os valores menos de 999 que serve para encerrar o programa.
def main():
    soma = cont = 0
    while True:
        n = int(input("Digite um número (999) para parar: "))
        if n == 999:
            break
        else:
            soma += n
            cont += 1
    print(f'A soma dos {cont} valores foi {soma}')
        
if __name__ == "__main__":
	main()