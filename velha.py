import random  # importação da classe random para realizar sorteios

campo = ["_", "_", "_", "_", "_", "_", "_", "_", "_"] # variável global do campo
jogadorPeca = ""  # variável global da peça do jogador
jogador = random.choice((0, 1))  # variável global referente a vez da jogada
oponentePeca = ""  # variável global da peça da computador


def imprimeCampo(campo):  # método para imprimir o campo de jogo
    c = 0
    for i in campo:
        if c % 3 == 0:
            print("")
            c = 0
        print(i, end=' ')
        c += 1

    print("\n")


def ganhou(simbolo, campo):  # método que verifica vencedor (de acordo com as regras do jogo) após cada jogada
    if campo[0] == simbolo and campo[1] == simbolo and campo[2] == simbolo:
        return 1
    if campo[3] == simbolo and campo[4] == simbolo and campo[5] == simbolo:
        return 1
    if campo[6] == simbolo and campo[7] == simbolo and campo[8] == simbolo:
        return 1
    if campo[0] == simbolo and campo[3] == simbolo and campo[6] == simbolo:
        return 1
    if campo[1] == simbolo and campo[4] == simbolo and campo[7] == simbolo:
        return 1
    if campo[2] == simbolo and campo[5] == simbolo and campo[8] == simbolo:
        return 1
    if campo[0] == simbolo and campo[4] == simbolo and campo[8] == simbolo:
        return 1
    if campo[2] == simbolo and campo[4] == simbolo and campo[6] == simbolo:
        return 1


def velha(campo):  # método que verfica se deu velha
    if '_' not in campo:
        return 1


def menu():  # método para o jogador escolher sua peça
    print("Jogo da velha!")
    resposta = input("Você quer ser X ou O? ")
    while resposta != "X" and resposta != "0":
        resposta = input("Resposta inválida! Você quer ser X ou O? ")

    global jogadorPeca  # identifica a variável como global
    global oponentePeca  # identifica a variável como global
    if resposta == "X":
        jogadorPeca = "X"
        oponentePeca = "O"
    else:
        jogadorPeca = "O"
        oponentePeca = "X"


def __main__():  # método principal que chama os demais
    menu()
    jogo()


def jogo():  # método que realiza o jogo
    global jogadorPeca  # identifica a variável como global
    global oponentePeca  # identifica a variável como global
    global jogador  # identifica a variável como global

    while 1:  # while infinito
        if velha(campo):  # verifica se deu velha
            imprimeCampo(campo)
            print("Velha!")
            break
        if jogador:  # seleciona a vez da jogada
            imprimeCampo(campo)

            while 1:  # jogador seleciona a casa onde deseja jogar
                entrada = int(input("Digite a casa [0-8]: "))
                while entrada > 8:
                    entrada = int(input("Entrada inválida! Digite a casa [0-8]: "))
                entrada

                if campo[entrada] == '_':
                    break

            campo[entrada] = jogadorPeca

            jogador = 0

            if ganhou(jogadorPeca, campo):
                imprimeCampo(campo)
                print("Você ganhou!")
                break
        else:
            imprimeCampo(campo)
            while 1:
                pc = random.randint(0, 8)  # é sorteado uma jogada para o oponente

                if campo[pc] == '_':
                    break

            campo[pc] = oponentePeca

            jogador = 1

            if ganhou(oponentePeca, campo):
                imprimeCampo(campo)
                print("Você perdeu!")
                break


__main__()  # chama o método para iniciar o programa