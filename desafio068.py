#Crie um jogo de par ou ímpar. O jogador deve entrar com um número e a escolha entre par ou ímpar. Sussetivas jogadas devem ser feitas até o jogador perder, então mostra quantas jogadas o jogador venceu.
from random import randint
def jogar():
    print('=-=-=-=-=-=-=-=-=-==-=--=')
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-=-=-=-=-=-=-=-=-==-=--=')
    vt = 0
    while True:
        humannunber = int(input('Digite um valor: '))
        ianunber = randint(0, 10)
        soma = humannunber + ianunber
        #validação de entrada
        humanchoice = ' '
        while humanchoice not in 'PI':
            humanchoice = str(input('Par ou Ímpar? [P/I] '))[0].upper()

        print('=' * 20)
        print(f'Você jogou {humannunber} e o cumputador {ianunber}. Total de {soma}')
        print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR') #if e else dentro de print
        print('=' * 20)

        
        if humanchoice == 'P':
            if soma % 2 == 0:
                print('VOCÊ VENCEU!')
                print('Vamos jogar mais uma')
                vt += 1
            else:
                 print('VOCÊ PERDEU!')
                 break
        else:
            if soma % 2 == 0:
                print('VOCÊ PERDEU!')
                break
            else:
                print('VOCÊ VENCEU!')
                print('Vamos jogar mais uma')
                vt += 1
    print(f'Você ganhou {vt} vezes')
        
def main():
    jogar()
if __name__ == "__main__":
	main()