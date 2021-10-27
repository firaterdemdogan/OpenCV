import cv2
import numpy as np

resim = cv2.imread("ezel.jpg")

gri_ton = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

alt_beden = cv2.CascadeClassifier("haarcascade_lowerbody.xml")

bedenler = alt_beden.detectMultiScale(gri_ton,1.1,3)

for (x,y,w,h) in bedenler:
    cv2.rectangle(resim,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()