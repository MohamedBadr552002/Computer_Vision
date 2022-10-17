from pickle import FRAME
import cv2
import numpy as np





def nothing():
    pass

def tranformation(phot ,x=0,y=0 ):
    #-x -->left
    #-y -->up
    #+x -->right
    #+y -->down
    x = cv2.getTrackbarPos('x_shift','vedio')
    y=  cv2.getTrackbarPos('y_shift','vedio')
    transMat=np.float32([[1,0,x],[0,1,y]])
                #(weidth,height)    
    dimantions=(phot.shape[1],phot.shape[0])
        #warpAffine(image, t_matrix,tuple of dimantions)
    shifted_image =cv2.warpAffine(phot,transMat,dimantions)
    cv2.imshow('vedio',shifted_image)
        

#translated = tranformation(img,100,100)
#cv2.imshow('translat',translated)


#function to rotate 
def funcRotate(fram,degree=0):
    height, width = fram.shape[:2]
    
    while True:
        success,fram=cam.read()
        degree = cv2.getTrackbarPos('rotater','vedio')
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
        rotated_image = cv2.warpAffine(fram, rotation_matrix, (width, height))
        cv2.imshow('vedio', rotated_image)
        k=cv2.waitKey(1)
        if k == ord('t'):
            break


    return    

    






cv2.namedWindow('vedio')

# create trackbar(bar name , window name ,start value ,end value,function)

degree=0


cv2.createTrackbar('rotater','vedio',0,360,funcRotate)
cv2.createTrackbar('x_shift','vedio',0,550,tranformation)
cv2.createTrackbar('y_shift','vedio',0,500,tranformation)


cam=cv2.VideoCapture(0)
success,fram=cam.read()

height, width = fram.shape[:2]

dimantions=(fram.shape[1],fram.shape[0])

while True:
    success,fram=cam.read()
    k=cv2.waitKey(1)
    
    ''' for rotation'''
    degree = cv2.getTrackbarPos('rotater','vedio')
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    fram = cv2.warpAffine(fram, rotation_matrix, (width, height))



    ''' for shifting'''
    #-x -->left
    #-y -->up
    #+x -->right
    #+y -->down
    x = cv2.getTrackbarPos('x_shift','vedio')
    y=  cv2.getTrackbarPos('y_shift','vedio')
    transMat=np.float32([[1,0,x],[0,1,y]])
                #(weidth,height)    
    
        #warpAffine(image, t_matrix,tuple of dimantions)
    fram =cv2.warpAffine(fram,transMat,dimantions)
    
    cv2.imshow('vedio',fram)
   
    if k==ord('q'):
        break


cv2.destroyAllWindows()