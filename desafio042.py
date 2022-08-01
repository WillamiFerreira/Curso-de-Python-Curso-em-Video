#crie um programa que leia 
l1 = float(input('Digete o primeiro lado: '))
l2 = float(input('Digete o segundo lado: '))
l3 = float(input('Digete o terceiro lado: '))

# if l1 == l2 == l3:
#     print('Equilátero')
# elif l1 == l2 or l2 == l3 or l1 == l3:
#     print('Isósceles')
# elif l1 != l2 and l2 != l3:
#     print('Escaleno')

if l2 + l3 > l1 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Pode formar um triângulo: ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 !=l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não pode formar triângulo')

