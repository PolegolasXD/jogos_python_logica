import random
def jogar():
    print("-------------------------------------")
    print("seja bem vindo ao jogo de Adivinhação")
    print("-------------------------------------")
    numeroSecreto = random.randint(1, 100)
    totalDeTentativas = 0
    pontos = 1000;

    nivel = int(input(" Escolha o nivel para jogar entre: (1)facil (2)medio (3) dificil)! "))

    while True:
        if(nivel <= 3 or None):
            pass
        else:
            nivel = int(input("voce digitou um numero nao listado! tente novamente (1)facil (2)medio (3) dificil)! "))

        if(nivel == 1):
                 totalDeTentativas = 10
        elif(nivel == 2):
                totalDeTentativas = 5
        elif(nivel == 3):
                totalDeTentativas = 3


        for rodada in range(1, totalDeTentativas + 1):
            print("\nTentativa {} de {}".format(rodada, totalDeTentativas))
            print(f"pontos atuais {pontos}")
            chute_str = input("\nDigite o seu número entre 1 e 100: ")

            print(f"Você digitou {chute_str}")
            chute = int(chute_str)


            if(chute < 1 or chute > 100 ):
                print("O numero entre 1 e 100 é obrigatorio!")
                continue

            acertou = numeroSecreto == chute
            chuteMaior = chute > numeroSecreto
            chuteMenor = chute < numeroSecreto

            if(acertou):
                print(f"voce acertou! o numero secreto era >>>{numeroSecreto}<<< parabens seus pontos foram{pontos}")
                break
            else:
                if (chuteMaior):
                  print("voce errou!! o seu chute foi maior que o numero secreto\n")
                  pontosPerdidos = abs(numeroSecreto - chute)
                  pontos = pontos - pontosPerdidos * 2
                elif (chuteMenor):
                    print("voce errou!! o seu chute foi menor que o numero secreto\n")
                    pontosPerdidos = abs(numeroSecreto - chute)
                    pontos = pontos - pontosPerdidos * 2
        if nivel == totalDeTentativas:
            break


    print("fim do jogo\n")
    print("O numero secreto era >>>{}<<<".format(numeroSecreto))
    print(f"seus pontos foram {pontos}")
jogar()
