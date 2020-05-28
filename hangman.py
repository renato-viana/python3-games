def play():
    print("**********************************************************")
    print("          ", "Hello welcome, let's start the game!")
    print("**********************************************************")
    print("Fim do jogo!")

    secret_word = "banana"
    found_letters = ["_", "_", "_", "_", "_", "_"]
    missing_letters = str(found_letters.count('_'))
    print('Ainda faltam acertar {} letras'.format(missing_letters))

    hanged = False
    hit = False

    print(found_letters)

    index = 0
    while (not hanged and not hit):

        # String é imutável funções do tipo str geram uma nova string
        hunch = input("Qual letra?").strip()

        index = 0
        for letter in secret_word:
            if (hunch.lower() == letter.lower()):
                found_letters[index] = letter
            index = index + 1

        print(found_letters)

print("Fim do jogo!")


if (__name__ == "__main__"):
    play()
