#reading images and videos
import cv2

input = cv2.imread('C:/Users/1640/Desktop/opencv-course-master/opencv-course-master/Resources/Photos/lady.jpg')

#cv2.imshow('Lady', input)

print(input.shape)
print("Height",input.shape[0],"pixels")
print("width",input.shape[1],"pixels")
#cv2.imwrite('C:/Users/1640/Desktop/Lady.jpg',input)

cv2.waitKey()
cv2.destroyAllWindows()
