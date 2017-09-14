# -*- coding:utf-8 -*-
import os
import shutil
import minidom
from PIL import Image
import datetime
import numpy as np
# from xml.dom import minidom
root_dir="D:/biaozhu_gongju/"
# anno_dir=root_dir+"Annotations/"train\stage2\test_gene_annotations
img_dir=root_dir+"JPEGImages/"
train_dir=root_dir+"train/"
train_anno_dir=train_dir+"Annotations/"
train_img_dir=train_dir+"JPEGImages/"

anno_dir=train_dir+"stage2/test_gene_annotations/"
# remove_img_dir = "D:/biaozhu_gongju/tmp/"

#拷贝图片到目标目录,转换文件格式
def copyImage2targetdir(img_file_name,target_file_name):
    origin_img_file_path = img_dir + img_file_name
    if not os.path.exists(origin_img_file_path):
        img_file_name = os.path.splitext(anno_file_name)[0] + ".bmp"
        Image.open(img_dir+img_file_name).save(train_img_dir+target_file_name)
    else:
        shutil.copy (origin_img_file_path, train_img_dir+target_file_name)
count = 1
#处理并拷贝标注数据文件到train目录
for anno_file_name in os.listdir(anno_dir):
    print anno_file_name
    #读取原标注文件内容，过滤并生成新的标注文件
    xmlfile = anno_dir + anno_file_name
    DomTree = minidom.parse(xmlfile)
    annotation = DomTree.documentElement

    # 得到dom对象，test为根元素
    imp = minidom.getDOMImplementation()
    dom = imp.createDocument(None, 'annotation', None)
    # 转化为element实例
    root = dom.documentElement

    folderlist = annotation.getElementsByTagName('folder')  # [<DOM Element: filename at 0x381f788>]
    folder = "VOC2012"#folderlist[0].childNodes[0].data
    elem = dom.createElement('folder')
    text = dom.createTextNode(folder)
    elem.appendChild(text)
    root.appendChild(elem)

    # filenamelist = annotation.getElementsByTagName('filename')  # [<DOM Element: filename at 0x381f788>]
    filename = os.path.splitext(anno_file_name)[0]+".jpg"#datetime.datetime.now().strftime('%m_%d_') + str(count) + '.jpg'#filenamelist[0].childNodes[0].data
    elem = dom.createElement('filename')
    text = dom.createTextNode(filename)
    elem.appendChild(text)
    root.appendChild(elem)

    pathlist = annotation.getElementsByTagName('path')  # [<DOM Element: filename at 0x381f788>]
    path = pathlist[0].childNodes[0].data
    elem = dom.createElement('path')
    text = dom.createTextNode(path)
    elem.appendChild(text)
    root.appendChild(elem)

    databaselist = annotation.getElementsByTagName('database')
    database = databaselist[0].childNodes[0].data
    elem = dom.createElement('source')
    text = dom.createTextNode(database)
    elem1 = dom.createElement('database')
    elem1.appendChild(text)
    elem.appendChild(elem1)
    root.appendChild(elem)

    elem = dom.createElement('size')
    widthlist = annotation.getElementsByTagName('width')
    width = widthlist[0].childNodes[0].data
    text = dom.createTextNode(width)
    elem1 = dom.createElement('width')
    elem1.appendChild(text)
    elem.appendChild(elem1)
    heightlist = annotation.getElementsByTagName('height')
    height = heightlist[0].childNodes[0].data
    text = dom.createTextNode(height)
    elem1 = dom.createElement('height')
    elem1.appendChild(text)
    elem.appendChild(elem1)
    text = dom.createTextNode('3')
    elem1 = dom.createElement('depth')
    elem1.appendChild(text)
    elem.appendChild(elem1)
    root.appendChild(elem)

    elem = dom.createElement('segmented')
    text = dom.createTextNode('0')
    elem.appendChild(text)
    root.appendChild(elem)

    hashelmet=False
    objectlist = annotation.getElementsByTagName('object')
    for objects in objectlist:
        # print objects
        namelist = objects.getElementsByTagName('name')
        # print 'namelist:',namelist
        objectname = namelist[0].childNodes[0].data
        # if not (objectname=="nhelmet" or objectname=="helmet"):
        #     continue
        if objectname == "o":
            objectname = "0"
        if objectname == "i":
            objectname = "1"
        if objectname == "ao":
            objectname = "yue"
        if objectname == "z":
            objectname = "7"
        if objectname == "a":
            objectname = "4"
        if objectname == "s":
            objectname = "5"
        if objectname == "-":
            continue
        hashelmet=True
        # print objectname
        elem = dom.createElement('object')
        text = dom.createTextNode(objectname)
        elem1 = dom.createElement('name')
        elem1.appendChild(text)
        elem.appendChild(elem1)
        text = dom.createTextNode('Unspecified')
        elem1 = dom.createElement('pose')
        elem1.appendChild(text)
        elem.appendChild(elem1)
        text = dom.createTextNode('0')
        elem1 = dom.createElement('truncated')
        elem1.appendChild(text)
        elem.appendChild(elem1)
        text = dom.createTextNode('0')
        elem1 = dom.createElement('difficult')
        elem1.appendChild(text)
        elem.appendChild(elem1)

        bndbox = objects.getElementsByTagName('bndbox')
        cropboxes = []
        for box in bndbox:
            try:
                x1_list = box.getElementsByTagName('xmin')
                x1 = int(x1_list[0].childNodes[0].data)
                # x1=max(0,x1-2)
                y1_list = box.getElementsByTagName('ymin')
                y1 = int(y1_list[0].childNodes[0].data)
                # y1=max(0,y1-2)
                x2_list = box.getElementsByTagName('xmax')
                x2 = int(x2_list[0].childNodes[0].data)
                # x2=min(width,x2+2)
                y2_list = box.getElementsByTagName('ymax')
                y2 = int(y2_list[0].childNodes[0].data)
                # y2=min(height,y2+2)

                elem1 = dom.createElement('bndbox')
                text = dom.createTextNode(str(x1))
                elem2 = dom.createElement('xmin')
                elem2.appendChild(text)
                elem1.appendChild(elem2)
                text = dom.createTextNode(str(y1))
                elem2 = dom.createElement('ymin')
                elem2.appendChild(text)
                elem1.appendChild(elem2)
                text = dom.createTextNode(str(x2))
                elem2 = dom.createElement('xmax')
                elem2.appendChild(text)
                elem1.appendChild(elem2)
                text = dom.createTextNode(str(y2))
                elem2 = dom.createElement('ymax')
                elem2.appendChild(text)
                elem1.appendChild(elem2)
                elem.appendChild(elem1)


            except Exception, e:
                print e

        root.appendChild(elem)
    if hashelmet == False:
        continue
    img_file_name = os.path.splitext(anno_file_name)[0] + ".jpg"
    # target_file_name = datetime.datetime.now().strftime('%m_%d_') + str(count) + '.jpg'
    # copyImage2targetdir(img_file_name,target_file_name)
    # 读写文件的句柄
    target_anno_name = anno_file_name#datetime.datetime.now().strftime('08_31_') + str(count) + '.xml'
    fileHandle = open(train_anno_dir+target_anno_name, 'w')
    # 写入操作，第二个参数为缩进（加在每行结束后），第三个为增量缩进（加在每行开始前并增量）
    dom.writexml(fileHandle, '\n', ' ', '')

    # fileHandle.write('\n')
    # fileHandle.write(elem.toprettyxml())
    fileHandle.close()
    count += 1
