import imp
from math import hypot #importando a função hypot que calcula a hipodenusa.
cate_oposto = float(input('O comprimento do cateto oporto é:'))#recebe o valor do cateto oporto.
cate_adjacente = float(input('O comprimento do cateto adjecente é:'))#recebe o valor do cateto adjecente.
hipotenusa = hypot(cate_oposto, cate_adjacente)#chamamos a função hypot com o valor do oposto e adjacente como parâmetro.
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))#retorna o valor da hipotenúsa formatado com duas casas decimais.