#script que recebe um valor de salário e faz um reajuste de 15% no salário do mesmo e mostra tanto o novo salário quanto o aumento efetivo
s = float(input('Digite o valor do salário do funcionário: R$ '))
print('O novo salário do funcionário é R$ {:.2f} e o aumento foi de R$ {:.2f}'.format(s * 1.15, s * 0.15))
