import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

low = np.array([40,50,50])
high = np.array([75,255,255])


resim1 = cv2.imread("agac.jpg")
#resim2 = cv2.imread("img2.png")

img_hsv = cv2.cvtColor(resim1, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(resim1,cv2.COLOR_BGR2GRAY)

#img_hsv2 = cv2.cvtColor(resim2, cv2.COLOR_BGR2HSV)

img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)


mask = cv2.inRange(img_hsv,low,high)
#mask2 = cv2.inRange(img_hsv2,low,high)
corners = cv2.goodFeaturesToTrack(mask,300,0.001,20)
corners = np.int0(corners)
counter = 0

for corner in corners:

    x,y = corner.ravel()


    cv2.circle(resim1,(x,y),3,(255,0,0),-1)
    counter += 1


edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

# Display Canny Edge Detection Image

cv2.imshow('Canny Edge Detection', edges)

cv2.imshow("Final",resim1)
#cv2.imshow("Test2",resim2)
cv2.imshow("Blur",img_blur)
#cv2.imshow("Final2",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()