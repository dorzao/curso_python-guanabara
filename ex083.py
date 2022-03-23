#script que analisa se uma expressão é válida
exp = input('Digite a expressão: ')
if exp.index(')') < exp.index('('):
    print('Expressão inválida! Jamais feche parenteses antes de abrir!')
elif exp.count('(') != exp.count(')'):
    print('Expressão inválida! Verifique o número de parenteses...')
else:
    print('Expressão válida')
