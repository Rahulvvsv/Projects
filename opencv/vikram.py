import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
image=mpimg.imread('hel.jpg')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_copy=np.copy(gray_image)
white=[]

for x in image_copy:
    temp=[]
    for y in x:
        if y<250:
            temp.append(0)
        else:
            temp.append(y)
    white.append(temp)

white_1=np.copy(white)
cv2.imshow("out",white_1)
cv2.waitKey(0)
cv2.imwrite('wh.jpg',white_1)
