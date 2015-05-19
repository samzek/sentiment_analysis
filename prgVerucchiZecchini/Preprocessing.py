# !/usr/bin/env python
#  -*- coding: utf-8 -*-

from nltk.corpus import stopwords
import nltk


def Preprocess(tweet):

    #tokenize
    tokens = nltk.word_tokenize(tweet)
    wnl = nltk.WordNetLemmatizer()

    #puntcation removal
    for i in tokens:
        if i in {u'.',u',',u';',u':',u'!',u'?'}:
            tokens.remove(i)

    #tagging
    tokens = nltk.pos_tag(tokens)

    #stopwords removal
    tokens_no_stop = []

    for t,part in tokens:
        if not t in stopwords.words('english'):
          tokens_no_stop.append((wnl.lemmatize(t),part))


    tokens_stemmed = []

    porter = nltk.PorterStemmer()
    for t,part in tokens_no_stop:
        tokens_stemmed.append((porter.stem(t),part))

    return tokens_no_stop, tokens_stemmed


