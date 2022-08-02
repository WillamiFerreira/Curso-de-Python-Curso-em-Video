#Crie um programa que le um número e retorna sua forma por extenço.
def main():
    #tupla com números por extenso
    numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito","dezenove", "vinte")
    #repitiçao while com teste lógico no fim
    while True:
        # um valor inteiro é pedido
        n = int(input('Digite um número de 0 a 20: '))
        # se esse valor estiver entre 0 e 20 o ciclo é encerrado. Se o valor não estiver nesse intervalo, então é pedido um número novamente.
        if 0 <= n <=20:
            print(f'Você digitou o número {numeros[n]}')
            continuar = input('deseja continuar? ')[0].upper()
            if continuar == 'N':
                break
        print('tente novamente.', end=' ')
    #quando a loop é encerrado é printado o elemento correspondente ao valor lido, usando esse como índice para para encontrar aquele.
    
if __name__ == "__main__":
    main()

