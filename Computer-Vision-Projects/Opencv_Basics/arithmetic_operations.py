# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')

M = np.ones(input.shape,np.uint8)*175

darker_image = cv2.subtract(input,M)
brighter_image = cv2.add(input,M)

cv2.imshow('darker image',darker_image)
cv2.imshow('brighter image',brighter_image)

cv2.waitKey()
cv2.destroyAllWindows()
