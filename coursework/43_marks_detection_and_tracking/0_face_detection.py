'''
bool detect and show 
void reset 


void get data 
threshold r,g,b 

'''

import cv2 
import numpy as np
from matplotlib import pyplot as plt

#reading image
img = cv2.imread('images/0.jpg')

#transforming image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray , (21,21) , 0)




#this is a pretrained models used to detect face and eyes based on haar features
face_cascade = cv2.CascadeClassifier(r'haar_files\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'haar_files\haarcascade_eye.xml')

#detecting faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#draw box on face
for (x,y,w,h) in faces:
    cv2.rectangle(img ,(x,y),(x+w,y+h),(255,0,0),2)
    #roi => area of interset
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    face_region = img[y:y+h, x:x+w]

   
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes: #draw box on eyes
        print (ew * eh)
        #Area filteration
        if ( 7000 >= (ew * eh)  >= 4000) : 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)






#show image
cv2.imshow('original',img)


#save image
cv2.imwrite('images/0_face_detected.jpg',img)

cv2.waitKey(0)
#cv2.destroyAllWindows()(0)