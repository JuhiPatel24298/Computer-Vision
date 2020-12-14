# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('shapes.jpg')

grey = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

#canny edge detection
canny = cv2.Canny(grey,20,70)
cv2.imshow('canny before contouring',canny)

#Contour finding
contours,hierarchy=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.imshow('canny after contouring',canny)
print('No of contours:',str(len(contours)))

cv2.drawContours(input,contours,-1,(0,0,255),5)
cv2.imshow('final',input)

cv2.waitKey()
cv2.destroyAllWindows()