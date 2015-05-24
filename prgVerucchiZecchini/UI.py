#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from DetectLanguage import get_language
import goslate
from Preprocessing import Preprocess
from SentiAnalisys import  senti_analisys

def on_delete_event(widget,event):
    window.show_all()
    windowNT.hide()

def load_new_test(event):
    windowNT.show_all()
    window.hide()
    windowNT.connect("delete-event", on_delete_event)




    pass
def show_XML_results (event):
    pass
def update_pope (event):
    pass
def exec_test(event):
    pass


def keyPress(widget, event):
    if event.keyval == 65293:
        sentence =  textField.get_text()

        sLower = sentence.lower()

        lng = get_language(sLower)
        if lng != 'english':
            gs = goslate.Goslate()
            translateS = gs.translate(sLower,'en')
        else:
            translateS = sLower

        tokens,tokens_stemmed =  Preprocess(translateS)

        sValue,moodValue = senti_analisys(tokens)

        if sValue ==1:
            image.set_from_file("images/happy.png")
        elif sValue == 0:
            image.set_from_file("images/boh.png")
        elif sValue == -1:
            image.set_from_file("images/sad.png")


builder = Gtk.Builder()
builder.add_from_file("GUI.glade")
window = builder.get_object("MainWindow")

NewTestBuilder = Gtk.Builder()
NewTestBuilder.add_from_file("InsertNewTest.glade")
windowNT = NewTestBuilder.get_object("window1")


textField = builder.get_object("entry1")
textField.connect('key-press-event', keyPress)

image = builder.get_object("image1")

liststore = builder.get_object("liststore1")
liststore.append(["Inglese tutto positivo"])
liststore.append(["Inglese tutto negativo"])
liststore.append(["Inglese posititvo e negativo"])


execTest = builder.get_object("button4")
execTest.connect('clicked', exec_test)

loadTest = builder.get_object("button1")
loadTest.connect('clicked', load_new_test)

updatePope = builder.get_object("button2")
updatePope.connect('clicked', update_pope)

showXML = builder.get_object("button3")
showXML.connect('clicked', show_XML_results)

results = builder.get_object("textview1")





window.show_all()
window.connect("delete-event", Gtk.main_quit)
Gtk.main()
