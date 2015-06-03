#  -*- coding: utf-8 -*-
__author__ = 'sam'

from lxml import etree as ET
import sys



def check_insert_value(tweet,value,str):
    if value == 1:
        ET.SubElement(tweet,str).text="POSITIVE"
    elif value == -1:
        ET.SubElement(tweet,str).text="NEGATIVE"
    else:
        ET.SubElement(tweet,str).text="OBJECTIVE"

def create_xml(root,tweetVal,trantweet,s_nostem,s_stem,real_value,language):
    tweet = ET.SubElement(root,"tweet")
    ET.SubElement(tweet,"Original_tweet").text=tweetVal.decode('utf-8')
    if language != 'english':
        ET.SubElement(tweet,"Translate_tweet").text=trantweet.decode('utf-8')

    check_insert_value(tweet,s_nostem,"Sentiment_nostem")
    check_insert_value(tweet,s_stem,"Sentiment_stem")
    check_insert_value(tweet,real_value,"Expected")

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
