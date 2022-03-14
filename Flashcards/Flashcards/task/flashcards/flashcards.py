import random
from collections import defaultdict
import io
import argparse


class Flashcards:
    def __init__(self):
        self.cards = {}
        self.terms = set()
        self.definitions_dict = {}
        self.definitions = set()
        self.mistakes = defaultdict(int)

    def play(self):
        while True:
            action = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
            output.write("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
            output.write(action + '\n')
            if action == 'import':
                self.import_cards()
            else:
                getattr(self, action.replace(' ', '_'))()

    def add(self):
        term = input("The card:\n")
        output.write("The card:\n")
        output.write(term + '\n')
        while term in self.terms:
            print(f'The term "{term}" already exists. Try again:')
            term = input()
            output.write(f'The term "{term}" already exists. Try again:\n')
            output.write(term + '\n')
        self.terms.add(term)
        definition = input("The definition of the card:\n")
        output.write("The definition of the card:\n")
        output.write(definition + '\n')

        while definition in self.definitions:
            print(f'The definition "{definition}" already exists. Try again:')
            definition = input()
            output.write(f'The definition "{definition}" already exists. Try again:\n')
            output.write(definition + '\n')
        self.definitions.add(definition)
        self.definitions_dict[definition] = term
        self.cards[term] = definition
        print(f'The pair ("{term}":"{definition}") has been added.')
        output.write(f'The pair ("{term}":"{definition}") has been added.\n')

    def remove(self):
        card = input("Which card?\n")
        output.write("Which card?\n")
        output.write(card + "\n")
        if card in self.terms:
            self.terms.remove(card)
            self.definitions.remove(self.cards[card])
            self.definitions_dict.pop(self.cards[card])
            self.cards.pop(card)
            print("The card has been removed.")
            output.write("The card has been removed.\n")
        else:
            print(f'Can\'t remove "{card}": there is no such card.')
            output.write(f'Can\'t remove "{card}": there is no such card.\n')

    def exit(self):
        if args.export_to:
            self.export(args.export_to)
        print("Bye bye!")
        quit()

    def export(self, file_name=None):
        if file_name is None:
            file_name = input("File name:\n")
            output.write("File name:\n")
            output.write(file_name + "\n")
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                for term in self.cards:
                    print(term, file=file, end='\n')
                    print(self.cards[term], file=file, end='\n')
                print(f'{len(self.cards)} cards have been saved.')
                output.write(f'{len(self.cards)} cards have been saved.\n')
        except EnvironmentError:
            print("File not found.")
            output.write("File not found.\n")

    def import_cards(self, file_name=None):
        if file_name is None:
            file_name = input("File name:\n")
            output.write("File name:\n")
            output.write(file_name + "\n")
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                n = 0
                line = file.readline()

                while line:
                    term = line.rstrip('\n')
                    definition = file.readline().rstrip('\n')
                    self.terms.add(term)
                    self.definitions.add(definition)
                    self.definitions_dict[definition] = term
                    self.cards[term] = definition
                    n += 1
                    line = file.readline()
                print(f'{n} cards have been loaded.')
                output.write(f'{n} cards have been loaded.\n')
        except EnvironmentError:
            print("File not found.")
            output.write("File not found.\n")

    def ask(self):
        n = int(input("How many times to ask?\n"))
        output.write("How many times to ask?\n")
        output.write(str(n) + "\n")
        for _ in range(0, n):
            term_q = random.choice(list(self.terms))
            print(f'Print the definition of "{term_q}":')
            output.write(f'Print the definition of "{term_q}":\n')
            answer = input()
            output.write(answer + "\n")
            if answer == self.cards[term_q]:
                print("Correct!")
                output.write("Correct!\n")
            elif answer in self.definitions:
                print(f'Wrong. The right answer is "{self.cards[term_q]}",'
                      f' but your definition is correct for "{self.definitions_dict[answer]}".')
                output.write(f'Wrong. The right answer is "{self.cards[term_q]}",'
                      f' but your definition is correct for "{self.definitions_dict[answer]}".\n')
                self.mistakes[term_q] += 1
            else:
                print(f'Wrong. The right answer is "{self.cards[term_q]}".')
                output.write(f'Wrong. The right answer is "{self.cards[term_q]}".\n')
                self.mistakes[term_q] += 1

    def hardest_card(self):
        if not len(self.mistakes):
            print("There are no cards with errors.")
            output.write("There are no cards with errors.\n")
            return
        max_mistake = max(self.mistakes.values())
        common_mistakes = [term for term in self.mistakes
                           if self.mistakes[term] == max_mistake]
        if len(common_mistakes) == 1:
            print(f'The hardest card is "{common_mistakes[0]}".')
            output.write(f'The hardest card is "{common_mistakes[0]}".\n')
        else:
            print('The hardest cards are ', end="")
            output.write('The hardest cards are ')
            res = ""
            for mistake in common_mistakes:
                res += f'"{mistake}"' + ", "
            res.rstrip(", ")
            print(res)
            output.write(res + '\n')
        print(f"You have {max_mistake} errors answering it")
        output.write(f"You have {max_mistake} errors answering it\n")

    def reset_stats(self):
        self.mistakes = defaultdict(int)
        print("Card statistics have been reset.")
        output.write("Card statistics have been reset.\n")

    def log(self):
        file_name = input("File name:\n")
        output.write("File name:\n")
        output.write(file_name + "\n")
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(output.getvalue())
            print("The log has been saved.")
            output.write("The log has been saved.\n")
        except EnvironmentError:
            print("File not found.")
            output.write("File not found.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program let you guess some flashcards")
    parser.add_argument("--import_from")
    parser.add_argument("--export_to")
    args = parser.parse_args()

    game = Flashcards()
    output = io.StringIO()
    if args.import_from:
        game.import_cards(args.import_from)

    game.play()
    output.close()


