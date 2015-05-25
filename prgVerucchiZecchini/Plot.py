__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import matplotlib.patches as mpatches



def plotMoodline (dates,moods, moodsS):

    correctDates = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]

    fig = plt.figure()
    ax = plt.subplot("111")

    ax.plot(correctDates,moods)
    ax.plot(correctDates,moodsS)

    ax.set_ylim([-1.0,1.0])

    fig.suptitle("Evalutation of mood without stemming", fontsize=16)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Mood (1 : positive, -1: negative)', fontsize=16)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.gcf().autofmt_xdate()

    plt.show()



if __name__ == '__main__':
    plotMoodline(['06/05/2015','03/06/2015','22/07/2015'],[0.5,0.8,-0.3],[0.1,0.5,-0.6])