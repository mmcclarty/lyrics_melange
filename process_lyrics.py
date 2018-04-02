import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

def read_words(words_file):
    rap_lyrics = [word for line in open(words_file, 'r') for word in line.split()]
    return rap_lyrics

rap_lyrics = read_words('text.txt')
print(rap_lyrics)
#example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))
#word_tokens = wordpunct_tokenize(rap_lyrics)

filtered_lyrics = [w for w in rap_lyrics if not w in stop_words]

filtered_lyrics = []

for w in rap_lyrics:
    if w not in stop_words:
        filtered_lyrics.append(w)

#print(word_tokens)
print(filtered_lyrics)