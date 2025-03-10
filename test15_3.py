import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('noisy.png',0)





ret1, th1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img1, (5, 5), 0)

ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img1, 0, th1,
          img1, 0, th2,
          blur, 0, th3]
titles = ['original', 'Histogram', 'global(v=127)',
          'original', 'Histogram', "Otsu's",
          'Gaussian', 'Histogram', "Otsu's"]

for i in range(3):
   plt.subplot(3,3,i*3+1), plt.imshow(images[i*3], 'gray')
   plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
   plt.subplot(3,3,i*3+2), plt.hist(images[i*3].ravel(), 256)
   plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])
   plt.subplot(3,3,i*3+3), plt.imshow(images[i*3+2], 'gray')
   plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])   
plt.show()
   


while(1):

 # 显示图像
 cv2.imshow('img',img)
 cv2.imshow('dst',dst)
 cv2.imshow('img1',img1) 
 if cv2.waitKey(1 )& 0xFF ==27:
             break

 # 关闭窗口
cv2.destroyAllWindows()

