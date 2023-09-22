import cv2 as CV
import numpy as np


def resizing_frame(frame,scale=0.75): #this function for image , videoes,live videoes
    #change the dimentions
    height=int(frame.shape[0] * scale)
    width=int(frame.shape[1] * scale)

    #make a tuple for both dimentions
    dimention=(height,width)

    #apply changing  
       # interpolation ==>The function resize resizes the image src down to or up to the specified size
    return CV.resize(frame,dimention,interpolation=CV.INTER_AREA)



img =   CV.imread("logo.png")
img = resizing_frame(img,0.25)
gray = CV.cvtColor(img , CV.COLOR_BGR2HSV)
_img = CV.cvtColor(gray, CV.COLOR_HSV2BGR)

CV.imshow("window", gray)
CV.imshow("window2", _img)
CV.waitKey(0)