# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
height , width = input.shape[:2]

M = cv2.getRotationMatrix2D((width/2,height/2),45,0.5)
rotated_image = cv2.warpAffine(input, M , (width,height))

cv2.imshow('Rotated_image',rotated_image)

cv2.waitKey()
cv2.destroyAllWindows()