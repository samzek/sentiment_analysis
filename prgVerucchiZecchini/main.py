#-*- coding: utf-8 -*-


def main():
    tweetB = "When it comes to a woman's health, no politician should get to decide what's best for you"
    print "English tweet ",tweetB
    #detect lang
    lng = get_language(tweetB)
    print lng
    #translate
    translateTweet = translate(lng)
    print "Translate tweet",translateTweet

if __name__ == '__main__':
    main()