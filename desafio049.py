#Crie uma tabuda usando estruturas de repetição

num = int(input('Digite um número: '))#pede um número inteiro
print('A tabuada de {} é: '.format(num))
for c in range(1, 11):#inicia uma estrutura de repetição com operador lógico for com 10 laços.
    print('{} * {} = {}'.format(num, c, c * num))#em cada laço uma string personalizada é printada com número numerador, denominador e produto.