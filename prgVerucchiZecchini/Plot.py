__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


def plotMoodline (dates,moods):

    correctDates = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.plot(correctDates,moods)
    plt.gcf().autofmt_xdate()
    plt.show()


#if __name__ == '__main__':
#    plotMoodline(['06/05/2015','03/01/2015','02/02/2015'],[0,1,0])