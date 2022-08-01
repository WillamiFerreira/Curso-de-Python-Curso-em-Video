#crie um programa que le dois números e os compare, dizendo qual é maior ou se são iguais
def comparador(vl1, vl2):
    if vl1 > vl2:
        print('O primeiro valor é maior')
    elif vl1 < vl2:
        print('O segundo valor é maior')
    else:
        print('Não existe valor maior, os dois são iguais')

def main():
    #as variáveis abaixo pedem um número inteiro, então são levadas para a função 'comparador' como parâmetros.
    primeiro_valor = int(input('Digite um valor: '))
    segundo_valor = int(input('Digite um segundo valor: '))
    comparador(primeiro_valor, segundo_valor)   
if __name__ == '__main__':
    main()