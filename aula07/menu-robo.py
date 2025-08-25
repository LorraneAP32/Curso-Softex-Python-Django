posicao = 0  # posição inicial do robô

while True:
    print("Menu de Comandos: \n "
           '1 - Avançar\n'
          '2 - Recuar\n'
          '3 - Status\n'
          '4 - Desligar\n')


    comando = input("Escolha uma opção: ")

    if comando == '1':
        posicao += 1
        print("O robô avançou para a posição ", posicao)
    elif comando == '2':
        posicao -= 1
        print("O robô recuou para a posição ", posicao)
    elif comando == '3':
        print("O robô está na posição ", posicao)
    elif comando == '4':
        print("Desligando o robô...")
        break
    else:
        print("Comando inválido. Tente novamente.")
