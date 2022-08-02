#crie uma matriz 3*3 onde os valores são lidos pelo teclado.

matriz = list()
linhas = int(input('Quantas linhas: '))
colunas = int(input('Quantas colunas: '))
linha = list()

for l in range(linhas):
    for c in range(colunas):
        linha.append(int(input(f'Digite um valor para [{l},{c}]: ')))
    matriz.append(linha[:])
    linha.clear()

print('-=' * 20)

for linha in range(linhas):
    for coluna in range(colunas):
        print(f'[{matriz[linha][coluna]:^5}]', end = ' ')
    print()