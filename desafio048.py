#Crie um programa que soma todos números ímpares que são múltiplos de 3 entre 1 e 500
s = 0 #Variável acumuladora
for c in range(1, 501, 2):#inicia uma repetição com for que vai de 1 até 500, pulando de 2 em 2, assim só os ímpares são considerados.
    if c % 3 == 0: #usando o operador lógico de módulo para encontrar os múltiplos de 3, e um operador condicional if para quando os múltiplos de 3 forem encontrados...
     s =+ c #o seu valor seja somado ao valor do acumulador
print(f'A soma dos ímpares múltiplos de 3 entre 1 até 500 é {s}')# ao final da repetição, é printado o resultado em uma f-string
    