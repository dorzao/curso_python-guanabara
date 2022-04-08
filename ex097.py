#script que tem cabeçalhos do tamando das mensagens
def escreva(msg):
    print('=' * len(msg))
    print(msg)
    print('=' * len(msg))


#Programa principal
escreva('Teste gigante')
escreva('Cruzeiro o mais querido do Brasil')
escreva('Galo não tem tri')
escreva(input('Digite uma nova mensagem para ver o tamanho certinho de seu cabeçalho: '))
