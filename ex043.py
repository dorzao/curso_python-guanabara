#script que calcula imc e o status 
p = float(input('Digite su peso/sua massa em kg: '))
a = float(input('Digite sua altura em metros.centímetros: '))
imc = p / (a ** 2)
print('Seu imc é de {:.1f} e sua situação é de: '.format(imc), end='')
if imc <= 18.5:
    print('Pessoa abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
