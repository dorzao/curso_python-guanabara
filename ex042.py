#script que recebe 3 lados, informa se pode ser um triângulo, e ainda fala qual o tipo de triângulo
l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
ma = l1
if l2 > ma:
    ma = l2
if l3 > ma:
    ma = l3

if (l1 + l2 + l3 - ma) > ma:
    print('É um triângulo', end='')
    if (l1 == l2) and (l2 == l3):
        print(' Equilátero')
    elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('Não pode ser um triângulo!')