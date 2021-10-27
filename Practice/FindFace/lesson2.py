import cv2
import  numpy as np

camera = cv2.VideoCapture("agalar.mp4")
#fourcc = cv2.VideoWriter_fourcc(* "XVID")
#kayit = cv2.VideoWriter("kayit.avi",fourcc,20,(640,480))

while True:
    ret,kare = camera.read()
    yuz_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    goz_casc = cv2.CascadeClassifier("haarcascade_eye.xml")



#resim = cv2.imread("bilim.jpg")

    gri_ton = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_casc.detectMultiScale(gri_ton,1.1,4)

#print(yuzler)

    for (x,y,w,h) in yuzler:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)
        yuz_bolgesi = kare[y:y+h,x:x+w]
        griyuz = cv2.cvtColor(yuz_bolgesi,cv2.COLOR_BGR2GRAY)
        gozler = goz_casc.detectMultiScale(griyuz,1.1,4)
        for (a,b,c,d) in gozler:
            cv2.rectangle(yuz_bolgesi,(a,b),(a+c,b+d),(0,255,0),2)
#kayit.write(resim)
    cv2.imshow("resim",kare)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()