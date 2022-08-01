#Crie um programa que leia cinco números inteiros e ordene-os em ordem crecente sem usar o método.short()
lista = []#Criamos uma lista vazia
for c in range(5): #usando a estrutura de repetição for para gerar 5 laços, onde c começa como 0 e termina como 4.
    n = int(input('Dige um valor: '))#ler um valor  e armazana em n
    if c == 0 or n > lista[-1]: #if o c for igual a zero, significa que é o primeiro laço, ou seja o número lido é o maior e o menor, OU se o numero lido for menor maior que o último da lista...
        lista.append(n)#ele é adicionado na última posição da lista. Essa algoritimo sempre garante o lugar do maior na última posição. 
    else: #se não for o primeiro laço, nem o valor lido for maior que o último da lista
        pos = 0#índica a posição 0 da lista.
        while pos < len(lista):#para não criar um looping infinito, o while só é executado até atingir o tamanho atual da lista.
            if n <= lista[pos]: #se o valor lido for menor ou igual que o valor da posição analizada no laço, se o valor lido for maior então o laço parte para o próximo número da lista.
                lista.insert(pos, n)#ent, o valor de n e adicionado no a posição do laço atual.
                break
            pos += 1
print(lista)