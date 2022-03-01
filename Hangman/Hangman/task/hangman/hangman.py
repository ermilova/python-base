import random
dictionary = ('python', 'java', 'kotlin', 'javascript')
print("H A N G M A N")


def hangman():
    answer = dictionary[random.randint(0, 3)]
    set_letters = set(answer)
    guessed = set()
    progress = list("-" * len(answer))
    lives = 8
    while lives > 0:
        print("\n" + "".join(progress))
        letter = input("Input a letter: ")
        if letter == "exit":
            return True
        if len(letter) > 1:
            print("You should input a single letter")
            continue

        if not letter.isalpha() or not letter.islower():
            print("Please enter a lowercase English letter")
            continue

        if letter in guessed:
            print("You've already guessed this letter")
            continue

        if letter not in set_letters:
            print("That letter doesn't appear in the word")
            guessed.add(letter)
            lives -= 1
            continue

        for i in range(0, len(answer)):
            if letter == answer[i]:
                progress[i] = letter
        guessed.add(letter)
        if "".join(progress) == answer:
            break

    if "".join(progress) == answer:
        print("\n" + "".join(progress))
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")
    return False


while True:
    play = False
    while not play:
        action = input('Type "play" to play the game, "exit" to quit: ')
        if action == 'exit':
            quit()
        if action == 'play':
            play = True
    if hangman():
        break

