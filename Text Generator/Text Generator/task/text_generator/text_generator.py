from collections import defaultdict
import random
import re
START = r"^[A-Z].*[^\.!\?]$"
END = r".*[\.!\?]$"


def get_next(word_dict):
    return random.choices(population=list(word_dict.keys()),
                          weights=list(word_dict.values()))[0]


def generate_sentence(next_word, markov_dict):
    sentence = next_word
    sentence_len = 2
    while True:
        word = get_next(markov_dict[next_word])
        sentence += " " + word
        sentence_len += 1
        if re.match(END, word) and sentence_len >= 5:
            break
        next_word = next_word.split()[1] + " " + word
    return sentence


file_name = input()
with open(file_name, "r", encoding="utf-8") as f:
    text = []
    line = f.readline()
    while line:
        text += line.split()
        line = f.readline()

    text = [(text[i - 2] + " " + text[i - 1], text[i])
            for i in range(2, len(text))]
    start_words = [x for x, y in text if re.match(START, x.split()[0])]

    markov = defaultdict(dict)
    for head, tail in text:
        markov[head].setdefault(tail, 0)
        markov[head][tail] += 1

    for _ in range(0, 10):
        print(generate_sentence(random.choice(start_words), markov))

