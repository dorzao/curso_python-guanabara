#script que lê 3 segmentos de reta, e diz se é possível se tornar um triângulo
l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
ma = l1
if l2 > ma:
    ma = l2
if l3 > ma:
    ma = l3
if ma == l1:
    if l2 + l3 > ma:
        print('SIM, pode ser um triânculo')
    else: 
        print('NÃO PODE SER UM TRIÂNGULO!')
elif ma == l2:
    if l3 + l1 > ma:
        print('SIM, pode ser um triângulo!')
    else:
        print('NÃO PODE SER UM TRIÂNGULO!')

else:
    if l1 + l2 > ma:
        print('SIM, pode ser um triângulo!')
    else:
        print('NÃO PODE SER UM TRIÂNGULO!')
