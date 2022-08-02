#crie um program que leia números pelo teclado, os armazene em uma lista e depois printe:
# a lista completa
# Uma lista só com os pares
# Uma lists só com os ímpares
lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = input('Deseja continuar? [S/N] ')[0].upper().strip()
    if continuar not in 'NS':
        continuar = input('Resposta inválida! Deseja continuar? [S/N]')[0].upper().strip()
    if continuar == 'N':
        break
pos = 0
while pos < len(lista):
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
    else:
        impares.append(lista[pos])
    pos += 1
print('=-' * 30)
print('A lista completa é ',lista)
print('A lista de pares é ',pares)
print('A lista de ímpares é ',impares)