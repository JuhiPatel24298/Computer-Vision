# -*- coding: utf-8 -*-
import cv2
import numpy as np

def sort_contours_area(contours):
    all_area=[]
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_area.append(area)
    return all_area



input = cv2.imread('C:/Users/1640/Desktop/opencv/Opencv_Basics/contour_img.jpg')

gray = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray,10,70)
cv2.imshow('Canny',canny)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
final = cv2.drawContours(input.copy(),contours,-1,(255,0,0),5)
cv2.imshow('final',final)

# contour area before sorting
print('Contour Area before Sorting', sort_contours_area(contours))

sorting_contours = sorted(contours, key=cv2.contourArea , reverse = True)

print('Contour Area after sorting', sort_contours_area(sorting_contours))

for c in sorting_contours:
    cv2.drawContours(input,[c],-1,(255,0,0),5)
    cv2.waitKey(0)
    cv2.imshow('sorted_image', input)
    
cv2.waitKey()
cv2.destroyAllWindows()