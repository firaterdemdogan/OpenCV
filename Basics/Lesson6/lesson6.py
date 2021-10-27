import cv2
import numpy as np

def main():

    feyyaz = cv2.imread("feyyaz.jpg")
    android = cv2.imread("../Lesson7/android.jpg")

    a_gri = cv2.cvtColor(android,cv2.COLOR_BGR2GRAY)


    h,w,c = android.shape

    ro1 =  feyyaz[0:h,0:w]
    cv2.imshow("RO1",ro1)

    ret,mask = cv2.threshold(a_gri,10,255,cv2.THRESH_BINARY)

    mask_inver = cv2.bitwise_not(mask)

    feyyazback = cv2.bitwise_and(ro1,ro1,mask = mask_inver)

    toplam = cv2.add(feyyazback,android)




    cv2.imshow("Sonuc",feyyazback)
    cv2.imshow("A",android)

    feyyaz[0:h,0:w] = toplam

    cv2.imshow("toplam", feyyaz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()