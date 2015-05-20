__author__ = 'sam'

from lxml import etree as ET
from lxml import objectify
import sys

ns = ("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
xi = ("xsi:noSpaceschemaLocation","tweet_collection.xsd")

def create_xml():

    root = ET.Element("tweet_collection")
    tweet = ET.SubElement(root,"tweet")
    ET.SubElement(tweet,"Original_tweet").text="Questa e' una prova"
    ET.SubElement(tweet,"Translate_tweet").text="This is a test"
    ET.SubElement(tweet,"Sentiment_nostem").text="POSITIVE"
    ET.SubElement(tweet,"Sentiment_stem").text="POSITIVE"

    tree = ET.ElementTree(root)
    tree.write("tweet.xml",pretty_print=True,xml_declaration=True)

    with open("tweet.xml",'r') as file:
        data = file.readlines()

    for i in xrange(0,len(data)):
        if data[i] == '<tweet_collection>\n':
            data[i] = "<tweet_collection " \
                      "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                      "xsi:noSpaceschemaLocation=\"tweet_collection.xsd\">\n"
            break

    with open("tweet.xml",'w') as file:
        file.writelines(data)

if __name__ == '__main__':
    create_xml()