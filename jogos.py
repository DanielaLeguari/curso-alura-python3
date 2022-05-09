import jogo_forca
import jogo_adivinhacao

def escolha_jogo():
    print("*********************************")
    print("******Escolha o seu Jogo!*******")
    print("*********************************")

    print("(1) Forca  (2) Adivinhação")

    jogo = int(input("Qual jogo?"))
    if (jogo == 1):
        print("Jogando Forca")
        jogo_forca.jogar_forca()  #chama uma função
    elif(jogo == 2):
        print("Jogando Adivinhação")
        jogo_adivinhacao.jogar_adivinhacao()


if (__name__== "__main__"):   #criação de arquivo principal
    escolha_jogo()

