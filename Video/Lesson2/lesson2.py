import cv2
import numpy as np

camera = cv2.VideoCapture("neoluyola.mp4")

camera.set(3,300)
camera.set(4,300)


def ayarlama(kare,yuzde = 75):
    genislik = int(kare.shape[1]* yuzde/75)
    yukseklik = int(kare.shape[0] * yuzde/100)
    boyut = (genislik,yukseklik)
    return  cv2.resize(kare,boyut,interpolation=cv2.INTER_AREA)



def main():

    while True:
        ret,kare = camera.read()

        gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

        kare2 = ayarlama(kare)

        cv2.imshow("Kare",kare)
        cv2.imshow("Gri",gri)
        cv2.imshow("New",kare2)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


