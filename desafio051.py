#Crie um programa que peça um número inteiro e uma razão, então printe uma progressão aritimetica com dez termos.
print ('=' * 20)
print('10 TERMOS DE UMA PA')
print ('=' * 20)

inicio = int(input('Digite um número inteiro qualquer que será o inicio: '))
razao = int(input('Digite o número que será a razão: '))
decimo = inicio + 9 * razao
 

for c in range(inicio, decimo + razao, razao):
    print(c, end=' ')
print('Acabou')