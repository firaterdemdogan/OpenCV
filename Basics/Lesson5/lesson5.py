import cv2
import numpy as np

def main():

    resim1 = cv2.imread("on.jpg")
    resim2 = cv2.imread("arka.jpg")

    #print("Ön Yüz Resim Değerleri Yükseklik : {} , Genişlik {}, Kanal Sayısı : {}".format(resim1.shape[0],resim1.shape[1],resim1.shape[2]))
    #print("Ön Yüz Resim Değerleri Yükseklik : {} , Genişlik {}, Kanal Sayısı : {}".format(resim2.shape[0],resim2.shape[1],resim2.shape[2]))
    #print(resim1[500,400])
    #print(resim2[500,400])

    toplam = (cv2.add(resim1,resim2))

    #Ağılıklı toplam

    agirlikli = cv2.addWeighted(resim1,0.4,resim2,0.6,0)


    cv2.imshow("onyuz",resim1)
    cv2.imshow("arka",resim2)

    #cv2.imshow("toplam",toplam)
    cv2.imshow("Ağırlıklı Toplam", agirlikli)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()