# -*- coding:utf-8 -*-
import os
import shutil
import xml.dom.minidom
from PIL import Image
import numpy as np
from xml.dom import minidom

anno_dir="C:/Users/ASUS/Desktop/labletool/jietu/biaozhu/"
img_dir="C:/Users/ASUS/Desktop/labletool/jietu/tupian/"
train_dir="C:/Users/ASUS/Desktop/labletool/jietu/train/"
train_anno_dir=train_dir+"Annotations/"
train_img_dir=train_dir+"JPEGImages/"
imageSets_dir="C:/Users/ASUS/Desktop/labletool/jietu/train/ImageSets/Main/"

labels=set(['helmet','nhelmet'])
dict={}
for label in labels:
    dict[label]=set([])

for anno_file_name in os.listdir(train_anno_dir):
    xmlfile = train_anno_dir + anno_file_name
    DomTree = xml.dom.minidom.parse(xmlfile)
    annotation = DomTree.documentElement
    f_no_ext = os.path.splitext(anno_file_name)[0]
    objectlist = annotation.getElementsByTagName('object')
    for objects in objectlist:
        namelist = objects.getElementsByTagName('name')
        # print 'namelist:',namelist
        objectname = namelist[0].childNodes[0].data
        dict[objectname].add(f_no_ext)
        labels.add(objectname)
print labels

if os.path.exists(imageSets_dir+'train.txt'):
    os.remove(imageSets_dir+'train.txt')
if os.path.exists(imageSets_dir+'val.txt'):
    os.remove(imageSets_dir+'val.txt')
train_val_ratio=4
index=1
for anno_file_name in os.listdir(train_anno_dir):
    f_no_ext = os.path.splitext(anno_file_name)[0]
    if index%5!=0:
        with open(imageSets_dir+'train.txt', 'a') as f:
            f.write(f_no_ext+'\n')
    else:
        with open(imageSets_dir + 'val.txt', 'a') as f:
            f.write(f_no_ext+'\n')
    index+=1
def isinfile(train_val,f_no_ext):
    pass

#先写train
with open(imageSets_dir + 'train.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        for label in labels:
            label_file = imageSets_dir+label+'_train.txt'
            with open(label_file, 'a') as fl:
                if line in dict[label]:
                    fl.write(line+' 1\n')
                else:
                    fl.write(line+' -1\n')
#再写val
with open(imageSets_dir + 'val.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        for label in labels:
            label_file = imageSets_dir+label+'_val.txt'
            with open(label_file, 'a') as fl:
                if line in dict[label]:
                    fl.write(line+' 1\n')
                else:
                    fl.write(line+' -1\n')