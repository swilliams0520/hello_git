import re
import string
import sys
from collections import OrderedDict



STRIP_PUNCT = str()
for i in string.punctuation:
    STRIP_PUNCT += "\\" + i + "|"


def quantify_words(text_file):
    word_count = dict()
    with open(text_file, "r") as f:
        words = f.read().casefold()
        clean = re.split(r' |\n', words)
        for word in clean:
            if word.isspace() or word == '':
                continue
            word = re.sub(STRIP_PUNCT, '', word)
            word_count[word] = word_count.get(word, 0) + 1    #assigns new value to dictionary

    word_count = OrderedDict(sorted(word_count.items(), key=lambda t: t[1])) #function that has no name, but is built in so python knows it
    for k,v in list(reversed(word_count.items()))[:10]:
        print(k,v)

if len(sys.argv) == 2:
    text_file = sys.argv[1]
    quantify_words(text_file)
else:
    print("usage: quantify.py TEXT FILE")
