
import cv2
import numpy as np


hue =0
detect=0

def selsctcolor(event , x, y ,flag, param):
    global hue,detect
    #separite colors
    B=fram[y,x][0]
    G=fram[y,x][1]
    R=fram[y,x][2]
    if event == cv2.EVENT_LBUTTONDOWN:
        hue =hsv[y,x][0]
        detect =1


cv2.namedWindow('video')
cv2.setMouseCallback('video', selsctcolor)


vid=cv2.VideoCapture(0)

while True:
    _,fram = vid.read()
    
    hsv=cv2.cvtColor(fram ,cv2.COLOR_BGR2HSV)
    lower=np.array([hue-10, 50, 20])
    upper=np.array([hue +10,255,255])

    if detect == 1:
        mask =cv2.inRange(hsv,lower,upper)

        fram = cv2.bitwise_and(fram,fram,mask=mask)

    cv2.imshow('video',fram)

    key=cv2.waitKey(1)
    if key ==ord('q'):
        break
    elif key ==ord('r'):
        detect =0

cv2.destroyAllWindows()        