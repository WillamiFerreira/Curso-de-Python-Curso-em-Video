def aumentar(n, formt = True, per=10):
    """
    Função que almenta o valor recebido em 10%
    """
    if formt == True:
        return moeda(n + (n * per/100))
    else:
        return n +(n*per/100)

def diminuir(n, formt, perc=13):
    """
    Função que diminui o valor recebido em 13%
    """
    if formt == False:
        return n - (n * perc/100)
    else:
        return moeda(n - (n * perc/100))

def dobrar(n, formt):
    if formt == False:
        return n * 2
    else:
        return(moeda(n*2))

def metade(n, formt):
    if formt == False:
        return n / 2
    else:
        return(moeda(n/2))

def moeda(n):
    return (f'R${n:.2f}').replace('.', ',')

def resumo(p, a=0, r=0):
    """
    função que retorna de forma formatada um resumo das funçoes acima e de forma mais legível.
    //significado dos parâmetros//
    p --> preço(valor lido inicialmente)
    a --> % de aumento
    r --> % de redução

    function created by gabriel from CodeinCave
    """
    print('='*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('='*30)
    print(f'{"Preço analisado:":<20}{moeda(p)}')
    print(f'{"Dobro do preço:":<20}{dobrar(p, True)}')
    print(f'{"Metade do preço:":<20}{metade(p, True)}')
    print(f'{a}{"% de aumento:":<18}{aumentar(p, True, a)}')
    print(f'{r}{"% de redução:":<18}{diminuir(p, True, r )}')
