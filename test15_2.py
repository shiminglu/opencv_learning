import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('chepai.jpg',0)

pts1 = np.float32([[94,100],[88, 178],[408,73],[394,143]])
pts2 = np.float32([[0,0],[0,120],[350,0],[350,120]])

M = cv2.getPerspectiveTransform(pts1,pts2)

img1 = cv2.warpPerspective(img,M,(350,120))

#中值滤波
img1 = cv2.medianBlur(img1, 5)

ret, th1 = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY)

#11 :block size  2:C值
th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)

th3 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

images = [img1,th1,th2,th3]
titles = ['original', 'global(v=127)',
          'adaptive', 'adaptive']

for i in range(4):
   plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()
   


 # 关闭窗口
cv2.destroyAllWindows()

