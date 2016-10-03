import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('yuzhi.png',0)

#二值化
ret, thresh1 = cv2.threshold(img, 100, 150, cv2.THRESH_BINARY)
#反向二值化
ret, thresh2 = cv2.threshold(img, 100, 150, cv2.THRESH_BINARY_INV)
#截断
ret, thresh3 = cv2.threshold(img, 100, 150, cv2.THRESH_TRUNC)
#超过被置为0
ret, thresh4 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO)
#低于被置为0
ret, thresh5 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO_INV)

titles = ['original', 'binary', 'binary_inv', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
   plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()
   
