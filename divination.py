import random

def play():
    print("**********************************************************")
    print("          ", "Hello welcome, let's start the game!")
    print("**********************************************************")

    # One line docstring

    """
    Multi line docstring
    """

    secret_number = random.randrange(1, 101)
    print(secret_number)
    total_chance = 0
    points = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    
    level = int(input("Define o nível: "))
    
    if (level == 1):
        total_chance = 20
    elif (level == 2):
        total_chance = 10
    else:
        total_chance = 5
    
    
    for round in range(1, total_chance + 1):
        print("Tentativa {} de {}".format(round, total_chance))
        hunch = input("Digite um número entre 1 e 100: ")
        print("Você digitou", hunch)
        hunch = int(hunch)
    
        if(hunch < 1 or hunch > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        hit = hunch == secret_number
        greater = hunch > secret_number
        less = hunch < secret_number
    
        if (hit):
            print("Parabéns, você acertou e fez {} pontos!".format(points))
            break
        else:
            if (greater):
                print("Você errou! O seu número foi maior que o número secreto")
            elif (less):
                print("Você errou! O seu número foi menor que o número secreto")
            lost_points =  abs(secret_number - hunch)
            points = points - lost_points
    
    print("Fim do jogo!")

if(__name__ == '__main__'):
    play()