#crie um programa onde 4 jogadores joguem um dado e tenham resultados aletatórios. Guarde esses resulatados em um dicionário.No final, coloque esse dicionário em ordem. Sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep

d = dict()
for p in range(1, 5):
    d[f'{"jogador"}{p}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in d.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=-' * 30)

posi = 1
print(f'{"== RANKING DOS JOGADORES ==":^30}')
for p in sorted(d, key=d.get, reverse=True):#usando os parâmetros key e reverse da função sorted
    print(f'{posi}º lugar: {p} com {d[p]}.')
    sleep(1)
    posi += 1
print()
