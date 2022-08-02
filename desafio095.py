#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualizações de detalhes do aproveitamento de cada jogador.
jogadores = list()
temp = dict()
while True:
    temp['Nome'] = input('Nome do Jogador: ')
    quant_partidas = int(input(f'Quantas partidas {temp["Nome"]} jogou? '))
    gols_por_partida = list()
    for p in range(1, quant_partidas + 1):
        gols_por_partida.append(int(input(f'Quantos gols na partida {p}? ')))
    temp['Partidas'] = (gols_por_partida)
    temp['Total'] = sum(gols_por_partida)
    jogadores.append(temp.copy())
    continuar = input('Quer continuar? [S/N]')[0].upper().strip()
    if continuar not in 'NS':
        continuar = input('Quer continuar? [S/N]')[0].upper().strip()
    if continuar == "N":
        break
print('=-' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"Total":>8}')
print('_' * 43)
for i, d in enumerate(jogadores):
    print(f'{i:>3} {d["Nome"]:<15}{d["Partidas"]!s:<15s}{d["Total"]:>8}')
print('_' * 43)

while True:
    opc = int(input(('Mostrar dados de qual jogador? (999 para parar) ')))
    if opc == 999:
        break
    while not opc < len(jogadores):
        print('O valor não corresponde a nenhum jogador')
        opc = int(input(('Mostrar dados de qual jogador? (999 para parar) ')))
    jogadores[opc]['Partidas'] = list(jogadores[opc]['Partidas'])
    if opc < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["Nome"]}: ')
        for n in range(len(jogadores[opc]["Partidas"])):
            print(f'No jogo {n + 1} fez {jogadores[opc]["Partidas"][n]} gols.')
print('<<< VOLTE SEMPRE >>>')