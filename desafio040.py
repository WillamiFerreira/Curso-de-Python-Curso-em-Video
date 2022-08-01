#Crie um programa que calcule a média de duas notas e print situações diferentes que dependem do resultado da média.
n1 = float(input('Digite a primeira nota: '))#pede a nota um
n2 = float(input('Digite a segunda nota: '))#pede a nota dois

media = (n1 + n2) / 2 #soma as duas notas e as divide por dois, e armazena na variável média.

#usando as estruturas if, elif e else...
if media <= 5: # se a média for menor ou igual a cinco, então é imprimido "REPROVADO".
    print('REPROVADO')
elif 5 < media < 7: #Se a média for maior que 5 e menor que 7, então é imprimido "RECUPERAÇÃO".
    print('RECUPERAÇÃO') 
else:
    media >= 7#se a média for igual ou maior que 7, então é imprimido "APROVADO".
    print('APROVADO')