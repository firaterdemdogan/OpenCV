import cv2
import numpy as np

camera = cv2.VideoCapture("neoluyola.mp4")

low = np.array([90,50,50])
high = np.array([120,255,255])


while True:

    ret,kare = camera.read()

    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,low,high)

    final = cv2.bitwise_and(kare,hsv,mask = mask)


    #smoothed

    kernel = np.ones((15,15),dtype=np.float32)/255

    smoothed = cv2.filter2D(final,-1,kernel)

    #blur

    blur= cv2.GaussianBlur(final,(15,15),0)

    #median

    median = cv2.medianBlur(final,15)

    #bilateral

    bilateral = cv2.bilateralFilter(final,15,75,75)

    #cv2.imshow("BGR Ana",kare)

    #cv2.imshow("Mask",mask)

    cv2.imshow("Son",final)

    cv2.imshow("blur",blur)

    cv2.imshow("median",median)

    cv2.imshow("smoothed",smoothed)

    cv2.imshow("bilateral",bilateral)

    #cv2.imshow("HSV",hsv)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
print(kernel)
camera.release()
cv2.destroyAllWindows()