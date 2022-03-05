#script que calcula a hipotenuza a partir do informe dos 2 catetos
from math import sqrt

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite agora o valor do cateto adjascente: '))
print('Tendo em vista que o cateto oposto é {:.0f} e o cateto adjascente é {:.0f}, a hipotenuza é {:.2f}'.format(co, ca, sqrt(co ** 2 + ca ** 2)))
