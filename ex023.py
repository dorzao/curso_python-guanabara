#script que recebe um númeto de 1 a 9999 e imprime x unidades, x dezenas, x centenas, etc
n = input('Digite um número de 1 até 9999 (preencha as 4 casas, com 0 exemplo 10 = 0010 e 884 = 0884): ')
print("""
{} Unidades de milhar
{} Centenas
{} Dezenas
{} Unidades
""".format(n[0], n[1], n[2], n[3]))
