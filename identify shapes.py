
from pickletools import uint8
import cv2
import numpy as np



vid=cv2.VideoCapture(0)


while True:
    _ ,fram=vid.read()
   # fram= cv2.resize(fram,(500,500))
    gray=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)

    #_ , thresh =cv2.threshold(gray,180,255,cv2.THRESH_BINARY)

    canny=cv2.Canny(gray,150,255)
    
    contours1,hierarchies =cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    #contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours1:
        approx =  cv2.approxPolyDP(contour , 0.01*cv2.arcLength(contour,True),True)
        cv2.drawContours(fram , [approx], 0 ,(255,0,0),1)

        x= approx.ravel()[0]
        y=approx.ravel ()[1]

        font=cv2.FONT_HERSHEY_COMPLEX

        #identify shapes by text
        if len(approx) == 3:
            cv2.putText(fram,"Triangle",(x,y),font,0.5,(0,255,0))
        elif len(approx) == 4:
               cv2.putText(fram,"Rectangle",(x,y),font,0.5,(0,255,0))

        elif len(approx) == 5:
               cv2.putText(fram,"Pologun",(x,y),font,0.5,(90,173,140))    
        elif len(approx) == 10:
               cv2.putText(fram,"star",(x,y),font,0.5,(0,0,255))
        else:    
            cv2.putText(fram,"circle",(x,y),font,0.5,(234,255,34))   


    cv2.imshow('canny edges',canny)
    cv2.imshow('video',fram)
    
    key =cv2.waitKey(1)
    if key == ord('q'):
        break


cv2.destroyAllWindows()    