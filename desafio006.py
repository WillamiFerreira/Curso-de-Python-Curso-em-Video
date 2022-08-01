#crie um programa que ler um valor e retorne:
#a) O dobro
#b) O triplo
#c) A potência por dois 

valor = int(input('Digite um valor: ')) #ler um valor inteiro
print('O dobro de {} é {}' .format(valor, valor*2)) #usa o operador lógico de multiplicação no parâmetro do método .format() para calcular o dobro e retornar em uma f-string.
print('O triplo de {} é {}'.format (valor, valor*3)) #usa o operador lógico de multiplicação no parâmetro do método .format() para calcular o triplo e retornar em uma f-string.
print('A raiz quadrada de {} é {}'.format (valor, valor**2)) #usa o operador lógico de potênciação no parâmetro do método .format() para calcular a potência por dois e retornar em uma f-string.