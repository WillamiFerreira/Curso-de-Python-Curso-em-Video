#Crie um programa que simule uma caixa registradora, pedindo o valor do saque(valor inteiro) e retorne quantas notas saem. As notas podem ser de 50, 20, 10, 5 e 1 real.
def banco():
    print('='* 30)
    print('{:^30}'.format('PATINHAS`N NEPHEWS'))
    print('='* 30)
    valor = int(input('Que valor voçe quer sacar? RS'))
    total = valor
    ced = 50
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} cédulas de R${ced}')
            if ced == 50:
                    ced = 20
            elif ced == 20:
                    ced = 10
            elif ced == 10:
                    ced = 1
            totced = 0
            if total == 0:
                break
            
def main():
    banco()
if __name__ == "__main__":
    main()