import cv2
##declaring the variable to store the image
img = cv2.imread("res/todoroki.jpg")
## imread is a function in open cv to read images
## to display there is another functoin
## in cv2.show we need to send two arguments first one is name of the display and the file which we want to display
cv2.imshow('Output',img)
## the image will come and go instantly
## inorder to delay the closing of the image we need to use antoher function of the cv2 (in milli seconds)
cv2.waitKey(0)
##0 means infinite time
## READING A image
## to use a webcam instead of directory tyoe 0
cap = cv2.VideoCapture('res/hello.mkv')
# cap = cv2.VideoCapture(0)
## we can define specific size by cap.set(3,640) 3 for width
# cap.set(4,480)
# to change the brightness the id is 10  cap.set(10,100)
# cap.set(10,0.1)
##vvideo is a group of images shown faster
## so wee meeed to images in a while loop
while True:
    success,img1 = cap.read()
##success will tell well the process is done or not
## img1 will store the file
    cv2.imshow('output',img1)
    
## to break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('hello')
        break
