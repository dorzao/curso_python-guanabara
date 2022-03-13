#script que recebe n números, pergunta se quer continuar, imprime a média, o maior e o menor
n = ma = me = i = soma = 0
v = ''
n = int(input('Digite um número: '))
v = input('Quer continuar[S/N] ? ').lower()
v = v.lower()
ma = me = n
soma += n
i += 1
while v != 's' and v != 'n':
    print('Opção inválida!')
    v = input('Quer continuar[S/N] ? ').lower()
    v = v.lower()

if v == 's':
  while v == 's':
      n = int(input('Digite um número: '))
      soma += n
      i += 1
      if n > ma:
          ma = n
      if n < me:
         me = n
      v = input('Quer continuar[S/N] ? ').lower()
      v = v.lower()
      while v != 's' and v != 'n':
          print('Opção inválida!')
          v = input('Quer continuar[S/N] ? ').lower()
          v = v.lower()
      if v == 'n':
          print('Tu somaste {} números, a média entre eles é {:.1f}, o maior foi {} e o menor foi {}! '.format(i, soma / i, ma, me))

elif v == 'n':
    print('Tu somaste {} números, a média entre eles é {:.1f}, o maior foi {} e o menor foi {}! '.format(i, soma / i, ma, me))

    