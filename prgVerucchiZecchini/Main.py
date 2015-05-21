#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ExecuteAll import ExecuteAll

print "Sentiment Analisys di tweet da tradurre sia positivi che negativi"
ExecuteAll('db/MixTweets.txt','results/Mixtweet.xml',False)

print "Sentiment Analisys di tweet in inglese sia positivi che negativi"
ExecuteAll('db/PosNegTweets.txt','results/PosNegtweet.xml',False)

print "Sentiment Analisys di tweet da tradurre solo positivi"

print "Sentiment Analisys di tweet da tradurre solo negativi"

print "Sentiment Analisys di tweet in inglese solo positivi"
ExecuteAll('db/PosTweets.txt','results/Postweet.xml',False)

print "Sentiment Analisys di tweet in inglese solo negativi"
ExecuteAll('db/NegTweets.txt','results/Negtweet.xml',False)

print "Sentiment Analisys dei tweet di una singola persona : Papa Francesco"
ExecuteAll('db/PopeTweets100.txt','results/Popetweet.xml',True)
