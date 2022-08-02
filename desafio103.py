#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. Oprograma deverá ser capaz de mostrar a ficha do jogador, memsmo que algum dado não tenha sido informado corretamente. 
def ficha (jog='<desconhecido>', gol=0): #função com dois parâmetros opcionais
    print(f'O jogador {jog} fez {gol} gols')

n = str(input('Nome: '))
g= input('Gols: ')
if g.isnumeric(): #testando se o g é numérico
    g = int(g) #se sim, então o type é mudado para int
else:
    g = 0 #se o g for uma frase(não numerico) o seu valor é mudado para zero
if n.strip()=='': #se o valor do n depois de tirar os espaços vários continua vario, então 
    ficha(gol=g) #chamamos a função fazendo a referência do valor padrão para a variável g
else:
    ficha(n, g) #se a variável g ainda possuir algo, significa que um nome foi adicionado, então é levado as duas variáveis