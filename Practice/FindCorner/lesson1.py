import numpy as np
import cv2

def main():

    resim= cv2.imread("zemin.jpg")
    resim_gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    resim_gri = np.float32(resim_gri)

    koseler = cv2.goodFeaturesToTrack(resim_gri,50,0.01,10)

    koseler = np.int0(koseler)

    for kose in koseler:
        x,y = kose.ravel()
        cv2.circle(resim,(x,y),3,(255,0,0),-1)

    cv2.imshow("resim",resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()