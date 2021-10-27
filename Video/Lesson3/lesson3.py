import cv2
import numpy as np


def main():

    camera = cv2.VideoCapture("neoluyola.mp4")

    fourcc = cv2.VideoWriter_fourcc(*"XVID") #format

    kayit = cv2.VideoWriter("kayit.avi",fourcc,30,(640,480))

    while True:
        ret,kare = camera.read()

        ters = cv2.flip(goruntu,0)

        if ret:
            kayit.write(kare)


        cv2.imshow("Sparring", kare)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()