# -*- coding: utf-8 -*-
import cv2

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
print("shape",input.shape)
smaller_image = cv2.resize(input,None,fx=0.5,fy=0.5)
print("smaller_image shape",smaller_image.shape)
cv2.imshow('smaller_image',smaller_image)

larger_image = cv2.resize(input,None,fx=1.5,fy=1.5)
print("larger image shape",larger_image.shape)
cv2.imshow('larger_image',larger_image)


cv2.waitKey()
cv2.destroyAllWindows()
