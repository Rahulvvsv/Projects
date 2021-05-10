import cv2
import numpy as np
import PIL as pil
from PIL import Image, ImageDraw, ImageFilter
from cv2 import VideoWriter, VideoWriter_fourcc
img = cv2.imread('kh.png')
print("size is "+str(img.size))
halfed = cv2.resize(img,(0,0),fx=0.1,fy=0.1)
width = 1280
height = 720
FPS = 24
seconds = 10
radius = 150
paint_h = int(height/2)
paint_w = 640
# def mask_circle_transparent(pil_img, blur_radius, offset=0):
#     offset = blur_radius * 2 + offset
#     mask = Image.new("L",pil_img.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
#     mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
#     result = pil_img.copy()
#     result.putalpha(mask)
#     return result
# Circled = mask_circle_transparent(img,2)
fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./Vikram.avi', fourcc, float(FPS), (width, height))

for paint_x in range(24*6):
    frame = np.zeros((height, width, 3),dtype=np.uint8)
    frame[:] = [200,200,255]
    frame[paint_h:paint_h+108,paint_w:paint_w+144]= halfed
    radius =  np.random.randint(0,255)
    cv2.circle(frame, (int(width/2), paint_h), radius ,(255, 0, 0), 1)
    video.write(frame)
video.release()
