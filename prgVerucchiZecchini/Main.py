#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from DetectLanguage import get_language
import goslate
from Preprocessing import Preprocess
from SentiAnalisys import  senti_analisys
from ExecuteAll import ExecuteAll
from XML_parser import parse_XML
import os
import webbrowser



def on_delete_event(widget,event):
    window.show_all()
    widget.destroy()


def keyPress(widget, event):
    if event.keyval == 65293:
        sentence =  widget.get_text()

        sLower = sentence.lower()

        lng = get_language(sLower)

        try:
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

        except Exception as e:
            md = Gtk.MessageDialog(None, 0,Gtk.MessageType.ERROR,Gtk.ButtonsType.OK, "No connection found!")
            md.run()
            md.destroy()

def nameInserted(widget, event):

    if event.keyval == 65293:
        insertB = NewTestBuilder.get_object("button1")
        insertB.set_sensitive(True)

        insertB.connect('clicked', saveData)


def saveData(event):
    data = NewTestBuilder.get_object("textview1")
    dataName = NewTestBuilder.get_object("entry1")
    name =  dataName.get_text()

    buffer = data.get_buffer()

    str = buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter(),False)


    control = True
    s = str.split('\n')
    for i in s:
        p = i.split('|')
        try:

            if len(p) >= 2 and int(p[1]) in {1,-1}:
                with open("db/"+name+".txt",'w') as file:
                    file.writelines(str)
            else:
                label = NewTestBuilder.get_object("label1")
                label.set_text("ERRORE, INPUT ERRATO : Inserire test nella forma frase|1 o -1|GG/MM/AAAA")
                control= False
            if(control):
                liststore.append([name])

            windowNT = NewTestBuilder.get_object("window1")
            window.show_all()
            windowNT.destroy()

        except ValueError as e:
            label = NewTestBuilder.get_object("label1")
            label.set_text("ERRORE, INPUT ERRATO : Inserire test nella forma frase|1 o -1|GG/MM/AAAA")
            control= False



def load_new_test(event):

    NewTestBuilder.add_from_file("InsertNewTest.glade")

    windowNT = NewTestBuilder.get_object("window1")

    windowNT.show_all()
    window.hide()
    windowNT.connect("delete-event", on_delete_event)

    insertB = NewTestBuilder.get_object("button1")
    insertB.set_sensitive(False)

    dataName = NewTestBuilder.get_object("entry1")
    dataName.connect('key-press-event', nameInserted)


def open_error(event):
    """
    model, treeiter = treeview.get_selection().get_selected()
    if treeiter != None:
        fout = 'results/'+model[treeiter][0]+".xml"
    """
    global last_file_open
    global lang
    if last_file_open != None:
        NewTestBuilder.add_from_file("InsertNewTest.glade")
        windowError = NewTestBuilder.get_object("window2")
        text = NewTestBuilder.get_object("textview2")
        windowError.show_all()
        window.hide()
        windowError.connect("delete-event", on_delete_event)
        buffer = Gtk.TextBuffer()
        buffer.set_text(parse_XML(last_file_open,lang))
        text.set_buffer(buffer)


def show_XML_results (event):
    """
    model, treeiter = treeview.get_selection().get_selected()
    if treeiter != None:
        fout = 'results/'+model[treeiter][0]+".xml"
    """
    global last_file_open
    if last_file_open != None:
        webbrowser.open(last_file_open)

    #showXML.set_sensitive(False)



def exec_test(event):
    global last_file_open
    global lang
    model, treeiter = treeview.get_selection().get_selected()
    if treeiter != None:
        fin = 'db/'+ model[treeiter][0]+".txt"
        fout = 'results/'+model[treeiter][0]+".xml"


        last_file_open = fout
        if model[treeiter][0] == "PopeTweets100" or  model[treeiter][0] == "EnPopeTweets100":
            resCase,prList,reList,lang = ExecuteAll(fin,fout,True)
        else:
            resCase,prList,reList,lang = ExecuteAll(fin,fout,False)

        buf = ''
        for i in xrange(len(prList)):
            buf+= resCase[i]+ '\n\t' + "PRECISION: "+str(prList[i])+ "%\n\tRECALL: "+str(reList[i])+"%\n\n"
        buffer = Gtk.TextBuffer()
        buffer.set_text(buf)

        results.set_buffer(buffer)
        #showXML.set_sensitive(True)
        #SentiError.set_sensitive(True)


NewTestBuilder = Gtk.Builder()

builder = Gtk.Builder()
builder.add_from_file("GUI.glade")

window = builder.get_object("MainWindow")

textField = builder.get_object("entry1")
textField.connect('key-press-event', keyPress)

image = builder.get_object("image1")

#gestione liststore
treeview = builder.get_object("treeview1")

liststore = Gtk.ListStore(str)


for i in os.listdir(os.path.join(".","db")):
    liststore.append([i.split(".")[0]])

treeview.set_model(model=liststore)

renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Dataset", renderer, text=0)
treeview.append_column(column)


#gestione bottoni
execTest = builder.get_object("button4")
execTest.connect('clicked', exec_test)

loadTest = builder.get_object("button1")
loadTest.connect('clicked', load_new_test)

SentiError = builder.get_object("button2")
#SentiError.set_sensitive(False)
SentiError.connect('clicked', open_error)

showXML = builder.get_object("button3")
#showXML.set_sensitive(False)
showXML.connect('clicked', show_XML_results)

results = builder.get_object("textview1")

last_file_open = None
lang = None

window.show_all()
window.connect("delete-event", Gtk.main_quit)
Gtk.main()
