import cv2
import numpy as np

img = cv2.imread('lena.jpg')

res = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)


#height,width=img.shape[:2]

#res = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

while(1):
 # 显示图像
 cv2.imshow('res',res)
 cv2.imshow('img',img)
 if cv2.waitKey(1 )& 0xFF ==27:
             break

 # 关闭窗口
cv2.destroyAllWindows()

