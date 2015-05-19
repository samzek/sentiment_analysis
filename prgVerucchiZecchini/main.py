#-*- coding: utf-8 -*-

import goslate;
from DetectLanguage import get_language
from Preprocessing import Preprocess
from SentiAnalisys import senti_analisys
from GetTweet import returnTweets

def main():

<<<<<<< HEAD
    tweetB = "Mike Boisner pitched an oustanding game today"
    print "Italian tweet ",tweetB
=======
    tweets = returnTweets()
>>>>>>> bf4df565107184f78abf718c433dd8c274cab24e

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
        senti_analisys(tokens)



if __name__ == '__main__':
    main()
