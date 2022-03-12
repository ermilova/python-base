import random

options = ["rock", "paper",  "scissors"]


def game(user_chose, user_rating):
    global options
    computer_chose = random.choice(options)
    index = options.index(user_chose)
    wins = options[index + 1:] + options[:index]
    wins = wins[:len(wins) // 2]
    if computer_chose in wins:
        print('Sorry, but the computer chose', computer_chose)
        return user_rating
    elif computer_chose == user_chose:
        print(f'There is a draw ({user_chose})')
        return user_rating + 50
    else:
        print(f'Well done. The computer chose {computer_chose} and failed')
        return user_rating + 100


if __name__ == "__main__":
    rate = 0
    name = input("Enter your name: ")
    print("Hello,", name)
    with open("rating.txt", 'r', encoding='utf-8') as file:
        for line in file:
            user_name, user_rate = line.strip(' \n').split()
            user_rate = int(user_rate)
            if name == user_name:
                rate = user_rate

    rules = input()
    if rules != "":
        options = rules.split(",")

    print("Okay, let's start")
    while True:
        chose = input()
        if chose == "!rating":
            print(f'Your rating: {rate}')
            continue
        elif chose == "!exit":
            break
        elif chose not in options:
            print("Invalid input")
            continue
        rate = game(chose, rate)
    print("Bue!")
