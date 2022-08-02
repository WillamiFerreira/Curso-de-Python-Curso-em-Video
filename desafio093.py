#Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, Tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.
d = dict()
d['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {d["nome"]} jogou? '))
d['gols'] = list()
for partida in range(0, partidas):
    d['gols'].append(int(input(f'Quantos gols na partidada {partida}? ')))
d['total'] = sum(d['gols'])
print('=-' * 25)
print(d)
print('=-' * 25)
for k, v in d.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 25)
print(f'O jogador {d["nome"]} jogou {partidas} partidas.')
for n in range(len(d['gols'])):
    print(f'    => Na partida {n}, fez {d["gols"][n]} gols.')
print(f'foi um total de {d["total"]} gols.')
print()