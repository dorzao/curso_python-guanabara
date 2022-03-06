#script que lê o nome completo da pessoa e escreve o nome todo em maiúsculo, todo em minúsculo, quantas letras sem espaço, e quantas letras tem o primeiro nome
n = input('Digite o seu nome completo: ')
print("""Seu nome todo em maiúsculo fica: {}
Seu nome todo em minújsculo é: {}
Seu nome completo tem {} letras 
Seu primeiro nome tem {} letras.
 """.format(n.upper(), n.lower(), len(''.join(n.split())), len(n.split()[0])  ))
 