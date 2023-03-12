import random


def jogar():
    imprimeMensagemAbertura()
    palavraSecreta = carregaPalavraSecreta()

    letrasAcertadas = inicializaLetrasAcertadas(palavraSecreta)
    print(letrasAcertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = chamaChute()

        if(chute in palavraSecreta):
            marcaLetraCorretaDoChuteCerto(chute, letrasAcertadas, palavraSecreta)
        else:
            erros += 1
            desenhaForca(erros)

        enforcou = erros == 7
        acertou = "_" not in letrasAcertadas

        print(letrasAcertadas)

    if(acertou):
        imprimeMensagemVencedor()
    else:
        imprimeMensagemPerdedor(palavraSecreta)


def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprimeMensagemVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprimeMensagemPerdedor(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marcaLetraCorretaDoChuteCerto(chute, letrasAcertadas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):
            letrasAcertadas[index] = letra
        index += 1

def chamaChute():
    chute = input("\nQual letra? ")
    chute = chute.strip().upper()
    return chute

def inicializaLetrasAcertadas(palavra):
    return ["_" for letra in palavra]

def imprimeMensagemAbertura():
    print("----------------------------------")
    print("---Bem vindo ao jogo da Forca!---")
    print("----------------------------------")

def carregaPalavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta


if(__name__ == "__main__"):
    jogar()
