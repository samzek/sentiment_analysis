#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ExecuteAll import ExecuteAll
<<<<<<< HEAD
from gi.repository import Gtk


builder = Gtk.Builder()
builder.add_from_file("GUI.glade")

window = builder.get_object("window1")
window.show_all()

Gtk.main()
"""
=======
>>>>>>> 6aa5c4491784b3e546498707ab9242a03ece4672

print "Sentiment Analisys di tweet da tradurre sia positivi che negativi"
ExecuteAll('db/TrPosNegTweets.txt','results/TrPosNegtweet.xml',False)

print "Sentiment Analisys di tweet in inglese sia positivi che negativi"
ExecuteAll('db/PosNegTweets.txt','results/PosNegtweet.xml',False)

print "Sentiment Analisys di tweet da tradurre solo positivi"
ExecuteAll('db/TrPosTweets.txt','results/TrPostweet.xml',False)

print "Sentiment Analisys di tweet da tradurre solo negativi"
ExecuteAll('db/TrNegTweets.txt','results/TrNegtweet.xml',False)

print "Sentiment Analisys di tweet in inglese solo positivi"
ExecuteAll('db/PosTweets.txt','results/Postweet.xml',False)

print "Sentiment Analisys di tweet in inglese solo negativi"
ExecuteAll('db/NegTweets.txt','results/Negtweet.xml',False)

print "Sentiment Analisys dei tweet di una singola persona : Papa Francesco"
ExecuteAll('db/PopeTweets100.txt','results/Popetweet.xml',True)
<<<<<<< HEAD
"""
=======
>>>>>>> 6aa5c4491784b3e546498707ab9242a03ece4672
