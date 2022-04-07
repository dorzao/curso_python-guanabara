#script cadastra n pessoas, e faz levantamentos
pessoas = []
mulheres = []
acmedia = []
pessoa = {}
media = 0
while True:
    pessoa['nome'] = input('Qual o nome da pessoa a cadastrar? ')
    pessoa['sexo'] = input(f'Qual o sexo de {pessoa["nome"]}[M/F]? ').strip().upper()[0]
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        print('Opção inválida! ')
        pessoa['sexo'] = input(f'Qual o sexo de {pessoa["sexo"]}[M/F]? ').strip().upper()[0]
    pessoa['idade'] = int(input(f'Qual a idade de {pessoa["nome"]}? '))
    media += pessoa['idade']
    op = input('Quer cadastrar mais pessoas[S/N]? ').strip().upper()
    while op != 'S' and op != 'N':
        print('Opção inválida!')
        op = input('Quer cadastrar mais pessoas[S/N]? ').strip().upper()
    pessoas.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa.clear()
    if op == 'N':
        break
media = media / len(pessoas)
print('=' * 35)

print(f'A) Ao todo tem {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade total é de {media:.1f} anos de idade')
print(end=f'C) Ao todo foram cadastradas {len(mulheres)} mulheres; e a lista de mulheres é: ')
for c in mulheres:
    print(c, end='  ')
print()
print(end=f'D) A lista de pessoas com idade superior à média {media:.1f} é/são:  ')
for c in range (0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(pessoas[c]['nome'], end='  ')
print()
print('=' * 35)
