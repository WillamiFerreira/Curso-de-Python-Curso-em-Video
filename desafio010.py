#"conversor" de real para dolar
n1 = float(input('Digite um valor em reais que ele será convertido em dolar R$'))#ler um número real, que será o valor em reais que será convertido.
n2 = n1 / 3.27 #adiciona em uma variável(n2) o resultado da divisão do valor em reais lido pelo valor do dollar atual (3.27)
print('{} reais vale {:.2f} dolares'.format(n1,n2))#imprime o valor de n2 formatado usado o método .format