def jogar():
    print("-------------------------------------")
    print("seja bem vindo ao jogo da forca")
    print("-------------------------------------\n")

    palavraSecreta = "batata"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Escolha uma letra: " + "\n" )
        chute = chute.strip()
        index = 0

        for letra in palavraSecreta:
            if(chute.upper() == letra.upper()):
                print(f"Encontrei a letra {chute} na posição {index}\n")
            index = index + 1

        print("jogando ...")

    print("fim de jogo")
    
if(__name__ == "__main__"):
    jogar()

