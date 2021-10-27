import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()

    #cv2.rectangle(kare, (100, 200), (200, 100), (255, 0, 0), 2)

    bolge = kare[0:200,0:200]
    cv2.imshow("Video",kare)
    cv2.imshow("Bolge",bolge)



    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()