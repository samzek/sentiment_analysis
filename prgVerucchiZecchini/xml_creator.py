#  -*- coding: utf-8 -*-
__author__ = 'sam'

from lxml import etree as ET
import sys


def create_xml(root,tweetVal,trantweet,s_nostem,s_stem):
    tweet = ET.SubElement(root,"tweet")
    ET.SubElement(tweet,"Original_tweet").text=tweetVal.decode('utf-8')
    ET.SubElement(tweet,"Translate_tweet").text=trantweet.decode('utf-8')
    if s_nostem == 1:
        ET.SubElement(tweet,"Sentiment_nostem").text="POSITIVE"
    elif s_nostem == -1:
        ET.SubElement(tweet,"Sentiment_nostem").text="NEGATIVE"
    else:
        ET.SubElement(tweet,"Sentiment_nostem").text="OBJECTIVE"
    if s_stem == 1:
        ET.SubElement(tweet,"Sentiment_stem").text="POSITIVE"
    elif s_stem == -1:
        ET.SubElement(tweet,"Sentiment_stem").text="NEGATIVE"
    else:
        ET.SubElement(tweet,"Sentiment_stem").text="OBJECTIVE"

def create_PR(root):
    pr = ET.SubElement(root,"Precision_recall")
    return pr

def add_PR_to_xml(root,val,precision,recall):
    pos=ET.SubElement(root,val)
    ET.SubElement(pos,"Precision").text=str(precision)+"%"
    ET.SubElement(pos,"Recall").text=str(recall)+"%"

def write_xml(root,file_output):

    tree = ET.ElementTree(root)
    tree.write(file_output,pretty_print=True,xml_declaration=True,encoding="utf-8")

    with open(file_output,'r') as file:
        data = file.readlines()

    for i in xrange(0,len(data)):
        if data[i] == '<tweet_collection>\n':
            data[i] = "<tweet_collection " \
                      "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n" \
                      "xsi:noNamespaceSchemaLocation=\"tweet_collection.xsd\">\n"
            break

    with open(file_output,'w') as file:
        file.writelines(data)
