import cv2
import numpy as np


img_dir="C:/Users/ASUS/Desktop/tmp/"
import random
def maybe_helmet(imgpath,img):
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    mask = mask0+mask1

    # set my output img to zero everywhere except my mask
    output_img = img.copy()
    output_img[np.where(mask==0)] = 0
    red_pixel_count=len(output_img[np.where(mask!=0)])
    other_pixel_count=len(output_img[np.where(mask==0)])
    red_ratio = float(red_pixel_count)/(red_pixel_count+other_pixel_count)
    print red_pixel_count,other_pixel_count
    print red_ratio
    # return red_ratio

    # cv2.imshow("", output_img)
    # # cv2.imshow("", img)
    # cv2.waitKey(0)

    #white color
    lower_white = np.array([0, 0, 0], dtype=np.uint8)
    upper_white = np.array([0, 0, 255], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(img_hsv, lower_white, upper_white)

    output_img = img.copy()
    output_img[np.where(mask == 0)] = 0
    white_pixel_count = len(output_img[np.where(mask != 0)])
    other_pixel_count = len(output_img[np.where(mask == 0)])
    white_ratio = float(white_pixel_count) / other_pixel_count
    print white_ratio
    os.rename(imgpath, img_dir + str(white_ratio) + "_" + str(random.randint(12, 20000)) + ".jpg")
    return white_ratio
    cv2.imshow("",output_img)
    cv2.waitKey(0)
import os
for img in os.listdir(img_dir):
    imgpath = img_dir+img
    img=cv2.imread(imgpath)
    maybe_helmet(imgpath,img)