def jogar():
    print("-------------------------------------")
    print("seja bem vindo ao jogo da forca")
    print("-------------------------------------\n")

    palavraSecreta = "batata"
    
    letrasAcertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letrasAcertadas)
    while(not enforcou and not acertou):

        chute = input("Escolha uma letra: " )
        chute = chute.strip()

        index = 0

        for letra in palavraSecreta:
            if(chute.upper() == letra.upper()):
                letrasAcertadas[index] = letra
            index = index + 1

        print(letrasAcertadas)

    print("fim de jogo")
    
if(__name__ == "__main__"):
    jogar()

