#crie um programa que peça nome e preço de vários produtos e no final exiba:
#a) Quantos produtos foram comprados;
#b) O valor total da compra;
#c) O produto mais barato;
#d) Quantos produtos custaram mais de 1000 reais.

def compras():
    total = totmais1000 = m_barato = cont = 0 #é crieado inicializadores para valor total, quantidade de itens que valem mais de 1000 reais, valor do item mais mais barato e um contadador para a quantidade de produtos.
    item_m_barato = ' '#variável para o nome do item mais barato.
    while True: #usando while com teste no final...
        nome_produto = input('Digite o nome do produto: ') #peço o nome do produto
        preco_produto = float(input('Preço do produto: R$')) #peço o valor do produto
        cont += 1 #já adiciono mais 1 no contador de produtos.
        total += preco_produto #além de somar seu preço a varial de valor total da compra. 

        if preco_produto > 1000: #se o valor do produto for maior que 1000...
            totmais1000 += 1 #então é somado +1 a variável 'totmais1000'
            
        #configurando o menor preço
        if cont == 1 or preco_produto < m_barato: #se o valor da variável cont for 1, significa que esse é o primeiro produto a contabilizar, ou seja, o seu valor é o menor, ou se o preço do produto atual for menor que o valor de 'm_barato'...
            m_barato = preco_produto #'m_barato' recebe o preço do produto atual.
            item_m_barato = nome_produto #o nome do item atual mais barato é recebido pela variável 'item_m_barato'

        #usando as estruturas if e else para criar uma validação simples de dados, é pergundado ao usuário se ele seja sair do programa, caso sim, o laço é quabrado e as informações são printadas em strings formatas, se não o laço volta ao inicio pedindo o nome e preço do próximo produto.
        continuar = ' '
        if continuar not in 'SN':
            continuar = input('Deseja continuar: [S/N]')[0].upper().strip()
            if continuar == 'N':
                break

    print('============= FIM DO PROGRAMA ===========')
    print(f'O total da compra foi de R${total:.2f}')#os valores foram formatados para ter apenas duas casas decimais.
    print(f'Temos {totmais1000} produtos custando mais de R$1000.00')
    print(f'O produto mais barato foi {item_m_barato} que custa R${m_barato:.2f}')

def main():
    compras()# chama a função.
if __name__ == "__main__":
    main()