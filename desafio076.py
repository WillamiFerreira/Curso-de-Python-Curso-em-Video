#Crie uma lista com nomes de itens e seus valores, no final printe os valores dessa lista como uma tabela.
listagem = ('Lapís', 1.75,
            'Borracha', 2,
            'Estojo', 15.89,
            'Mochila', 120.45,
            'canetas', 22.50)
for item in range(0, len(listagem), 2):
    print(f'{listagem[item]:.<30} R$ {listagem[item + 1]:.2f}')
    