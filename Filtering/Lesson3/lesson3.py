import cv2
import numpy as np

camera = cv2.VideoCapture("neoluyola.mp4")

low = np.array([88,50,50])
high = np.array([130,255,255])

while True:
    ret,kare = camera.read()

    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,low,high)

    final = cv2.bitwise_and(kare,hsv,mask = mask)

    kernel = np.ones((5,5),np.uint8)

    erosion = cv2.erode(mask,kernel,iterations=1)

    diolation = cv2.dilate(mask,kernel,iterations=1)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)



    cv2.imshow("Mask",mask)
    cv2.imshow("son",final)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()