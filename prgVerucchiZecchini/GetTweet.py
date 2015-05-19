__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

def returnTweets():
    f = open("test.txt")
    t = []
    for i in f.read().splitlines():
        line = i.split("|")
        t.append( line[0])
    f.close()
    return t

def returnMood():
    f = open("test.txt")
    m = []
    for i in f.read().splitlines():
        line = i.split("|")
        m.append( line[1])
    f.close()
    return m

def returnDates():
    f = open("test.txt")
    d = []
    for i in f.read().splitlines():
        line = i.split("|")
        d.append( line[2])
    f.close()
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