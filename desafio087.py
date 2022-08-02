#faça um programa que crie uma matriz 3*3, mostrando no final
#a soma de todos os valores par;
#a soma de todos os valores da terceira coluna;
#O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0 ], [0, 0, 0]]
somapar = mai = somacol = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int (input(f'Digite um valor para [{l},{c}]: '))
print('=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0: #se o valor for par...
            somapar += matriz[l][c] #soma a variável somapar
    print()

print('=-' * 20)
#a)----------
print(f'A soma dos pares é {somapar}')
#b)----------
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da teceira coluna é {somacol}')
#c) ----------
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c]> maior:
        maior = matriz[1][c]
print(f'O maior elemento da segunda linha é {maior}')