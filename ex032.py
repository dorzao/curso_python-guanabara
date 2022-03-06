#script que recebe um falaor de ano e calcula se é bisexto
n = int(input('Digite um ano para saber se é bisexto: '))
if n % 4 == 0:
    print(n, ' é um ano bisexto!')
else:
    print(n, ' NÃO é um ano bisexto!')
