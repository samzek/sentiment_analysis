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
