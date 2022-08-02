#crie um programa que ler 7 valores digitados e os coloque em uma lista, separando-os como ímpar e par. No final mostre os valores pares e ímpares na ordem crescente.
lista = [[],[]]
for c in range(7):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('=-' * 20)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')
