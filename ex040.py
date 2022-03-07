#script que recebe 2 notas, calcula a média, e mostra a situação conforme a nota (aprovado, reprovado ou em recuperação)
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite agora sua segunda nota: '))
if (n1 + n2) /2 <= 5:
    print('Tu estás reprovado com a nota {:.1f}'.format( (n1 + n2) / 2))
elif (n1 + n2) /2 <= 6:
    print('Tu estás de recuperação com a nota de {:.1f}.'.format( (n1 + n2) /2 ))
else:
    print('Tu estás aprovado com {:.1f} ponto(s).'.format( (n1 + n2) / 2 ))
