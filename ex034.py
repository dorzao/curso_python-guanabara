#script que recebe o valor do salário, se maior que 1250, aumenta 10% se menor, 15%
s = float(input('Digite o salário para saber seu reajuste: R$ '))
if s <= 1250.0:
    print("""Seu novo salário é de R$ {:.2f}.
    Seu reajuste foi de 15% 
    Seu aumento salarial foi de: R$ {:.2f}.""".format(s * 1.15, s * 0.15))
else:
    print("""Seu novo salário é de R$ {:.2f}.
    Seu reajuste foi de 10%
    Seu aumento foi de R$ {:.2f}
    """.format(s * 1.1, s * 0.1))
