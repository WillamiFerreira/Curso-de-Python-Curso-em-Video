def brasileirao():
    clas = ('Palmeiras', 'Athletico-PR', 'Atlético-MG','Corinthians', 'Internacional', 'Fluminence', 'São Paulo', 'Flamengo', 'Botafogo', "Santos", 'Avaí', 'América_MG', 'Bragantino', 'Ceará-MG', 'Atlético-GO', 'Goiás', 'Cuiabá', 'Juventide', 'Fortaleza')
    print('='*30)
    print('Lista de times do Brasileirão:' ,clas)
    print('='*30)
    print('Os cinco primeiros colocados são', clas[:5])
    print('='*30)
    print('Os quantro últimos são:', clas[-4:])
    print('='*30)
    print('Os times em ordem alfabética são:', sorted(clas))
    print('='*30)
    for time in clas:
        if time == 'Goiás':
            print(f'O Goiás está na {clas.index(time) + 1}º posição')
        else:
            pass

def main():
    brasileirao()
if __name__ == "__main__":
    main()