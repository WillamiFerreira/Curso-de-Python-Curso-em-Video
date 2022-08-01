#Faça um programa que calcula a quantida de litros de tinta são necessários para pintar um parede dado sua largura e altura.
l = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
area = l * a
print('A área da parede é {}M²'.format(area))
tin = area/2
print('São necessários {:.3f} litros de tinta para pintar toda a parede' .format(tin))