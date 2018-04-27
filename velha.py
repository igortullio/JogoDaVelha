import random

campo = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

jogador = random.choice((0, 1))


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
    resposta = input("Você quer ser X ou O?")
    while resposta != "X" or "O":
        if resposta == "X":
            jogador = "X"
            oponente = "O"
        else:
            jogador = "O"
            oponente = "X"
        resposta = input("Você quer ser X ou O?")


def __main__():
    pass

while 1:
    if velha(campo):
        imprimeCampo(campo)
        print("Velha!")
        break
    if jogador:
        imprimeCampo(campo)

        while 1:
            vc = int(input())

            if campo[vc] == '_':
                break

        campo[vc] = sVC

        jogador = 0

        if ganhou(sVC,campo):
            imprimeCampo(campo)
            print("Você ganhou!")
            break

    else:
        imprimeCampo(campo)
        while 1:
            pc = random.randint(0,8)

            if campo[pc] == '_':
                break

        campo[pc] = sPC

        jogador = 1

        if ganhou(sPC, campo):
            imprimeCampo(campo)
            print("Você perdeu!")
            break