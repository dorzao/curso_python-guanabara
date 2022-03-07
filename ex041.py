#script que calcula categoria conforme a idade. Idades: até 9 mirin, 10 a 14 infantil, 15 a 19 junior, 20 senior, mais de 20 master
from datetime import date
dn = int(input('Digite o ano do seu nascimento: '))
da = date.today().year
id = da - dn
print('sua idade é {} e sua categoria da natação é: '.format(id), end='')
if id <= 9:
    print('Mirin')
elif id <= 14:
    print('Infantil')
elif id <= 19:
    print('Junior')
elif id == 20:
    print('Senior')
else:
    print('Master')
