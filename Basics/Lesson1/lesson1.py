import cv2
import numpy as np

resim = cv2.imread("seinfeld.jpg", )
resim2 = cv2.imread("seinfeld.jpg", 0)

cv2.imwrite("seinfeld_gri.jpg", resim)

cv2.imshow("Seinfeld Resmi",resim)
cv2.imshow("Seinfeld Gri Resmi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()