__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

def retrieveData(index):
    f = open("test.txt")
    data = []
    for i in f.read().splitlines():
        line = i.split("|")
        data.append( line[index])
    f.close()
    return data

def returnTweets():
    t = retrieveData(0)
    return t

def returnMood():
    m = retrieveData(1)
    return m

def returnDates():
    d = retrieveData(2)
    return d

def returnNPos():
    n_pos = 0
    f = open("test.txt")
    for i in f.read().splitlines():
        line = i.split("|")
        if int(line[1]) == 1:
            n_pos += 1
    f.close()
    return n_pos

def returnNNeg():
    n_neg = 0
    f = open("test.txt")
    for i in f.read().splitlines():
        line = i.split("|")
        if int(line[1]) == -1:
            n_neg += 1
    f.close()
    return n_neg