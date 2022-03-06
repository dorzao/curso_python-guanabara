#script que adiciona uma frase a uma variável, conta quandos 'as' tem, a posição do primeiro a e do último a
f = input('Digite uma frase: ')
print("""
Quantas letras a? {}
Qual a posição da primeira letra a? {}
qual a posição da última letra a? {}
""".format(f.lower().count('a'), f.lower().find('a'), f.lower().rfind('a')))
