# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
height , width = input.shape[:2]
print(height , width)
new_height , new_width = height/4 , width/4

T = np.float32([[1 , 0, new_width],
                [0 , 1, new_height]])

translated_image = cv2.warpAffine(input,T,(width,height))

cv2.imshow('Translated image',translated_image)
cv2.waitKey()
cv2.destroyAllWindows()
