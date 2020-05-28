import hangman
import divination

def choose_game():
    print("**********************************************************")
    print("          ", "Welcome, choose your game!")
    print("**********************************************************")

    print("(1) Forca (2) Adivinhação")

    game = int(input("Qual jogo? "))

    if (game == 1):
        print("Jogando forca")
        hangman.play()
    elif (game == 2):
        print("Jogando adivinhação")
        divination.play()

if(__name__ == "__main__"):
    choose_game()

