import cv2

import numpy as np

camera = cv2.VideoCapture("torba.mp4")

while True:

    ret,kare = camera.read()

    laplacian = cv2.Laplacian(kare,cv2.CV_64F)

    kenarlar = cv2.Canny(kare,50,200)

    cv2.imshow("kare",kare)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

    cv2.imshow("Kenarlar", kenarlar)
#laplacian
#laplacian =cv2.Laplacian(resim,cv2.CV_64F)

#sobel
#sobel_dikey = cv2.Sobel(resim,cv2.CV_64F,0,1,ksize=5)

cv2.waitKey(0)
cv2.destroyAllWindows()