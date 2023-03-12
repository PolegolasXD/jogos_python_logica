import random

def jogar():
    
    imprimeMensagemAbertura()
    palavraSecreta = lendoArquivo()
    letrasAcertadas = inicializaLetraAcertada(palavraSecreta)

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


def imprimeMensagemAbertura():
    print("-------------------------------------")
    print("seja bem vindo ao jogo da forca")
    print("-------------------------------------")
    
def lendoArquivo():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numeroIndicePalavra = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numeroIndicePalavra].upper()
    return palavraSecreta

def inicializaLetraAcertada(palavra):
    return ["-" for letra in palavra]

    
if(__name__ == "__main__"):
    jogar()

