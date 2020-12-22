# -*- coding: utf-8 -*-
import cv2
import numpy as np

def x_cordinate_centroid(contour):
    M =cv2.moments(contour)
    return int(M['m10']/M['m00'])

input = cv2.imread('contour_img.jpg')
grey = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(grey,10,70)

contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

sorted_LH = sorted(contours, key = x_cordinate_centroid , reverse = False)

for (i,c) in enumerate(sorted_LH):
     M = cv2.moments(c)
     cx = int(M['m10']/M['m00'])
     cy = int(M['m01']/M['m00'])
     cv2.drawContours(input,[c],-1,(255,0,0),5)
     cv2.putText(input,str(i+1),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),4)
     cv2.waitKey(0)
     cv2.imshow('output',input)

cv2.waitKey(0)
cv2.destroyAllWindows(0)     
     
    