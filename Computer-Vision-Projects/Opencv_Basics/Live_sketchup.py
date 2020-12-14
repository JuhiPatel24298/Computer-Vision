# -*- coding: utf-8 -*-
import cv2
import numpy as np

def sketch(image):
    
    input = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(input,(5,5),0)
    
    edges = cv2.Canny(blurred,10,70)
    
    ret,thresh = cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)
    return(thresh)


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow('Live Sketchup',sketch(frame))
    if cv2.waitKey(1)==13:
        break
    
cap.release()
cv2.destroyAllWindows()
