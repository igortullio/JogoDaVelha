import random

campo = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
jogadorPeca = ""
jogador = 0
oponentePeca = ""
oponente = 0


def imprimeCampo(campo):
    c = 0
    for i in campo:
        if c % 3 == 0:
            print("")
            c = 0
        print(i, end=' ')
        c += 1

    print("\n")


def ganhou(simbolo, campo):
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


def velha(campo):
    if '_' not in campo:
        return 1


def menu():
    print("Jogo da velha!")
    resposta = input("Você quer ser X ou O? ")
    while resposta != "X" and resposta != "0":
        resposta = input("Resposta inválida! Você quer ser X ou O? ")

    global jogadorPeca
    global oponentePeca
    if resposta == "X":
        jogadorPeca = "X"
        oponentePeca = "O"
    else:
        jogadorPeca = "O"
        oponentePeca = "X"


def __main__():
    menu()
    jogo()


def jogo():
    global jogadorPeca
    global oponentePeca
    global jogador
    while 1:
        if velha(campo):
            imprimeCampo(campo)
            print("Velha!")
            break
        if jogador:
            imprimeCampo(campo)

            while 1:
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
                pc = random.randint(0, 8)

                if campo[pc] == '_':
                    break

            campo[pc] = oponentePeca

            jogador = 1

            if ganhou(oponentePeca, campo):
                imprimeCampo(campo)
                print("Você perdeu!")
                break


__main__()