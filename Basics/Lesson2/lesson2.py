import cv2

resim = cv2.imread("cemkaraca.jpg", 0)


print(resim)
#print(type(resim))
#print(resim.size)
#print(resim.shape)

cv2.imshow("Cem Karaca",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()