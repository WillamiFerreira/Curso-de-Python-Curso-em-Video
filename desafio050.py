#Crie um programa que some peça 5 números inteiros e verifique se ele é par ou não, no final, printe quantos números pares foram lidos e qual a soma deles.
soma = contador = 0 #duas variáveis inicializadoras são criadas, a primeira armazenará a soma dos pares e a segunda o valor correspondente a quantidade de números pares que serão lidos.

for _ in range(0, 6): #usando a estrutura de repetição for, fazermos 5 laços. Em cada laço...
    num = int(input('Digite um número inteiro qualquer: '))#é pedido um número inteiro.
    if num % 2 == 0: #se o resto desse número por dois é 0, significa que ele é par e os comandos dentro do if serão executados. Caso não seja, o programa segue para o próximo laço.
        contador += 1 # é adicionado +1 ao contador.
        soma += num #o valor do número é somado ao valor da variável soma.
print ('A soma de todos {} números pares é {}'.format(contador, soma)) #quando todos os 5 laços forem feitos, a repetição acaba e o comando imediatamente depois dele é executado, nesse caso é um printe formatado com os valores das variáveis 'contador' e 'soma'.
