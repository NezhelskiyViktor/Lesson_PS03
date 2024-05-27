from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        ru_word = Translator().translate(word, src="en", dest="ru").text
        word_definition = word_dict.get("word_definition")
        ru_definition = Translator().translate(word_definition, src="en", dest="ru").text

        print(f"Значение слова - {word_definition}\n({ru_definition})")
        user = input("Что это за слово? ")
        if user == word:
            print(f"Верно, это слово - {ru_word} {word}")
        else:
            print(f"Ответ неверный, было загадано слово - {word} ({ru_word})")

        play_again = input("Хотите сыграть еще раз? y/n  ")
        if play_again == "y":
            print("Продолжим...\n")
        else:
            print("Спасибо за игру!")
            break


word_game()
