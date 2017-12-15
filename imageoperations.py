#https://www.youtube.com/watch?v=1pzk_DIL_wo
#Tutorial 4 - Image Operations

import numpy as np
import cv2

img = cv2.imread('watch.jfif', cv2.IMREAD_COLOR)

#defines px as a specific point on the image then sets it equal to white
px = img[55,55]
img[55,55] = [255,255,255]
#print(px)

#ROI - Region Of image
#this sets var roi equal to a region of the image from these coordinates then makes the entire region white
roi = img[100:150, 100:150]
img[100:150, 100:150] = [255,255,255]

#defines a region of the image and then remaps it
#make sure the dimensions of the remap are the same as the defined region (watch_face)!
#for instance, 111-37 = 74 and 194 - 107 = 87
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
