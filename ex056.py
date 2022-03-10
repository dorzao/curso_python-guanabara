#script cadastra 4 pessoas, no final imprime a média de idade, o nome do homem mais velho, e quantas mulheres tem menos que 21 anos
novinha = 0
hmv = 'Não foram cadastrados homens!'
iha = 0
media = 0
nome = ['', '', '', '']
idade = [0, 0, 0, 0]
sexo = ['f', 'f', 'f', 'f']
nome[3] = input('Digite o primeiro nome: ')
idade[3] = int(input('Digite a idade de {}: '.format(nome[3])))
sexo[3] = input('Digite o sexo de {} (Somente m para masculino e f para feminino): )'.format(nome[3]))
if sexo[3] != 'm' and sexo[3] != 'f':
    print('Opção inválida! Fechando o programa')
    exit()

if sexo[3] == 'm':
    hmv = nome[3]
    iha = idade[3]
elif sexo[3] == 'f' and idade[3] <= 21:
    novinha = novinha +1
    
media = idade[3]


for c in range (0, 3):
    nome[c] = input('Digite o próximo nome:')
    idade[c] = int(input('Qual a idade de {} ? '.format(nome[c]))) 
    sexo[c] = input('Informe o sexo de {} apenas com m para masculino e f para feminino: '.format(nome[c]))
    media = media + idade[c]
    if sexo[c] != 'm' and sexo[c] != 'f':
        print('Opção inválida! Encerrando programa...')
        exit()
    if sexo[c] == 'm':
        if iha < idade[c]:
            iha = idade[c]
            hmv = '( Homem mais velho é: {}'.format(nome[c])
    else:
        if idade[c] < 21:
            novinha = novinha + 1

if novinha == 0:
    novinha = 'Nenhuma'

print('A média das idades é: {}\n O número de mulheres com menos de 21 anos é: {}\n {}'.format(media /4, novinha, hmv))
#Até agora, o que mais me deu trabalho
