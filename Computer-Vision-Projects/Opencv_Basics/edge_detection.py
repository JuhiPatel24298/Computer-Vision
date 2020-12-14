# -*- coding: utf-8 -*-
import cv2
import numpy as mp

input = cv2.imread('Lady.jpg',0)


# sobel
sobel_x = cv2.Sobel(input,cv2.CV_64F,0,1,ksize=5)
cv2.imshow('sobel_x',sobel_x)
sobel_y = cv2.Sobel(input,cv2.CV_64F,1,0,ksize=5)
cv2.imshow('sobel_y',sobel_y)
bitwise_OR = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('sobel',bitwise_OR)

#lapacian
laplacian = cv2.Laplacian(input,cv2.CV_64F)
cv2.imshow('laplacian',laplacian)

#canny 
canny = cv2.Canny(input,20,170)
cv2.imshow('Canny',canny)

cv2.waitKey()
cv2.destroyAllWindows()

