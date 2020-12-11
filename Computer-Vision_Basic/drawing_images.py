# -*- coding: utf-8 -*-
import cv2
import numpy as np

image_color = np.zeros((512,512,3),np.uint8)
image_gray = np.zeros((512,512),np.uint8)
#cv2.imshow('image_gray',image_gray)

cv2.line(image_color,(0,256),(170,0),(33,67,101),5)
cv2.line(image_color,(170,0),(256,256),(33,67,101),5)
cv2.line(image_color,(340,0),(256,256),(33,67,101),5)
cv2.line(image_color,(340,0),(512,256),(33,67,101),5)

cv2.rectangle(image_color,(350,350),(470,450),(33,67,101),5)
cv2.line(image_color,(350,350),(410,290),(33,67,101),5)
cv2.line(image_color,(470,350),(410,290),(33,67,101),5)

cv2.circle(image_color,(250,100),25,(33,67,101),5)
pts = np.array([[344,344],[234,123],[457,382],[984,234]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image_color,[pts],True,(33,67,101),5)

cv2.imshow('image_color',image_color)
cv2.waitKey()
cv2.destroyAllWindows()

