# -*- coding: utf-8 -*-
import cv2
import numpy as np

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
B , G , R = input[0,0]
print(B,G,R)
print("shape",input.shape)

cv2.waitKey()
cv2.destroyAllWindows()
#-----------------------------------------------------------------------------------------------
hsv_image = cv2.cvtColor(input,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv_image',hsv_image)
H,S,V = hsv_image[0,0]
print(H,S,V)

cv2.waitKey()
cv2.destroyAllWindows()
#----------------------------------------------------------------------------------------------
H , S , V = cv2.split(hsv_image)
cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.imshow('Value',V)
cv2.waitKey()
cv2.destroyAllWindows()
#---------------------------------------------------------------------------------------
new_merged = cv2.merge([H,S,V])
cv2.imshow('new_merged',new_merged)
cv2.waitKey()
cv2.destroyAllWindows()
#---------------------------------------------------------------------------------------
B , G , R = cv2.split(input)
zeros = np.zeros(input.shape[:2],dtype = 'uint8')
cv2.imshow('blue',cv2.merge([B,zeros,zeros]))
cv2.waitKey()
cv2.destroyAllWindows() 