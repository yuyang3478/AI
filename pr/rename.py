# -*- coding:utf-8 -*-
import os
import datetime

root_dir="D:/biaozhu_gongju/"
anno_dir=root_dir+"Annotations/"
img_dir=root_dir+"JPEGImages/"
train_dir=root_dir+"train/"
train_anno_dir=train_dir+"Annotations/"
train_img_dir=train_dir+"JPEGImages/"

count=247
for img in os.listdir(img_dir):
    print img
    # os.rename(xmlfile,train_anno_dir+datetime.datetime.now().strftime('%m_%d_')+str(count)+'.xml')
    os.rename(img_dir+img, img_dir + datetime.datetime.now().strftime('%m_%d_') + str(count) + '.jpg')
    count+=1