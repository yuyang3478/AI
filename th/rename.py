# -*- coding:utf-8 -*-
import os
import datetime

anno_dir="C:/Users/ASUS/Desktop/labletool/jietu/biaozhu/"
img_dir="C:/Users/ASUS/Desktop/labletool/jietu/tupian/"
train_dir="C:/Users/ASUS/Desktop/labletool/jietu/train/"
train_anno_dir=train_dir+"Annotations/"
train_img_dir=train_dir+"JPEGImages/"

count=1
for anno_file_name in os.listdir(train_anno_dir):
    xmlfile = train_anno_dir + anno_file_name
    f_no_ext = os.path.splitext(anno_file_name)[0]
    jpgfile = train_img_dir+f_no_ext+'.jpg'
    print f_no_ext

    os.rename(xmlfile,train_anno_dir+datetime.datetime.now().strftime('%m_%d_')+str(count)+'.xml')
    os.rename(jpgfile, train_img_dir + datetime.datetime.now().strftime('%m_%d_') + str(count) + '.jpg')
    count+=1