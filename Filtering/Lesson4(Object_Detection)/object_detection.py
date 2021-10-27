import cv2
import numpy as np

camera = cv2.VideoCapture("torba.mp4")

while True:
    ret , kare = camera.read()

    gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    obj = cv2.imread("torba.PNG",0)

    w,h = obj.shape

    res = cv2.matchTemplate(gri,obj,cv2.TM_CCOEFF_NORMED)

    esik = 0.8

    loc = np.where(res>esik)

    for i in zip(*loc[::-1]):
        cv2.rectangle(kare,i,(i[0]+h,i[1]+w),(0,255,0),2)
        cv2.putText(kare,"ALi",(i[0]+100,i[1]+100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),1)

    cv2.imshow("ekran",kare)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
