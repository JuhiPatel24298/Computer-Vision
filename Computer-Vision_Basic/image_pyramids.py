# -*- coding: utf-8 -*-
import cv2

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
smaller = cv2.pyrDown(input)
cv2.imshow('smaller',smaller)

larger = cv2.pyrUp(smaller)
cv2.imshow('larger',larger)

cv2.waitKey()
cv2.destroyAllWindows()