import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg',1)

rows, cols, h= img.shape

print(img.shape)
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,220]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))
print(img.shape)

print(plt.imshow(img))
#plt.subplot(500,plt.imshow(img),plt.title('Input'))
#plt.subplot(400,plt.imshow(dst),plt.title('Output'))
#plt.show()


while(1):

 # 显示图像
 cv2.imshow('img',img)
 cv2.imshow('dst',dst) 
 if cv2.waitKey(1 )& 0xFF ==27:
             break

 # 关闭窗口
cv2.destroyAllWindows()

