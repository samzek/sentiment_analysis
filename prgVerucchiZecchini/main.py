#-*- coding: utf-8 -*-

import goslate
from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys
from GetTweet import returnTweets,returnMood,returnNNeg,returnNPos, returnDates
from Plot import plotMoodline
from xml_creator import create_xml

def check(tweetValue,retrieved,intersection,realValue,t):
    if tweetValue == t :
        retrieved+=1
        if tweetValue == realValue:
            intersection += 1

    return retrieved, intersection

def calc_precision_recall(retrieved,intersection,relevant):
    #Precision: attinenti intersecato recuperati /recuperati
    precision = intersection / float(retrieved) *100
    print "\tPRECISION: ", precision,"%"
    #Recall: attinenti intersecato recuperati /attinenti
    recall = intersection / float(relevant) *100
    print "\tRECALL", recall,"%"

def main():

    #0 : positive       1: negative     2: positive and stemmed     3: negative and stemmed
    retrieved = [0,0,0,0]  #recuperati
    intersection = [0,0,0,0]  #intersezione
    relevant = [returnNPos(),returnNNeg(),returnNPos(),returnNNeg()]   #attinenti

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
        tweetValue,moodValue = senti_analisys(tokens)
        retrieved[0],intersection[0] = check(tweetValue,retrieved[0],intersection[0],int(mood[count]),1)
        #print "valori A, Ra,R POS",retrieved[0],intersection[0],returnNPos()
        retrieved[1],intersection[1] = check(tweetValue,retrieved[1],intersection[1],int(mood[count]),-1)
        #print "valori A, Ra,R NEG",retrieved[1],intersection[1],returnNNeg()

        retrMoods.append(moodValue)

        print "Results with stemming : ",
        tweetValue,moodValue = senti_analisys(tokens_stemmed)
        retrieved[2],intersection[2] = check(tweetValue,retrieved[2],intersection[2],int(mood[count]),1)
        retrieved[3],intersection[3] = check(tweetValue,retrieved[3],intersection[3],int(mood[count]),-1)

        retrMoodsS.append(moodValue)

        count += 1

    #precision and removal
    resCase = ["POSITIVE : ","NEGATIVE : ","POSITIVE STEMMED : ","NEGATIVE STEMMED: "]
    for i in xrange(4):
        print resCase[i]
        calc_precision_recall(retrieved[i],intersection[i],relevant[i])

    #graphic plot
    plotMoodline(returnDates(),retrMoods, retrMoodsS)
    #plotMoodline(returnDates(),retrMoodsS)
    create_xml()

if __name__ == '__main__':
    main()
