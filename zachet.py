from collections import Counter
from string import punctuation


input_text = open("Kotu.txt", encoding="utf-8").read().lower()
dictionary = dict(
    Counter(
        input_text.translate(str.maketrans("", "", punctuation)).split()
    ).most_common()
)
word = sorted(dictionary)
number_of = [value for (key, value) in sorted(dictionary.items())]
a = list(zip(word, number_of))
for i in a:
    print("Слово '{0[0]}' встречается {0[1]} раз(а)".format(i))
