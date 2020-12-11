# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
cv2.imshow('original image',input)

kernel_3x3 = np.ones((3,3),np.float32)/9
blurred_image = cv2.filter2D(input,-1,kernel_3x3)
cv2.imshow('kernel_3x3',blurred_image)

kernel_7x7 = np.ones((7,7),np.float32)/49
blurred_image1 = cv2.filter2D(input,-1,kernel_7x7)
cv2.imshow('kernel_7x7',blurred_image1)



#blurring functions

blurr = cv2.blur(input,(3,3))
cv2.imshow('blurr function',blurr)

g_blurr = cv2.GaussianBlur(input,(7,7),0)
cv2.imshow('Gaussian Blur',g_blurr)

cv2.waitKey()
cv2.destroyAllWindows()