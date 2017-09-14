# -*- coding:utf-8 -*-
import os
import shutil
import xml.dom.minidom
from PIL import Image
import numpy as np

anno_dir="D:/biaozhu_gongju/Annotations/"
img_dir="D:/biaozhu_gongju/JPEGImages/"
train_dir="D:/biaozhu_gongju/train/"
train_anno_dir=train_dir+"Annotations/"
train_img_dir=train_dir+"JPEGImages/"

# remove_img_dir = "D:/biaozhu_gongju/tmp/"

for img_file_name in os.listdir(train_img_dir):
    anno_file_name = os.path.splitext(img_file_name)[0]+".xml"
    orig_anno_file_path = anno_dir+anno_file_name
    shutil.copy (orig_anno_file_path, train_anno_dir+anno_file_name)

#拷贝图片到目标目录
for anno_file_name in os.listdir(anno_dir):
    img_file_name = os.path.splitext(anno_file_name)[0]+".jpg"
    origin_img_file_path =img_dir+img_file_name
    shutil.copy (origin_img_file_path, train_img_dir+img_file_name)

#裁剪车牌
for anno_file_name in os.listdir(anno_dir):
    img_file_name = os.path.splitext(anno_file_name)[0] + ".jpg"
    print img_file_name
    origin_img_file_path =img_dir+img_file_name

    xmlfile = anno_dir + anno_file_name

    DomTree = xml.dom.minidom.parse(xmlfile)
    annotation = DomTree.documentElement

    filenamelist = annotation.getElementsByTagName('filename')  # [<DOM Element: filename at 0x381f788>]
    filename = filenamelist[0].childNodes[0].data
    objectlist = annotation.getElementsByTagName('object')
    i = 1

    # 裁剪车牌
    minx = 10000
    maxx = -1
    miny = 10000
    maxy = -1
    for objects in objectlist:
        # print objects
        namelist = objects.getElementsByTagName('name')
        # print 'namelist:',namelist
        objectname = namelist[0].childNodes[0].data
        # print objectname

        bndbox = objects.getElementsByTagName('bndbox')
        cropboxes = []
        for box in bndbox:
            try:
                x1_list = box.getElementsByTagName('xmin')
                x1 = int(x1_list[0].childNodes[0].data)
                y1_list = box.getElementsByTagName('ymin')
                y1 = int(y1_list[0].childNodes[0].data)
                x2_list = box.getElementsByTagName('xmax')
                x2 = int(x2_list[0].childNodes[0].data)
                y2_list = box.getElementsByTagName('ymax')
                y2 = int(y2_list[0].childNodes[0].data)
                w = x2 - x1
                h = y2 - y1

                if x1<minx:
                    minx=x1
                if x2>maxx:
                    maxx=x2
                if y1<miny:
                    miny=y1
                if y2>maxy:
                    maxy=y2

            except Exception, e:
                print e

    img = Image.open(origin_img_file_path)
    width, height = img.size

    minX = max(0, minx)
    minY = max(0, miny)
    maxX = min(maxx, width)
    maxY = min(maxy, height)

    cropbox = (minX, minY, maxX, maxY)
    cropedimg = img.crop(cropbox)
    cropedimg.save(train_img_dir + img_file_name)