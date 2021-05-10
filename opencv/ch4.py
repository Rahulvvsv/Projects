import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)
print(img.shape)
img[100:520,200:400] = 200,200,255
cv2.line(img,(0,0),(200,520),(0,255,0),3) 
cv2.imshow('hello',img)
cv2.waitKey(0)
