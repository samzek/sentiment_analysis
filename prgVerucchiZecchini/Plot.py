__author__ = 'micaela'
# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import datetime
import random
import matplotlib.pyplot as plt


def plotMoodline (dates,moods):

    plt.plot(dates,moods)
    plt.gcf().autofmt_xdate()

    plt.show()