# Crie um programa que peça números e os armazene em uma lista, então dopis printe a lista em ordem decresente, quantos números foram digitados e se o número 5 foi ou não digitado.
numeros = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)

    continuar = input('Deseja continuar [S/N]: ')[0].strip().upper()
    while continuar not in 'SN':
         continuar = input('Valor incorreto! Deseja continuar [S/N]')
         
    if continuar == 'N':
        break

print('=-' * 20)
numeros.sort(reverse=True)
print(f'Voce digitou {len(numeros)} elementos')
print('Os valores em ordem decrescente são', numeros)

if 5 in numeros:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 NÃO está na lista!')
