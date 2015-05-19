__author__ = 'sam'

from lxml import etree as ET

def create_xml():
    root = ET.Element("tweet_collection")
    tweet = ET.SubElement(root,"tweet")
    ET.SubElement(tweet,"Original_tweet").text="Questa e' una prova"
    ET.SubElement(tweet,"Translate_tweet").text="This is a test"
    ET.SubElement(tweet,"Sentiment_nostem").text="POSITIVE"
    ET.SubElement(tweet,"Sentiment_stem").text="POSITIVE"

    #print ET.tostring(root,pretty_print=True,xml_declaration=True)

    tree = ET.ElementTree(root)
    tree.write("tweet.xml",pretty_print=True,xml_declaration=True)

if __name__ == '__main__':
    create_xml()