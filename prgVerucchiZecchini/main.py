#-*- coding: utf-8 -*-

import goslate;
from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys

def main():

    tweetB = "Mike Boisner pitched an oustanding game today"
    print "Italian tweet ",tweetB

    tweetLower = tweetB.lower()

    #language detection
    lng = get_language(tweetLower)
    print lng

    #translation
   # gs = goslate.Goslate()
   # translateTweet = gs.translate(tweetLower,'en')
    #print "Translate tweet",translateTweet

    #preprocessing
    tokens =  Preprocess(tweetLower)

    #SentiWordNet
    senti_analisys(tokens)
    


if __name__ == '__main__':
    main()
