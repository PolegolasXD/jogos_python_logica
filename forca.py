import random

def jogar():
    print("-------------------------------------")
    print("seja bem vindo ao jogo da forca")
    print("-------------------------------------")


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numeroIndicePalavra = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numeroIndicePalavra].upper()

    letrasAcertadas = ["-" for letra in palavraSecreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print("\n", letrasAcertadas, "\n")

    while(not enforcou and not acertou):

        chute = input("Escolha uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavraSecreta):
            index = 0

            for letra in palavraSecreta:
                if(chute == letra):
                    letrasAcertadas[index] = letra
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6

        acertou = "-" not in letrasAcertadas
        print("\n", letrasAcertadas, "\n")


    if(acertou):
        print("\nvocê ganhou!\n")
    else:
        print("você perdeu!\n")

    print("fim de jogo")
    
if(__name__ == "__main__"):
    jogar()

