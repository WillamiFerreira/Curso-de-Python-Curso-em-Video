#Crie um programa que peça dois números e que tenha as seguintes opções: 
#somar
#multiplicar
#maior
#novos números
#sair do programa

from time import sleep
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segunda valor: '))
opcao = 0
while opcao != 5: #Enquanto o valor de opcao for diferente de 5, o bloco é executado.
	opcao = int(input('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>>> Qual sua opção? '''))
	if opcao == 1:
		print(f'A soma entre {primeiro_valor} e {segundo_valor} é {primeiro_valor + segundo_valor}')

	elif opcao == 2:
		print(f'A multiplicação entre {primeiro_valor} e {segundo_valor} é {primeiro_valor * segundo_valor}')

	elif opcao == 3:
		if primeiro_valor > segundo_valor:
				maior = primeiro_valor
		else:
				maior = segundo_valor
		print('Entre {} e {} o maior é {}'.format(primeiro_valor, segundo_valor, maior))

	elif opcao == 4:
		primeiro_valor = int(input('Digite o primeiro valor: '))
		segundo_valor = int(input('Digite o segunda valor: '))
		
	elif opcao == 5:
		print('finalizando...')
		sleep(2)
		print('Até logo!')
	else:
		print('Opção inválida. Tente novamente')
	print('=-=' * 10)
print('fim do programa!')

		
