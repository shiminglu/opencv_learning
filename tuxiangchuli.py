import numpy as np
import cv2


img = cv2.imread('/home/lsm/Documents/opencv_learning/lena.jpg')

#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.imwrite('messigray.png',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#img=np.zeros((600,900,3),np.uint8)

#cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#img[100,100]=[255,0,122]

###print img.item(10,10,2)
###img.itemset((10,10,2),100)
###print img.item(10,10,2)

#bal = img[1:10,11:20]
#img[31:40,41:50]=ball

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
#cv2.imwrite('messigray.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


