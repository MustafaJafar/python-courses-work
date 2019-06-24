#https://docs.opencv.org/3.4.3/d7/d4d/tutorial_py_thresholding.html
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

import cv2 
import numpy as np
from matplotlib import pyplot as plt


#Get the image : 
org_img = cv2.imread("images/candy2.png" , 1)

#Separate imge into 3 planes 
blue,green,red = cv2.split(org_img)
gray_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)


#Merge colors back into 1 image 
new_img = cv2.merge((blue , green , red ))


#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

th1 = [0,0,0]
th2 = [0,0,0]
th2 = [0,0,0]
th3 = [0,0,0]
th4 = [0,0,0]
th5 = [0,0,0]

th = [th1 , th2 , th3 , th4 , th5]

for index , values, color , ths_value in zip(range(3),(red, green, blue), ('red', 'green', 'blue') , (75 , 45 , 127)) :
    
    img = cv2.GaussianBlur(values,(5,5),0)

    ret,th1[index] = cv2.threshold(img,ths_value,255,cv2.THRESH_BINARY)
    th1[index] = cv2.morphologyEx(th1[index], cv2.MORPH_CLOSE, kernel) 
    #th1 = cv2.dilate(th1 ,kernel,iterations = 1)

    th2[index] = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th2[index] = cv2.morphologyEx(th2[index], cv2.MORPH_OPEN, kernel)

    th3[index] = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    th3[index] = cv2.morphologyEx(th3[index], cv2.MORPH_OPEN, kernel)

    # Otsu's thresholding
    ret4,th4[index] = cv2.threshold(values,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # Otsu's thresholding after Gaussian blur
    blur = cv2.GaussianBlur(values,(5,5),0)
    ret5,th5[index] = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    titles = ['Original ' + color + ' Image' , 'Global Thresholding (v = ' + str(ths_value) +')', 'Adaptive Mean Thresholding',
                 'Adaptive Gaussian Thresholding' , "Otsu's Thresholding" ,"Otsu's Thresholding after blur" ]
    images = [values, th1[index], th2[index], th3[index] , th4[index] , th5[index]]   

    plt.figure(figsize=(8,9))
    
    #cv2.imwrite('th_global_' + color + '.png',th1[index])

    for i in range(6):
        plt.subplot(3,2, i + 1),plt.imshow(images[i],'gray')
        plt.subplots_adjust(hspace=0.32 , left = 0.09 , wspace = 0.51)
        plt.margins(0)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
        

    plt.savefig('images/thr_'+ color +'.png')


images[0] = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)     

for i in range(5) : 
    images[i+1] = cv2.merge((th[i][0] , th[i][1] , th[i][2]))

titles = ['Original Image' , 'Global Thresholding (indvidual v per channel)', 'Adaptive Mean Thresholding',
                 'Adaptive Gaussian Thresholding' , "Otsu's Thresholding" ,"Otsu's Thresholding after blur" ]

plt.figure(figsize=(8,9))
for i in range(6):
        plt.subplot(3,2, i + 1),plt.imshow(images[i],'gray')
        plt.subplots_adjust(hspace=0.32 , left = 0.09 , wspace = 0.51)
        plt.margins(1)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

plt.savefig('images/thr_base_color.png')


for i in range(5) : 
        '''
        temp  = cv2.absdiff(th[i][0] , th[i][1])
        temp  = cv2.absdiff(temp , th[i][2])
        images[i+1] = temp  
        '''
        th[i][0] = abs(th[i][0] - 255)
        th[i][1] = abs(th[i][1] - 255)
        th[i][2] = abs(th[i][2] - 255)
    
        temp = cv2.add(th[i][0],th[i][1])
        images[i+1] = cv2.add(temp , th[i][2])
    
        images[i+1] = (images[i+1] + 255) % 256
    
    

plt.figure(figsize=(8,9))
for i in range(6):
        plt.subplot(3,2, i + 1),plt.imshow(images[i],'gray')
        plt.subplots_adjust(hspace=0.32 , left = 0.09 , wspace = 0.51)
        plt.margins(1)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

plt.savefig('images/thr_base_color_BW.png')


blur = cv2.GaussianBlur(gray_img,(5,5),0)

ths_value = 115

ret,t1 = cv2.threshold(gray_img,ths_value,255,cv2.THRESH_BINARY)
t1 = cv2.morphologyEx(t1, cv2.MORPH_CLOSE, kernel) 
#th1 = cv2.dilate(th1 ,kernel,iterations = 1)

t2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
t2 = cv2.morphologyEx(t2, cv2.MORPH_OPEN, kernel)

t3 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
t3 = cv2.morphologyEx(t3, cv2.MORPH_OPEN, kernel)

# Otsu's thresholding
ret4,t4 = cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian blur
ret5,t5 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['Original Gray Image' , 'Global Thresholding (v = ' + str(ths_value) +')', 'Adaptive Mean Thresholding',
               'Adaptive Gaussian Thresholding' , "Otsu's Thresholding" ,"Otsu's Thresholding after blur" ]

images = [gray_img, t1, t2, t3, t4, t5]   


plt.figure(figsize=(8,9))
for i in range(6):
        plt.subplot(3,2, i + 1),plt.imshow(images[i],'gray')
        plt.subplots_adjust(hspace=0.32 , left = 0.09 , wspace = 0.51)
        plt.margins(1)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

plt.savefig('images/thr_Gray_color.png')



plt.show()
