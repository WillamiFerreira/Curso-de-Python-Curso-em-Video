#Faça um programa que ler uma frase e retorne ela ao contrário, e classificando de é um palíndromo ou não.
frase = str(input('Digite uma frase: ')).strip().upper().replace(" ","")
inverso = frase[:: - 1]
print( frase, inverso )
if frase == inverso:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
