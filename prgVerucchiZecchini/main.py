#-*- coding: utf-8 -*-

import goslate;
from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys
from GetTweet import returnTweets,returnMood


def check(tweetValue,docAtt,totdoc,realValue,t,f):
    #if tweetValue == t and tweetValue == realValue:
    #    docAtt+=1
    #    totdoc+=1
    #elif tweetValue == f and tweetValue != realValue:
    #    totdoc += 1

    if tweetValue == t :
        docAtt+=1
        if tweetValue == realValue:
            totdoc += 1

    return  docAtt, totdoc

def calc_precision_recall(docatt,totdoc,totdocatt):
    #Precision: numero di documenti attinenti trovati / totale documenti recuperati
    #precision = docatt / float(totdoc) * 100
    precision = totdoc / float(docatt) *100
    print "\tPRECISION: ", precision,"%"
    #Recall: numero di documenti attinenti trovati / totale documenti attinenti esistenti
    #recall = docatt / float(totdocatt) * 100
    recall = totdoc / float(totdocatt) *100
    print "\tRECALL", recall,"%"

def main():
    docAttPos = 0 #recuperati
    totdocPos = 0 #intersezione
    totdocAttPos = 5 #attinenti

    docAttNeg = 0
    totdocNeg = 0
    totdocAttNeg = 3

    docAttPosS = 0
    totdocPosS = 0
    totdocAttPosS = 5

    docAttNegS = 0
    totdocNegS = 0
    totdocAttNegS = 3

    count = 0
    tweets = returnTweets()
    mood = returnMood()

    for t in tweets:
        print "Original tweet ",t

        tweetLower = t.lower()

        #language detection
        lng = get_language(tweetLower)
        print lng

        #translation
        gs = goslate.Goslate()
        translateTweet = gs.translate(tweetLower,'en')
        print "Translate tweet",translateTweet

        #preprocessing
        tokens,tokens_stemmed =  Preprocess(translateTweet)

        #SentiWordNet
        print "Results without stemming : ",
        tweetValue = senti_analisys(tokens)
        docAttPos,totdocPos = check(tweetValue,docAttPos,totdocPos,int(mood[count]),1,0)
        docAttNeg,totdocNeg = check(tweetValue,docAttNeg,totdocNeg,int(mood[count]),0,1)

        print "Results with stemming : ",
        tweetValue = senti_analisys(tokens_stemmed)
        docAttPosS,totdocPosS = check(tweetValue,docAttPosS,totdocPosS,int(mood[count]),1,0)
        docAttNegS,totdocNegS = check(tweetValue,docAttNegS,totdocNegS,int(mood[count]),0,1)

        count += 1


    print "POSITIVE : "
    calc_precision_recall(docAttPos,totdocPos,totdocAttPos)
    print "NEGATIVE : "
    calc_precision_recall(docAttNeg,totdocNeg,totdocAttNeg)
    print "POSITIVE STEMMED : "
    calc_precision_recall(docAttPosS,totdocPosS,totdocAttPosS)
    print "NEGATIVE STEMMED: "
    calc_precision_recall(docAttNegS,totdocNegS,totdocAttNegS)

if __name__ == '__main__':
    main()
