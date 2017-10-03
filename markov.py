import sys
import random


def analyze_text(source, table):
    nonword = '\n'
    w1 = nonword
    w2 = nonword

    words = source.split()

    for word in words:
        word = word.lower()
        table.setdefault( (w1, w2) , [] ).append(word)
        w1, w2 = w2, word

    table.setdefault((w1, w1), []).append(nonword)

    return table

# GENERATE OUTPUT
def generate_output(table, maxwords):
    nonword = '\n'
    w1 = nonword
    w2 = nonword

    sentence = ''

    for i in range(0, maxwords):
        new_word = random.choice(table[ (w1,w2)] )
        if new_word == nonword:
            print( sentence )
            input()
            sys.exit()

        sentence += ' %s' % new_word

        if not ( new_word[-1].isalpha() ):
            print(sentence)
            sentence = ''

        w1, w2 = w2, new_word

if __name__ == '__main__':
    table = {}

    source = (open('text.txt')).read()

    analyze_text(source, table)
    generate_output(table, 200)
