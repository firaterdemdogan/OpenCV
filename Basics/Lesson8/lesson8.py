import cv2
import numpy as np

def main():

    resim = np.zeros((400,400,3),dtype="uint8")
    resim.fill(255)

    cv2.line(resim,(0,0),(200,200),(2550,0,0),2)
    cv2.circle(resim,(200,200),50,(0,255,0),2)
    cv2.putText(resim,"Gaddar Feyyaz",(100,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.rectangle(resim,(150,250),(250,150),(150,150,150),2)
    cv2.imshow("Arka Plan ",resim)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()