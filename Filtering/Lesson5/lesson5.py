import cv2
import numpy as np


resim = cv2.imread("behzat.jpg")

mask = np.zeros(resim.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),dtype=np.float64)
fgdModel = np.zeros((1,65),dtype=np.float64)

rect = (250,0,400,300)

cv2.grabCut(resim,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 0 | (mask == 2)),0,1).astype(np.uint8)

resim = resim*mask2[:,:,np.newaxis]


cv2.imshow("Behzat",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
