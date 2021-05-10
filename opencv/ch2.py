import cv2
import numpy as np
img = cv2.imread('res/todoroki.jpg')
# converting images to gray
# using the comvert color funciton
## defining kernel to use it in dilation
kernel = np.ones((5,5),np.uint8)
imgray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
IMGB = cv2.GaussianBlur(img,(7,7),0)
IMGCANN =   cv2.Canny(img,100,100)
imgdil  = cv2.dilate(IMGCANN,kernel,iterations=1)
# cv2.imshow('ORIGINAL',img)
cv2.imshow('image',imgray)
cv2.imshow('blurimage',IMGB)
cv2.imshow('cannyimage',IMGCANN)
cv2.imshow('dilimage',imgdil)



cv2.waitKey(0)
