#-*- coding: utf-8 -*-

import goslate
from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys
from GetTweet import returnTweets,returnMood,returnNNeg,returnNPos, returnDates
from Plot import plotMoodline


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

    return docAtt, totdoc

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

    #0 : positive       1: negative     2: positive and stemmed     3: negative and stemmed
    docAtt = [0,0,0,0]  #recuperati
    totdoc = [0,0,0,0]  #intersezione
    totdocAtt = [returnNPos(),returnNNeg(),returnNPos(),returnNNeg()]   #attinenti

    count = 0
    tweets = returnTweets()
    mood = returnMood()
    retrMoods = []
    retrMoodsS = []

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
        docAtt[0],totdoc[0] = check(tweetValue,docAtt[0],totdoc[0],int(mood[count]),1,0)
        docAtt[1],totdoc[1] = check(tweetValue,docAtt[1],totdoc[1],int(mood[count]),0,1)

        retrMoods.append(tweetValue)

        print "Results with stemming : ",
        tweetValue = senti_analisys(tokens_stemmed)
        docAtt[2],totdoc[2] = check(tweetValue,docAtt[2],totdoc[2],int(mood[count]),1,0)
        docAtt[3],totdoc[3] = check(tweetValue,docAtt[3],totdoc[3],int(mood[count]),0,1)

        retrMoodsS.append(tweetValue)

        count += 1


    resCase = ["POSITIVE : ","NEGATIVE : ","POSITIVE STEMMED : ","NEGATIVE STEMMED: "]
    for i in xrange(4):
        print resCase[i]
        calc_precision_recall(docAtt[i],totdoc[i],totdocAtt[i])


    plotMoodline(returnDates(),retrMoods)
    plotMoodline(returnDates(),retrMoodsS)

if __name__ == '__main__':
    main()
