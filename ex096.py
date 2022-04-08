#script que cria uma função que calcula área de um terreno

def cte(a, b):
    print(f'A área total de um terreno de {a} de altura por {b} de largura é de {a * b}m². Veja')
    for c in range (0, a):
        print('[ ]' * b)
                

#programa principal
print(f"{'Calculador deterreno':^40}")
print('=' * 40)
a = int(input('Qual a Altura do terreno (m)? '))
b = int(input('Qual a largura do terreno (m)? '))
cte(a, b)
