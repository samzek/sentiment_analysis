#-*- coding: utf-8 -*-

import goslate;
from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys
from GetTweet import returnTweets,returnMood



def calc_precision_recall(docatt,totdoc,totdocatt):
    #Precision: numero di documenti attinenti trovati / totale documenti recuperati
    precision = docatt / float(totdoc) * 100
    print "PRECISION: ", precision,"%"
    #Recall: numero di documenti attinenti trovati / totale documenti attinenti esistenti
    recall = docatt / float(totdocatt) * 100
    print "RECALL", recall,"%"

def main():
    docAtt = 0
    totdoc = 0
    totdocAtt = 5

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
        tokens =  Preprocess(translateTweet)

        #SentiWordNet
        tweetValue = senti_analisys(tokens)
        if tweetValue == 1 and tweetValue == int(mood[count]):
            docAtt+=1
            totdoc+=1
        elif tweetValue == 0 and tweetValue != int(mood[count]):
            totdoc += 1
        count += 1
    calc_precision_recall(docAtt,totdoc,totdocAtt)

if __name__ == '__main__':
    main()
