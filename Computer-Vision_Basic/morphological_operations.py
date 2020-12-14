# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('juhi.jpg')
cv2.imshow('original',input)

kernel = np.array((5,5), np.uint8)

#erosion
erosion = cv2.erode(input,kernel, iterations = 1)
cv2.imshow('erosion',erosion)

#dilution
dilation = cv2.dilate(input,kernel, iterations = 1)
cv2.imshow('dilation',dilation)

#opening
opening = cv2.morphologyEx(input,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)

#closing
closing = cv2.morphologyEx(input,cv2.MORPH_CLOSE,kernel)
cv2.imshow('closing',closing)

cv2.waitKey()
cv2.destroyAllWindows()
