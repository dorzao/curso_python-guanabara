#script que imprime uma tupla e mostra quais as vogais em cada palavra da mesma
tupla = ('Bandida', 'Safada', 'Renata', 'Pedro', 'Carlinhos', 'Aurelio', 'Jumanji', 'Dragonballz', 'Urubu', 'Zacarias' )
for c in tupla:
    print(end=f'Na palavra {c.upper()} temos as vogais: ')
    if 'a' in c.lower():
        print(end ='a ')
    if 'e' in c.lower():
        print(end='e ')
    if 'i' in c.lower():
        print(end='i ')
    if 'o' in c.lower():
        print(end='o ')
    if 'u' in c.lower():
        print(end='u ')
    print('')
