import cv2
import numpy as np

img = cv2.imread('lena.jpg',0)

rows, cols = img.shape

#first 旋转中心，second 角度， 3：缩放因子
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)

dst = cv2.warpAffine(img, M, (cols, rows))

while(1):

 # 显示图像
 cv2.imshow('img',img)
 cv2.imshow('dst',dst) 
 if cv2.waitKey(1 )& 0xFF ==27:
             break

 # 关闭窗口
cv2.destroyAllWindows()

