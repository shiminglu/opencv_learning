import cv2
import numpy as np

cv2.useOptimized()

img1 = cv2.imread('lena.jpg')

e1 = cv2.getTickCount()

for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()

time = (e2 - e1)/ cv2.getTickFrequency()

print time

cv2.setUseOptimized(False)
#cv2.useOptimized()

img1 = cv2.imread('lena.jpg')

e1 = cv2.getTickCount()

for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()

time = (e2 - e1)/ cv2.getTickFrequency()

print time
