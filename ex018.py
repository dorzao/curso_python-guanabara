#script que mede seno, cosseno e tangente de um ângulo
from math import tan, cos, sin

a = float(input('Digite o ângulo o qual deseja saber o seno, cosseno e tangente: '))
print('o seno é: {}\n o cosseno é {}\n a tangente é {}.'.format(sin(a), cos(a), tan(a)))
