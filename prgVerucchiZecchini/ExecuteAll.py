#-*- coding: utf-8 -*-

import goslate
from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys
from GetTweet import returnTweets,returnMood,returnNNeg,returnNPos, returnDates
from Plot import plotMoodline
from xml_creator import create_xml,write_xml
from lxml import etree as ET
import sys

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

def calcPosAndNeg(file_input):
    if returnNPos(file_input) == 0:
        pos = False
    else:
        pos= True
    if returnNNeg(file_input) == 0:
        neg = False
    else:
        neg = True

    return pos,neg




def ExecuteAll(file_input,file_output, plot):

    pos,neg = calcPosAndNeg(file_input)

    #0 : positive       1: negative     2: positive and stemmed     3: negative and stemmed
    retrieved = [0,0,0,0]  #recuperati
    intersection = [0,0,0,0]  #intersezione
    relevant = [returnNPos(file_input),returnNNeg(file_input),returnNPos(file_input),returnNNeg(file_input)]   #attinenti

    count = 0
    tweets = returnTweets(file_input)
    mood = returnMood(file_input)
    retrMoods = []
    retrMoodsS = []

    root = ET.Element("tweet_collection")

    for t in tweets:
        print "Original tweet ",t

        tweetLower = t.lower()

        #language detection
        lng = get_language(tweetLower)

        #translation
        if lng != 'english':
            gs = goslate.Goslate()
            translateTweet = gs.translate(tweetLower,'en')
            print "Translate tweet",translateTweet
        else:
            translateTweet = tweetLower

        #preprocessing
        tokens,tokens_stemmed =  Preprocess(translateTweet)

        #SentiWordNet
        print "Results without stemming : ",
        tweetValue,moodValue = senti_analisys(tokens)
        if pos:
            retrieved[0],intersection[0] = check(tweetValue,retrieved[0],intersection[0],int(mood[count]),1)
        #print "valori A, Ra,R POS",retrieved[0],intersection[0],returnNPos()
        if neg:
            retrieved[1],intersection[1] = check(tweetValue,retrieved[1],intersection[1],int(mood[count]),-1)
        #print "valori A, Ra,R NEG",retrieved[1],intersection[1],returnNNeg()

        retrMoods.append(moodValue)

        print "Results with stemming : ",
        tweetValueS,moodValue = senti_analisys(tokens_stemmed)
        if pos:
            retrieved[2],intersection[2] = check(tweetValueS,retrieved[2],intersection[2],int(mood[count]),1)
        if neg:
            retrieved[3],intersection[3] = check(tweetValueS,retrieved[3],intersection[3],int(mood[count]),-1)

        retrMoodsS.append(moodValue)

        #create XML
        create_xml(root,tweetLower,translateTweet,tweetValue,tweetValueS)

        count += 1

    #precision and removal
    resCase = ["POSITIVE : ","NEGATIVE : ","POSITIVE STEMMED : ","NEGATIVE STEMMED: "]
    for i in xrange(4):
        if neg==False and i in {1,3}:
            continue
        if pos==False and i in {0,2}:
            continue
        print resCase[i]
        calc_precision_recall(retrieved[i],intersection[i],relevant[i])

    #write XML
    write_xml(root,file_output)

    #graphic plot
    if plot:
        plotMoodline(returnDates(file_input),retrMoods, retrMoodsS)



if __name__ == '__main__':
    ExecuteAll('db/PosNegTweets.txt','results/PosNegtweet.xml',False)
