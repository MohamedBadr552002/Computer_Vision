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



black = np.zeros((400,400),dtype='uint8')

rect = CV.rectangle(black.copy(), (30,20),(270,280),255,-1)
cir = CV.circle(black.copy() ,(270,280),40,255 ,-1)

_and = CV.bitwise_and(rect, cir)

CV.imshow("and",_and)

CV.imshow("rec",rect)
CV.imshow("cir",cir)

CV.waitKey(0)
