__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

def retrieveData(index, file_input):
    f = open(file_input)
    data = []
    for i in f.read().splitlines():
        line = i.split("|")
        data.append( line[index])
    f.close()
    return data

def returnTweets(file_input):
    t = retrieveData(0,file_input)
    return t

def returnMood(file_input):
    m = retrieveData(1,file_input)
    return m

def returnDates(file_input):
    d = retrieveData(2,file_input)
    return d

def returnNPos(file_input):
    n_pos = 0
    f = open(file_input)
    for i in f.read().splitlines():
        line = i.split("|")
        if int(line[1]) == 1:
            n_pos += 1
    f.close()
    return n_pos

def returnNNeg(file_input):
    n_neg = 0
    f = open(file_input)
    for i in f.read().splitlines():
        line = i.split("|")
        if int(line[1]) == -1:
            n_neg += 1
    f.close()
    return n_neg