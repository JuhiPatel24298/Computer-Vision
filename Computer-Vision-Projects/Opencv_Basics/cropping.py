# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
height , width = input.shape[:2]

x1 , y1 = int(width * 0.25) , int(height*0.25)
x2 , y2 = int(width * 0.75) , int(height*0.75)

new_image = input[x1:x2,y1:y2]

cv2.imshow('original image', input)
cv2.imshow('new cropped image', new_image)
cv2.waitKey()
cv2.destroyAllWindows()
