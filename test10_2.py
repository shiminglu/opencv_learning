import cv2
import numpy as np

cv2.useOptimized()


e1 = cv2.getTickCount()

img1 = cv2.imread('opencv.jpg')
img2 = cv2.imread('lena.jpg')

img = img1[0:220,0:220]

dst = cv2.addWeighted(img, 0.5, img2, 0.8, 0)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

cv2.imshow('dst', dst)

print (time)
print (e1,e2)

cv2.waitKey(0)
cv2.destoryAllWindow()
