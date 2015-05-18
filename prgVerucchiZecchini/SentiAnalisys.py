__author__ = 'sam'

from nltk.corpus import sentiwordnet as swn
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize

def senti_analisys(tokens):
    print tokens
    for token,part in tokens:
        if swn.senti_synsets(token) != []:
            l = list(swn.senti_synsets(token))
            


            """
            try:
                prova = lesk(tokens, token, 'a').name()
                print swn.senti_synset(prova)
            except AttributeError:
                try:
                    prova = lesk(tokens, token, 'n').name()
                    print swn.senti_synset(prova)
                except AttributeError:
                    try:
                        prova = lesk(tokens, token, 'v').name()
                        print swn.senti_synset(prova)
                    except AttributeError:
                        try:
                            prova = lesk(tokens, token, 'r').name()
                            print swn.senti_synset(prova)
                        except AttributeError:
                            print "no a,n,v,r"
            """


