#https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/

#Color explorer : http://colorizer.org/

import cv2
import numpy as np
import matplotlib.pyplot as plt


for i in range(6):
    #read image and convert to HSV 
    nemo_BGR = cv2.imread('images2/'+ str(i) +'.jpg')
    nemo_RGB = cv2.cvtColor(nemo_BGR, cv2.COLOR_BGR2RGB)
    nemo_HSV = cv2.cvtColor(nemo_RGB, cv2.COLOR_RGB2HSV)

    # Range for orange
    lower = np.array([1,190,200])
    upper = np.array([18,255,255])
    mask1 = cv2.inRange(nemo_HSV, lower, upper)
    

    # Range for white
    lower = np.array([0,0,200])
    upper = np.array([145,60,255])
    mask2 = cv2.inRange(nemo_HSV,lower,upper)
    
    # Generating the final mask to detect red color
    mask1 = mask1+mask2

    mask1 = cv2.morphologyEx(mask1 , cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1 , cv2.MORPH_DILATE, np.ones((3,3),np.uint8))


    #Segmenting the cloth out of the frame using bitwise and with the inverted mask
    res = cv2.bitwise_and(nemo_BGR,nemo_BGR,mask=mask1)

    
    
    #Generating the final output
    #plt.figure()
    #plt.imshow(res)
    #plt.savefig('images2/'+ str(i) +'_result_2.jpg')
    cv2.imwrite('images2/'+ str(i) +'_result_2.jpg' ,res)

#plt.show()

