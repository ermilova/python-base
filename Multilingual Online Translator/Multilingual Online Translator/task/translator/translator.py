import requests
import argparse
from bs4 import BeautifulSoup
LANGUAGES = ["arabic", "german", "english", "spanish", "french",
             "hebrew", "japanese", "dutch", "polish", "portuguese",
             "romanian", "russian", "turkish"]


def get_url(lang_from, lang_to, word_):
    url_ = "https://context.reverso.net/translation/"
    url_ += get_language(lang_from)
    url_ += '-'
    url_ += get_language(lang_to)
    url_ += '/'
    url_ += word_
    return url_


def get_language(lang):
    return lang


def get_word_translations(lang, soup_, file_):
    print()
    print(get_language(lang).capitalize(), "Translations:")
    file_.write("\n" + get_language(lang).capitalize() + " Translations:\n")
    translations_html = soup_.find_all('a', {'class': 'translation'})
    for translated in translations_html:
        if 'dict' in translated["class"]:
            print(translated.text.strip())
            file_.write(translated.text.strip() + "\n")
            break


def get_examples(lang, soup_, file_):
    print()
    print(get_language(lang).capitalize(), "Examples:")
    file_.write("\n" + get_language(lang).capitalize() + " Examples:\n")
    examples_html = soup_.find_all('div', {'class': 'example'})
    for example in examples_html:
        src_example = example.find('div', {'class': 'src'})
        trg_example = example.find('div', {'class': 'trg'})
        print(src_example.text.strip())
        print(trg_example.text.strip())
        print()
        file_.write(src_example.text.strip() + "\n")
        file_.write(trg_example.text.strip() + "\n\n")
        break


def greet_user():
    global LANGUAGES
    print("Hello, you're welcome to the translator. Translator supports:")
    for i, lang in enumerate(LANGUAGES):
        print(str(i + 1) + ". " + lang)


# greet_user()
parser = argparse.ArgumentParser(description="This program translates word and gives examples")
parser.add_argument("language_from")
parser.add_argument("language_to")
parser.add_argument("word")

args = parser.parse_args()
language_to = args.language_to
language_from = args.language_from
word = args.word
if language_to not in LANGUAGES and language_to != "all":
    print(f"Sorry, the program doesn't support {language_to}")
    quit()
if language_from not in LANGUAGES:
    print(f"Sorry, the program doesn't support {language_from}")
    quit()

languages = [args.language_to]
if args.language_to == "all":
    languages = LANGUAGES


with open(word + ".txt", "w", encoding="utf-8") as file:
    for language in languages:
        url = get_url(language_from, language, word)
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == requests.codes.ok:
                soup = BeautifulSoup(response.content, 'html.parser')
                if soup.find("section", {'id': 'no-results'}):
                    file.write(f"Sorry, unable to find {word}\n")
                    print(f"Sorry, unable to find {word}")
                get_word_translations(language, soup, file)
                get_examples(language, soup, file)
            else:
                file.write(f"Sorry, unable to find {word}\n")
                print(f"Sorry, unable to find {word}")
                quit()

        except ConnectionError:
            file.write("Something wrong with your internet connection\n")
            print("Something wrong with your internet connection")
            quit()

