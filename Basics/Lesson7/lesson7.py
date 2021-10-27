import cv2
import numpy as np

def main():
    resim = cv2.imread("android.jpg")

    resim = np.zeros((400,400,3),dtype="uint8")


    print(resim)
    cv2.rectangle(resim, (100, 300), (300, 100),(255, 255, 255), 3)
    iki_kat = cv2.pyrUp(resim)
    cv2.imshow("Resim", resim)
    cv2.imshow("Büyük Resim",iki_kat)



    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()