#script que verifica a possibilidade de realização de empréstimo
e = float(input('Qual o valor do empréstimo? R$ '))
s = float(input('Qual o seu salário? R$ '))
t = int(input('Em quantos anos pretende financiar o empréstimo? '))

if (s * 0.3) * (t *12) >= e:
    print('Empréstimo aprovado! Tu pagarás {} parcelas mensais de R$ {:.2f}'.format(t * 12, e / (t * 12) ))
else:
    print('Emprestimo negado! Com um salário de R$ {:.2f}, num período de financiamento de {} meses, seu empréstimo máximo é de R$ {:.2f}! '.format(s, t * 12, (0.3 *s) * (t * 12) ))
