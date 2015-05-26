__author__ = 'sam'

import xml.dom.minidom


def parse_XML(file):
    nostm = stm = exp = org = trs = ""
    buf = ''
    dom = xml.dom.minidom.parse(file)
    rootel = dom.documentElement
    topnodes = rootel.childNodes
    for i in topnodes:
        child = i.childNodes
        for el in child:
            descendant = el.childNodes
            for elem in descendant:
                if elem.parentNode.nodeName == "Sentiment_nostem":
                    nostm = elem.nodeValue
                elif elem.parentNode.nodeName == "Sentiment_stem":
                    stm = elem.nodeValue
                elif elem.parentNode.nodeName == "Expected":
                    exp = elem.nodeValue
                elif elem.parentNode.nodeName == "Original_tweet":
                    org = elem.nodeValue
                elif elem.parentNode.nodeName == "Translate_tweet":
                    trs = elem.nodeValue

            if nostm != exp or stm != exp:
                buf += "Original tweet "+org + "\n" +"Translate tweet"+trs +"\n"+\
                      "No Stemmed: "+nostm+"\nStemmed: "+stm+"\nExpected: "+exp+"\n"
    return buf

if __name__ == '__main__':
    parse_XML("results/PopeTweets100.xml")