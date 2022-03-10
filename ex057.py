#script que valida registro com sexo
s = input('Digite seu sexo m/f: ')
s = s.lower()
while s != 'm' and s != 'f':
    s = input('Opção inválida! Por favor, digite somente m para masculino ou f para feminino: ')
if s == 'm':
    print('Sexo masculino registrado com êxito! ')
else:
    print('Sexo feminino registrado com êxito! ')
