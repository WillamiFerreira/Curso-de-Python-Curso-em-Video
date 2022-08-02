#Crie um programa que peça peso e altura de uma pessoa e calcule o IMC dela. Além disso, o programa deve classifica-la de acordo com seu imc como: 
# abaixo do peso - menos de 18.5
# Peso ideal - entre 18.5 e 19
# Sobrepeso - entre 25 e 29
# Obesidade - entre 30 e 39
# Obesidade Morbida - mais de 40

peso = float(input('Qual o seu peso em kg? '))
altura  = float(input('Qual a sua altura em metros? '))

imc = peso / (altura ** 2)#calculo do IMC

#estrutura condicional usando if, elif e else para classificação
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 20:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    imc > 40
    print('Obesidade mórbida')