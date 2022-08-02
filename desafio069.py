#Crie um programa que peça idade e sexo de várias pessoas, a cada pessoa ele pergunte se o user deseja continuar, no final mostre:
# Quantas pessoas com mais de 18 anos;
# Quantidade de homens;
# Quantidade de mulherds com menos de 20 anos
def registrar():
	mais18 = 0
	homens = 0
	mulheresmenos20 = 0
	while True:
		idade = int(input('Idade: '))
		sexo = ' '
		while sexo not in 'MF':
			sexo = str(input('Sexo: [M/F]'))[0].strip().upper()
		if idade > 18:
			mais18 += 1
		if sexo == 'M':
			homens += 1
		if sexo == 'M' and idade < 20:
			mulheresmenos20 += 1

		continuar = ' '
		while continuar not in 'SN':
			continuar = input('Deseja continuar? [S/N]')[0].upper()
		if continuar == "N":
			break
	print(f'{mais18} pessoas com mais de 18 anos.')
	print(f'{homens} homens foram registrados.')
	print(f'{mulheresmenos20} mulheres com menos de 20 anos.')

def main():
	registrar()
if __name__ == "__main__":
	main()