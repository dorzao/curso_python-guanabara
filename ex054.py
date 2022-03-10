#script que lê ano de nascimento de 7 pessoa e imprime quantos são maiores e quantos são menores de idade
from datetime import date
cma = 0
cme = 0
for c in range (0, 7):
    an = int(input('Digite o ano de nascimento de uma pessoa: '))
    if date.today().year - an <= 21:
        cme = cme + 1
    else:
        cma = cma + 1

print('Das 7 pessoas cadastradas é/são: \n Maior(es): {}\n Menor(es): {} '.format(cma, cme))
