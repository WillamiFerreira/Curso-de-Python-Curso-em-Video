#Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros. Seu programa tem analisar todos mos valores e dizer qual deles é o maior.
from time import sleep
#1º passo - criar o bloco principal, chamando a função maior().
#2º passo - criar a função maior() com a possibilidade de receber n parâmetros.
#3º passo - criar variável inicial zero, então criar sistema de repetição para analizar cada parãmetro e substituir o valor da variável pelo maior parâmetro.
def maior(*n):
    print('-=' * 20)
    print('Anlisando os valores passados...')
    sleep(0.5)
    for v in n:
        print(v, end=' ', flush=True)
        sleep(0.5)
    sleep(0.5)
    print(f'Foram informados {len(n)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {max(n)}.')
    print()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)