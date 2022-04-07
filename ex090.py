#script que recebe nome e média de um aluno, e mostre sua situação pro meio de um dicionário (Se nota maior que 7 aprovado se não reprovado)
aluno = {}
aluno['nome'] = input('Qual o nome do aluno? ')
aluno['media'] = float(input(f'qual a média de {aluno["nome"]}? '))
print(end=f'A média de {aluno["nome"]} é {aluno["media"]} e ele(a) está ')
if aluno['media'] >= 7.0:
    print('APROVADO(A)')
else:
    print('REPROVADO(A)')
