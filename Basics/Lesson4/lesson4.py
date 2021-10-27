import cv2
import numpy as np

resim = cv2.imread("oldkuzey.jpg")


#Resim Uzatma

#uzatilan = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

#Resmi Aynalama

#aynala = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

#Resmi Tekrar Etme

#tekrar = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

#Resmi Etrafını Sarma

#sarma = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT,value = [255,255,255])


cv2.rectangle(resim,(500,200),(600,20),[0,0,255],2)










#face = resim[50:400,400:700]
#print(resim.shape)

cv2.imshow("Kuzey Orjinal",resim)
#cv2.imshow("Kuzey Uzatma",uzatilan)
#cv2.imshow("Kuzey Aynalama ",aynala)
#cv2.imshow("Kuzey Tekrarlama",tekrar)
#cv2.imshow("Kuzey Sarma",sarma)
#cv2.imshow("Kuzey'in sıfad",face)

cv2.waitKey(0)
cv2.destroyAllWindows()