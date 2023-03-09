import forca
import adivinhacao


print("-------------------------------------")
print("---------Escolha o seu jogo!---------")
print("-------------------------------------")

print("(1)forca (2)adivinhacao")
jogo = int(input("Qual jogo voce quer jogar: "))


if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
