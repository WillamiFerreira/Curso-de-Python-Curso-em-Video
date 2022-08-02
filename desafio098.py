#faça um programa que tenha uma função chamada contador(), que receba três parâmetros: incio, fim e passo. Seu programa tem que realizar três contagens atravês da função criada:
# de um até 10
#de 10 até 0 de 2 em 2
#uma contagem personalizada

from time import sleep
def contador (a, b, p):
    print(f'=-' * 25)
    print(f'Contagem de {a} até {b} de {abs(p)} em {abs(p)}')
    if a < b:
        for n in range(a, b + p, p):
            print(f'{n}', end = ' ', flush=True)
            sleep(0.5)
        print('FIM')
    else:
        for n in range(a, b - p, -p):
            print(n, end = ' ', flush=True)
            sleep(0.5)
        print('FIM')
    if p < 0:
        abs(p)
        for n in range(a, b + p, p):
            print(n, end = ' ', flush=True)
            sleep(0.5)
        print('FIM')
print('=-'* 25)
print('Contagem até 10 de 1 em 1')

for n in range(1, 11, 1):
    print(n, end =' ', flush=True)
    sleep(0.5)
print('FIM!')
print('=-'* 25)
print('Contagem de 0 até 10 de 2 em 2')
for n in range(10 + 2, -1, -2):
    print(n, end=' ', flush=True)
    sleep(0.5)
print('FIM!')
print('=-'* 25)

def main():
    a = int(input('Inicio: '))
    b = int(input('Final:  '))
    p = int(input('Passo:  '))
    if p == 0:
        p = 1
    contador(a, b, p)

if __name__ == "__main__":
    main()