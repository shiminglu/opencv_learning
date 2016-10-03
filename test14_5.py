import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('chepai.jpg',1)

rows, cols, h = img.shape
#55,69    28 383    362 59  384 391
#94,100  88 178  408 73  394 143
pts1 = np.float32([[94,100],[88, 178],[408,73],[394,143]])
pts2 = np.float32([[0,0],[0,120],[350,0],[350,120]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(350,120))

#print(img.shape)

#print(plt.imshow(img))
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

