#script que diz tudo sobre algo digitado
resultado = input('Digite Algo: ')
print('O tipo primitivo deste valor é:  ', type(resultado))
print('Contem somente espaços? ', resultado.isspace())
print('É um número? ', resultado.isnumeric())
print('É alfabético? ', resultado.isalpha())
print('É alfanumérico', resultado.isalnum())
print('È tudo em maiúsculo? ', resultado.isupper())
print('É só em letrasc minúsculas? ', resultado.islower())
