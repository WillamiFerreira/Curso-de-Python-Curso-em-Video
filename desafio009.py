#crie um programa que ler um número e retorna a sua tabuada até o 10
n = int(input('Digite um número: '))
a = n * 2
b = n * 3
c = n * 4
d = n * 5
e = n * 6
f = n * 7
g = n * 8
h = n * 9
i = n * 10
print('''A tabuada de {} é:
         {} * 2 = {}
         {} * 3 = {}
         {} * 4 = {}
         {} * 5 = {}
         {} * 6 = {}
         {} * 7 = {}
         {} * 8 = {}
         {} * 9 = {}
         {} * 10 = {}''' .format(n,n,a,n,b,n,c,n,d,n,e,n,f,n,g,n,h,n,i))
