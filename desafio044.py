#DESAFIO IMCOMPLETO
print('{:=^40}'.format(' LOJAS FERREIRA '))

preco = float(input('Digite o valor do preço das compras: R$: '))
modo = int(input('''Qual a forma de pagamento: ?
1 - à vista - 10% de desconto
2 - À vista no cartão - 5% de desconto
3 - 2x no cartão - Preço normal
4 - 3x no cartão. - 20% de juros
'''))

if modo == 1:
    print(f'O valor a ser pago é {preco - preco/100 * 10} reais.')
elif modo == 2:
    print(f'O valor a ser pago é {preco - preco/100 * 5} reais.' )
elif modo == 3:
    print(f'O valor a ser pago é {preco} reais.')
else:
    print(f'O valor a ser pago é {preco + preco/100 * 20} reais')