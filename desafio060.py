#criar um programa que calcula o fatorial de um programa lido pelo teclado.
def gera_fatorial(n):
    resultado = 1 #variável que armazena o resultado de cada multiplicação da fatorial.
    for _ in range(1, n+1): #para cada número de 1 até n...
        print(_, end=' ') #printe o número e não quebre linha...
        print('x'if _<n else'=', end=' ')#print 'x' se o número forma menor que 'n', se não for, printe'='
        resultado *= _ #em cada laço uma nova multiplicação é feita e esses resultados são armazenados aqui.
    print(resultado) #ao final do ciclo, é printado o resuldado.

def main(): 
    n = int(input('Numero: '))#pede um valor inteiro e armazena em 'n'.
    gera_fatorial(n) #chama a função 'gera_fatorial levando 'n' como parâmetro.'
if __name__ == "__main__":
    main()