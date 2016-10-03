import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while(1):

   ret,frame=cap,read()

   hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

   lower_blue=np.array([110,50,50])
   upper_blue=np.array([130,255,255])

   mask=cv2.inRange
 # 显示图像
 cv2.imshow('res',res)
 cv2.imshow('img',img)
 if cv2.waitKey(1 )& 0xFF ==27:
             break

 # 关闭窗口
cv2.destroyAllWindows()

