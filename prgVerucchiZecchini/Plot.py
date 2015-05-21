__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


def plotMoodline (dates,moods, moodsS):

    correctDates = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]

    #eventuale ordinamento delle date
    """
    prova = []
    for i in xrange(len(moods)):
        prova.append((dates[i],moods[i]))

    for i in xrange(len(prova)-1,-1,-1):
        for j in xrange(0,i):
            if prova[j][0]>prova[j+1][0]:
                prova[j], prova[j+1] = prova[j+1],prova[j]

    dates = []
    moods = []
    for d,m in prova:
        dates.append(d)
        moods.append(m)

    """

    fig = plt.figure()
    withoutStemming = fig.add_subplot(211)
    withoutStemming.plot(correctDates,moods)
    withStemming = fig.add_subplot(212)
    withStemming.plot(correctDates,moodsS)

    withoutStemming.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    withStemming.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    plotMoodline(['06/05/2015','03/06/2015','22/07/2015'],[0.5,0.8,-0.3],[0.1,0.5,-0.6])