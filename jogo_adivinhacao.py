import random  # 0.0 até 1.0

def jogar_adivinhacao():
    print("*********************************")
    print("Bem-vindo ao Jogo de adivinhação!")
    print("*********************************")

    # numero_secreto = 42  # numero fixo
    # numero_secreto = round(random.random() * 100) # para sair do decimal e gerar um número maior, porem ainda decimal.
    # função round é uma função já embutida no python para arredondar decimais, porém pode dar errado se gerar 0.
    numero_secreto = random.randrange(1, 101)  # essa função seria a mais correta, gerando um nº aleatório.
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")  # de acordo com a dificuldade, um total de rodadas.
    nivel = int(input("Define o nível.:"))  # variável intermediária
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):  # range(start, stop, [step])
        print("Tentativa {} de {}".format(rodada, total_tentativas))  # String interpolation
        chute_str = input("Digite um número entre 1 e 100.:")  # uso da função int
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # sair dessa iteração, e continua o laço na proxima iteração

        acertou = chute == numero_secreto  # condições
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):  # estou testando um número int com str, isso dá False, preciso converter
            print("Você acertou e fez {} pontos!".format(pontos))
            break  # sair do laço se voce acertou.
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(
                numero_secreto - chute)  # 40 - 20 = 20 pontos perdidos, abs: gera um valor absoluto sem considerar o sinal -
            pontos = pontos - pontos_perdidos
    print("Fim de jogo")
# fora da função
if (__name__== "__main__"):
    jogar_adivinhacao()
