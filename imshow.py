import numpy as np
import cv2
 
#read img
img = cv2.imread('/home/lsm/Documents/opencv_learning/lena.jpg')


#show img
#change window
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

