#-*- coding: utf-8 -*-

from detect_language import get_language
from nltk.corpus import sentiwordnet as swn
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize

def main():
    tweetB = "When it comes to a woman's health, no politician should get to decide what's best for you"
    print "English tweet ",tweetB
    sent = word_tokenize(tweetB)

    prova = lesk(sent, 'health', 'n').name()

    print swn.senti_synset(prova)

   # breakd = swn.senti_synset('slow.a.02')
   # print breakd
if __name__ == '__main__':
    main()