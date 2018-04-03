import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize


def read_words(words_file):
    into_words = [word for line in open(words_file, 'r') for word in line.split()]
    return into_words


def swear_words(swear_file):
    swear_words = [line.rstrip() for line in open(swear_file, 'r')]
    return swear_words


def filter_lyrics(rap_lyrics, stop_words):
    filtered_lyrics = [w.lower() for w in rap_lyrics if not w in stop_words]
    filtered_lyrics = []
    for w in rap_lyrics:
        if w.lower() not in stop_words:
            filtered_lyrics.append(w.lower())

    no_punc = [s.translate(None, string.punctuation) for s in filtered_lyrics]

    return no_punc


def filter_swears(filtered, swear_list):
    rap_swears = [w for w in filtered if w in swear_list]

    swear_dict = {}
    for word in rap_swears:
        swear_dict[word] = swear_dict.get(word, 0) + 1

    return swear_dict


def main():
    en_rap_lyrics = read_words('EN.txt')
    fr_rap_lyrics = read_words('FR.txt')

    en_stop_words = set(stopwords.words('english'))
    fr_stop_words = set(stopwords.words('french'))
    english_swears = swear_words('en')
    french_swears = swear_words('fr')

    en_filtered = filter_lyrics(en_rap_lyrics, en_stop_words)
    fr_filtered = filter_lyrics(fr_rap_lyrics, fr_stop_words)

    en_swear_dict = filter_swears(en_filtered, english_swears)
    fr_swear_dict = filter_swears(fr_filtered, french_swears)

    print(en_swear_dict)
    print(fr_swear_dict)


main()



