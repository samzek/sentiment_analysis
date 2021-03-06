#-*- coding: utf-8 -*-

import time
from gi.repository import Gtk

import goslate
from lxml import etree as ET

from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys
from GetTweet import returnTweets,returnMood,returnNNeg,returnNPos,returnDates
from Plot import plotMoodline
from XML_creator import *


def check(tweetValue,retrieved,intersection,realValue,t):
    if tweetValue == t :
        retrieved+=1
        if tweetValue == realValue:
            intersection += 1

    return retrieved, intersection

def calc_precision_recall(retrieved,intersection,relevant):
    #Precision: attinenti intersecato recuperati /recuperati
    if retrieved == 0:
        precision = 0
    else:
        precision = intersection / float(retrieved) *100

    #Recall: attinenti intersecato recuperati /attinenti
    recall = intersection / float(relevant) *100


    return round(precision,2),round(recall,2)

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

def profile_start():
    s = time.time()
    return s
def profile_stop(string,s1):
    s = time.time() - s1
    print "Function: "+string+":"+str(s)

def ExecuteAll(file_input,file_output, plot):

    pos,neg = calcPosAndNeg(file_input)
    lng = 'english'
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
        #print "Original tweet ",t

        tweetLower = t.lower()

        #ret = profile_start()
        #language detection
        lng = get_language(tweetLower)
        #profile_stop("get_language",ret)

        #translation
        if lng != 'english':
            try:
                #ret = profile_start()
                gs = goslate.Goslate()
                #profile_stop("Goslate",ret)
                #ret = profile_start()
                translateTweet = gs.translate(tweetLower,'en')
                #profile_stop("translate",ret)
            except Exception as e:
                md = Gtk.MessageDialog(None, 0,Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, "No connection found!")
                md.run()
                md.destroy()
                return [],[],[]

        else:
            translateTweet = tweetLower

        #preprocessing
        #ret = profile_start()
        tokens,tokens_stemmed =  Preprocess(translateTweet)
        #profile_stop("Preprocess",ret)

        #ret = profile_start()
        #SentiWordNet
        tweetValue,moodValue = senti_analisys(tokens)
        #profile_stop("Senti analisys",ret)

        if pos:
            retrieved[0],intersection[0] = check(tweetValue,retrieved[0],intersection[0],int(mood[count]),1)

        if neg:
            retrieved[1],intersection[1] = check(tweetValue,retrieved[1],intersection[1],int(mood[count]),-1)

        retrMoods.append(moodValue)

        tweetValueS,moodValue = senti_analisys(tokens_stemmed)
        if pos:
            retrieved[2],intersection[2] = check(tweetValueS,retrieved[2],intersection[2],int(mood[count]),1)
        if neg:
            retrieved[3],intersection[3] = check(tweetValueS,retrieved[3],intersection[3],int(mood[count]),-1)

        retrMoodsS.append(moodValue)

        #create XML
        create_xml(root,tweetLower,translateTweet,tweetValue,tweetValueS,int(mood[count]),lng)

        count += 1

    tagPR = create_PR(root)
    prList = []
    reList = []
    caseDone = []
    #precision and removal
    resCase = ["POSITIVE","NEGATIVE","POSITIVE_STEMMED","NEGATIVE_STEMMED"]
    for i in xrange(4):
        if neg==False and i in {1,3}:
            continue
        if pos==False and i in {0,2}:
            continue
        #print resCase[i]
        precision,recall=calc_precision_recall(retrieved[i],intersection[i],relevant[i])
        prList.append(precision)
        reList.append(recall)
        caseDone.append(resCase[i])
        add_PR_to_xml(tagPR,resCase[i],precision,recall)

    #write XML
    write_xml(root,file_output)

    #graphic plot
    if plot:
       plotMoodline(returnDates(file_input),retrMoods, retrMoodsS)

    return  caseDone,prList,reList,lng

if __name__ == '__main__':
    ExecuteAll('db/Pope.txt','results/tweet.xml',False)
