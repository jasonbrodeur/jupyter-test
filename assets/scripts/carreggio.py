import nltk
nltk.download('stopwords')
import spacy
import sys
import contextualSpellCheck
import os

path = "C:\\Local\\jupyter-test\\assets\\scripts\\careggio-raw.txt"

with open(path) as f:
    text = f.read()

print(text)

nlp = spacy.load('en_core_web_md')


contextualSpellCheck.add_to_pipe(nlp)




## Stopwords
from nltk.corpus import stopwords
stopwords = stopwords.words('english') # making an easier-to-work-with list from the NLTK stopwords

from string import punctuation
punctuation = list(punctuation) # making a list again, as above

print(f"Stopwords: \n {stopwords}")

print()

print(f"Punctuation: \n {punctuation}")

