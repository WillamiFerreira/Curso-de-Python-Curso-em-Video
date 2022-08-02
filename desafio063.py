#Crie um programa que execute a sequência de fibonatte. Crie a opção de quantos elementos da sequência o usuário deseja.
def read(seq):
    seq2 = []
    cont = 0
    while cont < len(seq) - 2:
        seq2.append(seq[cont])
        print(seq2[cont], end=' ')
        cont += 1
        

def fibo(n):
    sequencia = [0, 1]
    c = 0
    
    while c < n:
        x = sequencia[-1]
        sequencia.append(x + sequencia[-2])
        c += 1
    read(sequencia)


def main():
    numero = int(input('Digite quantos elementos voçe de deseja na sequência: '))
    fibo(numero)
if __name__ == "__main__":
 main()