num = int(input('Digite um número: '))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[36m", end=' ')
        cont +=1
    else:
        print('\033[31m', end=' ' )
    print(c, end=' ')

print(f'\n\033[mO número {num} foi divisível por {cont} vezes.')

if cont == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo. ')
