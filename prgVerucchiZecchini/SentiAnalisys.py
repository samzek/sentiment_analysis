__author__ = 'sam'

from nltk.corpus import sentiwordnet as swn
from Preprocessing import  Preprocess

#Vedi documento proposto dai prof per calcolo score
def senti_analisys(tokens):
    #print tokens
    scorePosTot = 0
    scoreNegTot = 0
    scoreObjTot = 0
    scoreObjNorm = scoreNegNorm = scorePosNorm = 0
    count = 0
    for token,part in tokens:

        if part.startswith("JJ") or part.startswith("NN") or part.startswith("VB"):

            scorePos = 0
            scoreNeg = 0
            scoreObj = 0
            #print swn.senti_synsets(token)
            #if token == "wonderful":
             #   print "i'm "+token,swn.senti_synsets(token)
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

                #print "The token is: "+token + "\n\tscore pos: "+str(round(scorePos,2)) + "\n\tscore neg: "+str(round(scoreNeg,2))+\
                      #"\n\tscore obj: " + str(round(scoreObj,2))


                scorePosTot += scorePos
                scoreNegTot += scoreNeg
                scoreObjTot += scoreObj
            count += 1

    #if count != 0:
    scorePosNorm = scorePosTot / count
    scoreNegNorm = scoreNegTot / count
    scoreObjNorm = scoreObjTot / count

    #print "NORM: "+ "\n\tscorePOS: "+str(round(scorePosNorm,2)) + "\n\tscoreNEG: "+str(round(scoreNegNorm,2)) \
          #+ "\n\tscoreOBJ: "+str(round(scoreObjNorm,2))
    if scoreNegNorm < scorePosNorm :
        #print "POSITIVE"
        return 1,scorePosNorm
    elif scoreNegNorm > scorePosNorm:
        #print "NEGATIVE"
        return -1,-scoreNegNorm
    else:
        #print "OBJECTIVE"
        return 0,0
    #print "tweet value:",scorePosNorm,scoreNegNorm,scoreObjNorm

if __name__ == '__main__':

    """
    sentence = "we can bring the Gospel to others if it deeply permeates our lives"
    tokens,tokens_stemmed = Preprocess(sentence)

    print "SENTENCE: "+sentence
    print "VALUE NOSTEMM **"
    tweetValue,moodValue = senti_analisys(tokens)
    print "*********\nVALUE STEMM"
    tweetValueS,moodValue = senti_analisys(tokens_stemmed)
    print "*********"

    sentence = "during Lent, we find concrete ways to overcome our indifference."
    tokens,tokens_stemmed = Preprocess(sentence)

    print "SENTENCE: "+sentence
    print "VALUE NOSTEMM **"
    tweetValue,moodValue = senti_analisys(tokens)
    print "*********\nVALUE STEMM"
    tweetValueS,moodValue = senti_analisys(tokens_stemmed)
    print "*********"

    sentence = "god awaits us always, always understand us,always forgives us"
    tokens,tokens_stemmed = Preprocess(sentence)

    print "SENTENCE: "+sentence
    print "VALUE NOSTEMM **"
    tweetValue,moodValue = senti_analisys(tokens)
    print "*********\nVALUE STEMM"
    tweetValueS,moodValue = senti_analisys(tokens_stemmed)
    print "*********"

    sentence = "christ is risen! Christ is alive and he walks with us!"
    tokens,tokens_stemmed = Preprocess(sentence)

    print "SENTENCE: "+sentence
    print "VALUE NOSTEMM **"
    tweetValue,moodValue = senti_analisys(tokens)
    print "*********\nVALUE STEMM"
    tweetValueS,moodValue = senti_analisys(tokens_stemmed)
    print "*********"
    """
    sentence = "Jesus came to save us: we do not reject this wonderful gift"
    tokens,tokens_stemmed = Preprocess(sentence)

    print "SENTENCE: "+sentence
    print "VALUE NOSTEMM **"
    tweetValue,moodValue = senti_analisys(tokens)
    print "*********\nVALUE STEMM"
    tweetValueS,moodValue = senti_analisys(tokens_stemmed)
    print "*********"