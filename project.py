from project_dictionary import *

sentence = ""
KEYWORD = "хвост"


def find_word_meaning(input_sentence: str) -> str:
    for word_input_sent in input_sentence:
        for meaning in dictionary:
            keyword_index = input_sentence.index(KEYWORD)
            description_word_index = input_sentence.index(word_input_sent)
            if word_input_sent in dictionary[meaning]["right"]:
                if keyword_index - description_word_index in range(-5, 5):
                    return (
                        f"\nСлово 'хвост' использовано в следующем значении: {meaning}."
                    )
            elif word_input_sent in dictionary[meaning]["left"]:
                if keyword_index - description_word_index in range(-5, 5):
                    return (
                        f"\nСлово 'хвост' использовано в следующем значении: {meaning}."
                    )


def main():
    print(find_word_meaning(sentence))


while sentence != "*":
    sentence = input(
        "(Чтобы выйти, введите '*' или нажмите 'CTRL+C')\nВведите Ваше п-жение с словом 'хвост': \n"
    ).lower()
    if sentence == "*":
        print("Выход из программы...")
        break
    sentence = (
        sentence.replace(".", "")
        .replace(",", "")
        .replace("хвосты", "хвост")
        .replace("хвостами", "хвост")
        .replace("хвосты", "хвост")
        .replace("хвоста", "хвост")
        .replace("хвосту", "хвост")
        .replace("хвостом", "хвост")
        .replace("хвосте", "хвост")
        .replace("хвостов", "хвост")
        .replace("хвостам", "хвост")
        .replace("хвостами", "хвост")
        .replace("хвостах", "хвост")
        .replace("ё", "е")
        .split(" ")
    )

    if KEYWORD not in sentence:
        print("'Хвост' не обнаружен ¯\_(ツ)_/¯")
        continue

    if __name__ == "__main__":
        main()
