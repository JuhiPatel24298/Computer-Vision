import cv2

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')
gray_image = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_image',gray_image)

cv2.waitKey()
cv2.destoryAllWindows()

