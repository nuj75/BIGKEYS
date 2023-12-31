from nltk.corpus import brown
from nltk.tokenize import word_tokenize

import pickle
import json

import nltk
nltk.download('brown')






        
def associate_pair(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

new_dictionary(5)
