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

rap_lyrics = read_words('text.txt')
print(rap_lyrics)

stop_words = set(stopwords.words('english'))

filtered_lyrics = [w.lower() for w in rap_lyrics if not w in stop_words]
filtered_lyrics = []
for w in rap_lyrics:
    if w.lower() not in stop_words:
        filtered_lyrics.append(w.lower())

no_punc = [s.translate(None, string.punctuation) for s in filtered_lyrics]

english_swears = swear_words('en')
french_swears = swear_words('fr')
print(english_swears)
print(french_swears)

english_rap_swears = [w for w in no_punc if w in english_swears]

en_swear_dict = {}
for word in english_rap_swears:
  en_swear_dict[word] = en_swear_dict.get(word, 0) + 1

print(en_swear_dict)