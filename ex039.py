#script que recebe o ano de nascimento do sujeito, calcula a situação de alistamento do mesmo, e em caso ser a hora, mostrar a diferença do tempo em anos
from datetime import date
d = int(input('Digite a data de seu nascimento: '))
da = date.today().year
if da - d == 18:
    print('Tá na hora filhão! Você fez ou faz 18 este ano, a hora é agora!')
elif da - d < 18:
    print('Ainda não está na hora! Faltam {} anos para você se alistar.'.format(18 - (da - d) ))
else:
    print('Já não é mais necessário o alistamento! Voce se alistou ou deveria ter se alistado há {} anos.'.format( (da - d) - 18 ))
