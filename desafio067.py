#Crie um programa que peça um número e mostre a sua tabuada até o 10, se um valor negativo for lido, então o programa é encerrado.
def tabuada():
    while True:
        n = int(input('''Quer ver a tabuada de qual valor? (número negativo para encerar): '''))
        if n < 0:
            print('PROGRAMA ENCERRADO. Volte sempre!')
            break
        else:
            x = 1
            for c in range(0, 10):
                print(f'{n} x {x} = {n * x}')
                x += 1
            print('='*30)
def main():
    tabuada()
if __name__ == "__main__":
	main()