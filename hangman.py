import random


def play():

    welcome_message()

    secret_word = random_word()

    found_letters = word_length(secret_word)

    hanged = False
    hit = False
    errors = 0

    print(found_letters)

    index = 0
    while (not hanged and not hit):

        # String é imutável funções do tipo str geram uma nova string
        hunch = input("Qual letra?").strip().upper()

        if (hunch in secret_word):
            fill_word_letters(hunch, secret_word, found_letters)
        else:
            errors += 1
            draw_hangman(errors)

        hanged = errors == 7
        hit = '_' not in found_letters
        print(found_letters)

    end_of_game(hit, secret_word)


def welcome_message():
    print("**********************************************************")
    print("          ", "Hello welcome, let's start the game!")
    print("**********************************************************")


def random_word(file_name='b'):
    with open(file_name) as file:
        words = []
        for line in file:
            line = line.strip()
            words.append(line)

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()

    return secret_word


def word_length(secret_word):
    # List Comprehensions
    return ['_' for letter in secret_word]


def fill_word_letters(hunch, secret_word, found_letters):
    index = 0
    for letter in secret_word:
        if (hunch == letter):
            found_letters[index] = letter
        index = index + 1

def end_of_game(hit, secret_word):
    if (hit):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(secret_word))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    print("Fim do jogo!")

def draw_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    play()
