# -*- coding: utf-8 -*-
import os
import xml.dom.minidom
root_dir="D:/biaozhu_gongju/"
anno_dir=root_dir+"Annotations/"
img_dir=root_dir+"JPEGImages/"
train_dir=root_dir+"train/"
train_anno_dir=train_dir+"Annotations/"
train_img_dir=train_dir+"JPEGImages/"
imageSets_dir=train_dir+"ImageSets/Main/"
labels=set([])
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
        labels.add(objectname)
print labels
print len(labels)
count=1
with open(train_dir+"p_label_map.pbtxt","w") as f:
    for label in labels:
        f.write("item {\n")
        f.write("  id:"+str(count)+"\n")
        f.write("  name:'"+label+"'\n")
        f.write("}\n")
        print count
        count+=1
