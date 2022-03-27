#script que recebe nota de n alunos, calcula a média entre 2 notas, depois mostra as 2 notas de cada aluno pelo seu id
aluno = list()
alunos = list()
cont = 0
while True:
    nome = input('Qual o nome do aluno? ')
    nota1 = float(input(f'Qual a primeira nota de {nome}? '))
    nota2 = float(input(f'Qual a segunda nota de {nome}? '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(( nota1 + nota2) / 2)
    alunos.append(aluno[:])
    aluno.clear()
    op = input('Quer cadastrar mais alunos[S/N]? ').strip().lower()[0]
    while op != 's' and op != 'n':
        print('Opção inválida! ')
        op = input('Quer cadastrar mais alunos[S/N]? ').strip().lower()[0]
    if op == 'n':
        break
print(end=f"{'  id |':<6}")
print(end=f"{' Nome':<20}")
print(f"{'| Média':<5}")
print('-' * 34)
for a in range (0, len(alunos)):
    print(end=f'{a:^6}')
    for c in range (0, 4):
        if c == 0:
            print(end=f' {alunos[a][c]:<20}')
        if c == 3:
            print(f' {alunos[a][c]:<5}')

while True:
    id = int(input('Digite o id de um aluno para saber a nota dele(a) [999 fecha o programa]: '))
    if id == 999:
        print('Fechando o programa...')
        break
    print(f'As notas de {alunos[id][0]} foram respectivamente: {alunos[id][1]} e {alunos[id][2]} ')
