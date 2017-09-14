import cv2
import sys
import os
from PIL import Image

orig_images_dir = "D:/biaozhu_gongju/image_origin/"
image_save_dir = "D:/biaozhu_gongju/image/"
for img in os.listdir(orig_images_dir):
    img_path = orig_images_dir+img;
    image= cv2.imread(img_path)
    print img
    # width = image.shape[0]
    # height = image.shape[1]
    # M = cv2.getRotationMatrix2D((width/4, height/4), 270, 1)
    # resimg = cv2.warpAffine(image, M, (width, height))
    #
    #
    # # ratio = height/1000.0
    # resimg = cv2.resize(resimg, (image.shape[1]/3,image.shape[0]/3))
    # cv2.imshow("lena", resimg)
    # cv2.waitKey(0)
    #
    cv2.imwrite(image_save_dir+img,image)