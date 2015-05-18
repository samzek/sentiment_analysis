#-*- coding: utf-8 -*-

import goslate;
from DetectLanguage import get_language
from Preprocessing import Preprocess
def main():

    tweetB = "Pronti a discutere merito di tutto, con tutti. Ma dopo aver discusso, si decide. L'Italia non può più perdere tempo"
    print "Italian tweet ",tweetB

    tweetLower = tweetB.lower()

    #language detection
    lng = get_language(tweetLower)
    print lng

    #translation
    gs = goslate.Goslate()
    translateTweet = gs.translate(tweetLower,'en')
    print "Translate tweet",translateTweet

    #preprocessing
    print Preprocess(translateTweet)

    #SentiWordNet
    


if __name__ == '__main__':
    main()