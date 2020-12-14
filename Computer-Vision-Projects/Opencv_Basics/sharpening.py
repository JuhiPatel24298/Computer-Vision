# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
kernel = np.array([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]])

sharp = cv2.filter2D(input,-1,kernel)
cv2.imshow('sharpened_image',sharp)

cv2.waitKey()
cv2.destroyAllWindows()