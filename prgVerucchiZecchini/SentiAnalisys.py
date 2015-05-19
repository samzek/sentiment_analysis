__author__ = 'sam'

from nltk.corpus import sentiwordnet as swn
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize

#Vedi documento proposto dai prof per calcolo score
def senti_analisys(tokens):
    print tokens
    scorePosTot = 0
    scoreNegTot = 0
    scoreObjTot = 0
    count = 0
    for token,part in tokens:
        scorePos = 0
        scoreNeg = 0
        scoreObj = 0
        if swn.senti_synsets(token) != []:
            list_synset = list(swn.senti_synsets(token))
            dim_synset = list_synset.__len__()

            for i in list_synset:
                scorePos += i.pos_score()
                scoreNeg += i.neg_score()
                scoreObj += i.obj_score()

            scorePos = scorePos / dim_synset
            scoreNeg = scoreNeg / dim_synset
            scoreObj = scoreObj / dim_synset

            print token,scorePos,scoreNeg,scoreObj

            scorePosTot += scorePos
            scoreNegTot += scoreNeg
            scoreObjTot += scoreObj
        count += 1

    scorePosNorm = scorePosTot / count
    scoreNegNorm = scoreNegTot / count
    scoreObjNorm = scoreObjTot / count

    if scoreNegNorm < scorePosNorm :
        print "tweet value: POSITIVE"
    elif scoreNegNorm > scorePosNorm:
        print "tweet value: NEGATIVE"
    else:
        print "tweet value: OBJECTIVE"
    #print "tweet value:",scorePosNorm,scoreNegNorm,scoreObjNorm

