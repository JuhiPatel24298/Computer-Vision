# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = np.zeros((255,255),np.uint8)

for i in range(0,255):
    for j in range(0,255):
        image[i][j]= i
        
cv2.imshow('image',image)

# thresh Binary
ret,thresh_binary = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('ThreshBinary',thresh_binary)

#thresh binary inverse
ret,thresh_binary_inv = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('ThreshBinaryinv',thresh_binary_inv)

#thresh trunc
ret,thresh_trunc = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('ThreshTruncate',thresh_trunc)

#thresh tozero
ret,thresh_tozero = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow('threshtozero',thresh_tozero)

#thresh tozero inv
ret,thresh_tozero_inv = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('threshtozeroinv',thresh_tozero_inv)

cv2.waitKey()
cv2.destroyAllWindows()    
        
