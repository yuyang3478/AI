# -*- coding:utf-8 -*-
import os
import shutil
import minidom
from PIL import Image
import datetime
import numpy as np
# from xml.dom import minidom
root_dir="C:/Users/ASUS/Desktop/labletool/jietu/"
anno_dir=root_dir+"biaozhu/"
img_dir=root_dir+"tupian/"
train_dir=root_dir+"train/"
train_anno_dir=train_dir+"test_gene_annotations/"
train_img_dir=train_dir+"test_images/"

imglist=[]
for img in os.listdir(train_img_dir):
    noext = os.path.splitext(img)[0]
    imglist.append(noext)

for anno in os.listdir(train_anno_dir):
    noext = os.path.splitext(anno)[0]
    if noext not in imglist:
        os.remove(train_anno_dir+anno)


