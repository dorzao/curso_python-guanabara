#script que recebe um nome completo e imprime o primeiro e o último nome
n = input('Digite seu nome completo: ')
print('Seu primeiro nome é: {}\n Seu último nome é: {}.'.format(n.split()[0], n.rsplit()[len(n.rsplit()) - 1] ))
