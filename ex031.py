#script que calcula preço da viagem de acordo com os km de distância (50 cent até 200km e 45 acima de 200)
d = float(input('Digite a distância da viagem em km/h para saber o preço dela: '))
if d <= 200.0:
    print('Por se tratar de uma viagem mais curta, a tarifa é de R$ 0.50 /km.\n Sua passagem ficará por R$ {:.2f}'.format(d * 0.5))
else:
    print('Desconto detectado! Sua passagem custará R$ 0.45/km.\n Sua passagem custará R$ {:.2f}.'.format(d * 0.45))
