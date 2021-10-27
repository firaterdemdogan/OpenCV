import cv2
import numpy as np

camera = cv2.VideoCapture("neoluyola.mp4")

low = np.array([80,50,50])
high = np.array([130,255,255])


while True:

    ret,kare  = camera.read()

    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,low,high)

    final = cv2.bitwise_and(kare,hsv,mask=mask)

    cv2.imshow("BGR Ana",kare)

    cv2.imshow("Mask",mask)

    cv2.imshow("Son",final )

    cv2.imshow("HSV",hsv)




    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()