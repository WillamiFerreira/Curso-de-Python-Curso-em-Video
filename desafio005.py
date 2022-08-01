#Built a program that show the predecessor and the succesor of a number read by the keyboard.
valor = int(input('Digite em valor '))#read a integer value by the keyboard and store it in a variable.
print('O antecessor de {} é {}'.format(valor, valor - 1)) #print the the value and it´s predecessor in a formated string.
print('O sucessor de {} é {}' .format(valor, valor + 1))#print the value and it´s succesor in a formated string.