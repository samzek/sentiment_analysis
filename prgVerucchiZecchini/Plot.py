__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


def plotMoodline (dates,moods):

    correctDates = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

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

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.plot(correctDates,moods)
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    plotMoodline(['06/05/2015','03/01/2015','02/02/2015'],[0,1,0])