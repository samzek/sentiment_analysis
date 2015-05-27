__author__ = 'sam'

import xml.dom.minidom


def parse_XML(file,lang):
    nostm = stm = exp = org = trs = ""
    buf = ''
    dom = xml.dom.minidom.parse(file)
    rootel = dom.documentElement
    topnodes = rootel.childNodes


    for i in topnodes:
        child = i.childNodes
        if len(child) == 0:
            continue
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
                else:
                    nostm = exp = org = trs = stm = ""

        if nostm != exp or stm != exp:
            if lang != 'english':
                buf += "Original tweet:\t"+org + "\n" +"Translate tweet:\t"+trs +"\n"+\
                     "No Stemmed:\t"+nostm+"\nStemmed:\t"+stm+"\nExpected:\t"+exp+"\n\n"
            else:
                buf += "Tweet:\t"+trs +"\n"+\
                     "No Stemmed:\t"+nostm+"\nStemmed:\t"+stm+"\nExpected:\t"+exp+"\n\n"

    return buf

if __name__ == '__main__':
    print parse_XML("results/PopeTweets100.xml","english")
