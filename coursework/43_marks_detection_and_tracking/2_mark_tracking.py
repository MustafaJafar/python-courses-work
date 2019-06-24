#https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/

#Color explorer : http://colorizer.org/

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import hsv_to_rgb


def segmentation(bgr):

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    # Range for white
    lower = np.array([0,0,200])
    upper = np.array([145, 60,255])
    
    mask1 = cv2.inRange(hsv,lower,upper)
        
    mask1 = cv2.morphologyEx(mask1 , cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1 , cv2.MORPH_DILATE, np.ones((3,3),np.uint8))


    #Segmenting the cloth out of the frame using bitwise and with the inverted mask
    res = cv2.bitwise_and(bgr,bgr,mask=mask1)

    return res 

def face_eye(bgr) :
    gray = cv2.cvtColor(bgr , cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray , (21,21) , 0)
 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for (x,y,w,h) in faces:
        #print(w*h)
        if((w * h)  >= 10000) :
            cv2.rectangle(BGR ,(x,y),(x+w,y+h),(255,0,0),2)
            #roi => area of interset
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = BGR[y:y+h, x:x+w]
            
            face = roi_color.copy() 
    
            eyes = eye_cascade.detectMultiScale(roi_gray)
            i = 0 
            eye =[0,0]

        if (len(eyes) > 0) : 
            for (ex,ey,ew,eh) in eyes: #draw box on eyes
                print (ew * eh)
                if ( 5000 >= (ew * eh)  >= 3500) :
                    eye[i] = roi_color[ey:ey+eh, ex:ex+ew]
                    cv2.rectangle(roi_color ,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    i += 1 

    return [face , eye]


def thresh(img,ths_value) : 
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray , (21,21) , 0)

    ret,thr = cv2.threshold(gray,ths_value , 255,cv2.THRESH_BINARY)
    #thr = cv2.morphologyEx(thr , cv2.MORPH_CLOSE, kernel) 

    #ret , thr = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    return thr

def blobs(img) :

    # Detect blobs.
    img=cv2.bitwise_not(img) #Its an opencv bug in the filter by color 
    keypoints = detector.detect(img)
    img=cv2.bitwise_not(img)  

    # Draw detected blobs as red circles.
    im_with_keypoints = cv2.drawKeypoints(img , keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    


    return keypoints , im_with_keypoints

#Haar cascades
face_cascade = cv2.CascadeClassifier(r'haar_files\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'haar_files\haarcascade_eye.xml')

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200
 
# Filter by Area.
params.filterByArea = True
params.minArea = 100
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.80
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
 
# Set up the detector with the parameters.
detector = cv2.SimpleBlobDetector_create(params)
    


#Code Stars from here : 

#reading image
#BGR = cv2.imread('images3/4.jpg')
#org_BGR = BGR.copy()
#HSV = cv2.cvtColor(BGR, cv2.COLOR_BGR2HSV)

video = cv2.VideoCapture(0) #camera selection , 0 : first cam , 1 : second cam , ...

while True :
    check , BGR = video.read()
    

    #face = face_eye(BGR) #out: [face , [left_eye , right_eye]]

    #segm = segmentation(face[0])
    segm = segmentation(BGR)
    
    thr = thresh(segm,200)
    #thr = segm


    keypoints , img_blob = blobs(thr)

    new_BGR = cv2.drawKeypoints(BGR, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        


    #display results : 

    images = [segm , thr , img_blob , new_BGR ]
    titles = ["face_segment" , "face_threshold"  , "face_blobs" , "final_result" ]

    for i in range(4) : 
        cv2.imshow(titles[i] , images[i] )
        #cv2.imwrite('images3/4_results/'+ str(i) + '_' + titles[i]+'.png' , images[i])
    
    key = cv2.waitKey(1)
    if key == ord('q') : 
        break

video.release()

cv2.destroyAllWindows()
