#script com uma lista de 10 produtos com preço utilizando tupla
print('='*51)
print(f"{'Lista de produtos':^51}")
print('='*51)
lista = ('Leite', 5.50, 'Arroz', 12.70, 'Biscoito', 3.30, 'Feijão', 9.20, 'Coca Cola', 7.99, 'Suco de uva', 8.77, 'Pastel de Frango', 6.99, 'Caixa de Morangos', 12.03, 'Água Mineral', 2.59, 'Sabonete', 0.99)
i = 0
while i < len(lista):
    print(end='{: .<42} R$'.format(lista[i]))
    i += 1
    print('{:>5.2f}'.format(lista[i]))
    i += 1
print('='*51, '\n')
