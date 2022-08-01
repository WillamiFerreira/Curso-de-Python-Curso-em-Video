#O CÓDIGO CONVERTE UM NÚMERO DECIMAL PARA AS BASES BINÁRIA, OCTAL OU HEXADECIMAL.

def conversor(numero, base):
    if base == 1:
        print (f'O número {numero} convertido para binário é {numero:b}')# converte para binário
    elif base == 2:
        print('O número {} em octal fica {}'.format(numero, oct(numero)))#converte para octal 
    else:
        base == 3
        print(f'{numero} convertido para hexadecimal é igual a {numero:X}')#converte para hexadecimal 
def main():
    numero = int(input('Digite um número inteiro: '))
    base = int(input('''Digite um número para converter o número:
1 para binário
2 para octal 
3 para hexadecimal.
Sua opção: '''))
    conversor(numero, base)
if __name__ == '__main__':
    main()