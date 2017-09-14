import os
import shutil
import xml.dom.minidom
from PIL import Image
import numpy as np
from xml.dom import minidom
import shutil

root_dir="D:/biaozhu_gongju/"
anno_dir=root_dir+"train/Annotations/"
img_dir=root_dir+"train/JPEGImages/"
test_images_dir=root_dir+"test_images/"

imglist = []
for img in os.listdir(img_dir):
    noext = os.path.splitext(img)[0]
    imglist.append(noext)

for img_ in os.listdir(test_images_dir):
    noext = os.path.splitext(img_)[0]
    if noext in imglist:
        imgpath = test_images_dir+img_
        os.remove(imgpath)

# annolist=[]
# for anno in os.listdir(anno_dir):
#     noext = os.path.splitext(anno)[0]
#     annolist.append(noext)
#
# print len(annolist)
# for img in os.listdir(img_dir):
#     noext = os.path.splitext(img)[0]
#     if noext=="08_31_247":
#         print "a"
#     if noext in annolist:
#         print img
#         shutil.copy(img_dir+img, test_images_dir + img)

