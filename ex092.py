#script que recebe algumas informações, calcula idade, tempo que ainda falta para aposentar, se tiver com carteira de trabalho, e com quantos anos a pessoa vai se aposentar
from datetime import datetime
pessoa = dict()
pessoa['nome'] = input('Qual o nome da pessoa a consultar? ')
nasc = int(input(f'Qual o ano do nascimento de {pessoa["nome"]}? '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input(f'Qual o número da carteira de trabalho de {pessoa["nome"]} (0 = não tem)? '))
if pessoa['ctps'] != 0:
    anoi = int(input(f'Em que ano {pessoa["nome"]} começou a trabalhar? '))
    pessoa['salário'] = float(input(f'Qual o salário de {pessoa["nome"]}? R$ '))
    pessoa['idade de aposentadoria'] = pessoa['idade'] + (35 - (datetime.now().year - anoi) )
    pessoa['anos que faltam para aposentadoria'] = pessoa['idade de aposentadoria'] - pessoa['idade']
else:
    pessoa['ctps'] = 'não tem'
print()
print('=' * 35)
print(f"{'Mostrando relação':^35}")
print('=' * 35)
print()
for k, v in pessoa.items():
    print(f' - {k}: {v}')
print()
print('=' * 35)
