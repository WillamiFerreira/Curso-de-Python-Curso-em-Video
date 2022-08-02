#Crie um programa que tenha a função leiaint(), que ai funcionar de forma semelhantde a função input()do Python, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaint(a=0):
    while True:#inicia um laço while.
        global n #define que a variável n que será usada será a global.
        n = input('Digite um número: ')#usa a variável global n para pedir um número, porém com entrada str.
        if n.isnumeric(): #testa se a string lida é numerica. Se for...
            n = int(n) #...converte para inteiro e... 
            break# dá break no while, retornado o valor n agr transformado em int.
        else: #mas se a string lida não for numérica, então é printado uma mensagem de erro e o laço recomeça pedindo um novo valor.
            print('ERRO! Digite um número válido!')
    return n

n = leiaint()#Chama a função leiaint().
print(f'Você acabou de digitar o número {n}')