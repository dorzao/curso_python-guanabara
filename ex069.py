#script que cadastra pessoas, e depois mostra estatísticas
i = 1
idade = ch = cmn = cv = 0
op = sexo = ''
while True:
    print('-' * 20)
    print(f'Cadastro da {i}ª pessoa')
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    sexo = input('Qual o sexo/gênero [M/F]? ').strip().lower()[0]
    while sexo != 'm' and sexo != 'f':
        print('Opção inválida!')
        sexo = input('Qual o sexo/gênero [M/F]? ').strip().lower()[0]
    if sexo == 'm':
        ch += 1
    if idade > 18:
        cv += 1
    if sexo == 'f' and idade < 18:
        cmn += 1
    op = input('Quer cadastrar mais pessoas [S/N]? ').strip().lower()[0]
    while op != 's' and op != 'n':
        print('Opção inválida! ')
        op = input('Quer cadastrar mais pessoas [S/N]? ').strip().lower()[0]
    if op == 'n':
        break
    else:
        i += 1

print('-' * 20)
print('Balanço final:')
print('-' * 20)
print(f'Todal de pessoas: {i} \n Total de Homens: {ch} \n Maiores de 18 anos: {cv} \n Mulheres com menos de 18 anos: {cmn}. ')