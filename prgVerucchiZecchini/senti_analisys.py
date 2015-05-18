__author__ = 'sam'

from nltk.corpus import sentiwordnet as swn
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize

def sennti_analisys():
    tweetB = "When it comes to a woman's health, no politician should get to decide what's best for you"
    print "English tweet ",tweetB
    sent = word_tokenize(tweetB)
    prova = lesk(sent, 'health', 'n').name()
    print swn.senti_synset(prova)