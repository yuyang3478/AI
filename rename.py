import os
import datetime
root_dir="D:/biaozhu_gongju/"
anno_dir=root_dir+"Annotations/"
img_dir="I:/pictures1/"
targ_img_dir="I:/p1rename/"


count=247
for img in os.listdir(img_dir):
    print img
    if not img.endswith(".jpg"):
        continue
    # os.rename(xmlfile,train_anno_dir+datetime.datetime.now().strftime('%m_%d_')+str(count)+'.xml')
    os.rename(img_dir+img, targ_img_dir + datetime.datetime.now().strftime('%m_%d_') + str(count) + '.jpg')
    count+=1