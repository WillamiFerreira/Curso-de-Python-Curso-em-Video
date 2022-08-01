#faça um programa que leia um número float e retorne somente sua parte inteira
import math
numero = float(input('Digite um número com casas decimais diverentes de zero: '))
print('O número {} tem a parte inteira {}'.format(numero, math.trunc(numero)))#usei a função trunc() do módulo math, para retirar as casas decimais.