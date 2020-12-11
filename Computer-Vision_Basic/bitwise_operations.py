# -*- coding: utf-8 -*-
import cv2
import numpy as np

image1 = np.zeros((300,300),np.uint8)
image2 = np.zeros((300,300),np.uint8)

square = cv2.rectangle(image1,(100,150),(200,250),(255,255,255),-1)
circle = cv2.circle(image2, (150,150),100,(255,255,255),-1)

cv2.imshow('image1',image1)
cv2.imshow('image2',image2)

#bitwise operations

And = cv2.bitwise_and(image1,image2)
OR = cv2.bitwise_or(image1,image2)
XOR = cv2.bitwise_xor(image1,image2)
NOT = cv2.bitwise_not(image1)

cv2.imshow('bitwise_and',And)
cv2.imshow('bitwise_or',OR)
cv2.imshow('bitwise_xor',XOR)
cv2.imshow('bitwise_not',NOT)


cv2.waitKey()
cv2.destroyAllWindows() 

