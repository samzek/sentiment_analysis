#-*- coding: utf-8 -*-
__author__ = 'sam'

from weka.core import jvm as jvm
from weka.core.converters import  Loader
from weka.classifiers import Classifier,Evaluation
from weka.core.classes import Random

def weka():
    data_dir="/home/sam/Dropbox/prg_sentiment/weka-3-6-12/data/"
    jvm.start()
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("train_weka.arff")#data_dir+"iris.arff")
    data.class_is_last()
    print data
    cls = Classifier(classname="weka.classifiers.functions.SimpleLogistic")
    cls.build_classifier(data)
    evaluation = Evaluation(data)
    evaluation.crossvalidate_model(cls,data,10,Random(40))
    print(evaluation.summary())
    """
    for index,inst in enumerate(data):
        pred = cls.classify_instance(inst)
        dist = cls.distribution_for_instance(inst)
        print(str(index+1)+" "+str(pred)+" "+str(dist))
    """
    jvm.stop()

if __name__ == '__main__':
    weka()