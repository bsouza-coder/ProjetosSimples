import random

def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1, 101)
    validador_de_dificuldade = 1
    total_de_tentativas = 0
    pontos = 1000
    contador = 0
    validador_de_numero = 0


    while(validador_de_dificuldade == 1):

        validador_de_dificuldade = 0

        print("O jogo tem três niveis de dificuldade! facil(1), medio(2), dificil(3)")
        dificuldade = input("Digite o numero correspondente: ")

        if(dificuldade == "1" or dificuldade == "2" or dificuldade == "3"):
            dificuldade = int(dificuldade)

            if(dificuldade == 1):
                total_de_tentativas = 20
            elif(dificuldade == 2):
                total_de_tentativas = 10
            else:
                total_de_tentativas = 5
        else:
            print("Digite um numero válido!")
            validador_de_dificuldade = 1

    for rodada in range(1, total_de_tentativas + 1):
        print("rodada {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        chute_str = list(chute_str)
        while(contador <= len(chute_str) - 1):
            if(ord(chute_str[contador]) < 48 or ord(chute_str[contador]) > 57 ):
                validador_de_numero = 1
                break
            else:
                validador_de_numero = 0
            contador = contador + 1

        contador = 0

        if(validador_de_numero == 1):
            print("Digitou um numero invalido!")
            continue

        chute_str = ''.join(chute_str)

        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você digitou não digitou um numero entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        menor   = numero_secreto > chute
        maior   = numero_secreto < chute

        if (acertou):
            print("Você acertou!!! Você fez {} pontos!!!".format(pontos))
            break
        else:
            if(maior):
                print("VocÊ errou! Chute mais baixo!")
            elif (menor):
                print("Você errou! Chute mais alto!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        if(total_de_tentativas == rodada):
            print("Suas tentativas acabaram! O numero secreto era {} e você fez {} pontos.".format(numero_secreto, pontos))

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()