#Crei um programa que tenha uma função fatorial() que receba dois parâmtros: o primeiro que indique o número a calcular e o outro chamado show, que será valor lógico, indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(a=0, s=False):
    if s == True:
        #mostrar o calculo
        resul = 1
        print('=-'* 20)
        for n in range(a, 0, -1):
            resul *= n
            print(f'{n} x' if n>1 else n, end =' ' )
        return(f'= {resul}')
    else:
        resul = 1
        for n in range(a, 0, -1):
            resul *= n
        return (f'''
{"=-" * 20}
{resul}''')
print(fatorial(5, s=True))