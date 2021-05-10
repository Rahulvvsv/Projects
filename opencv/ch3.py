import cv2


img = cv2.imread('res/deto.png')
print(img.shape)
# imgres = cv2.resize(img,(595,335))

cv2.imshow('image',img)
# cv2.imshow('imageres',imgres)
## cropping an image
imgcropped = img[0:1000,0:500]
cv2.imshow('cropped',imgcropped)

cv2.waitKey(0)
