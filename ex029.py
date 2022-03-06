#script que recebe velocidade de um carro, se maior que 80km/h imprime a mensagem de que será multado, e a multa é de R$ 7,00 por km excedente
v = float(input('Digite a velocidade atual do seu carro em km/h:'))
if v > 80.0:
    print('Você será multado! o limite de velocidade é 80.0 km/h e você está a {:.1f}.\n O total da sua multa é de R$ {:.2f}.'.format(v, (v - 80.0) * 7))
else:
    print('Ok! Você está a {:.1f} km/h o que está dentro do limite permitido.\n Boa viagem!'.format(v))
