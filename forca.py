
def jogar():

    print("-------------------------------------")
    print("seja bem vindo ao jogo da forca")
    print("-------------------------------------\n")

    palavraSecreta = "batata"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual a letra escolhida: ")
        index = 0
        for letra in palavraSecreta:
            if(chute == letra):
                print(f"Encontrei a letra '{chute}' na posição '{index}'")
            index = index + 1

        print("jogando ...")

    print("fim de jogo")
    
if(__name__ == "__main__"):
    jogar()