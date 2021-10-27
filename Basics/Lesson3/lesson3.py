import cv2
import numpy as np

resim = cv2.imread("kuzey.jpg")

bolge = resim[100:300,200:400]

#resim[0:200,0:200] = bolge
#resim[0:200,200:400] = bolge

#b,g,r = cv2.split(resim)

#yeni_resim = cv2.merge((b,g,r))
resim[:,:,0] = 255

#print(resim[50,50])
#print("Resim özelliği = " + str(resim.shape))
#print("Resim boyutu = " + str(resim.size))
#print("Resim bit değeri = " + str(resim.dtype))

cv2.imshow("Kuzey Tekinoğlu",resim)
#cv2.imshow("Kuzey Tekinoğlu Yeni",yeni_resim)



cv2.waitKey(0)
cv2.destroyAllWindows()