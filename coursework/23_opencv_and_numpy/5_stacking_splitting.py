import cv2 
import numpy

im_g = cv2.imread("smallgray.png",0) #0 == gray scale , 1 == BGR

#stacking
ims = numpy.hstack((im_g , im_g)) #stack == putting images side by side
                                  #hstack (h == horizontal) takes 1 prameter so we passing 
                                  #the prameter as a tuple (img , img)

print(ims , "\n")

ims = numpy.vstack((im_g , im_g, im_g))
print(ims , "\n")

#splitting 
lst = numpy.hsplit(ims,5) #number of columns should be 
print(lst , "\n")         #divisable by the paramter given 

lst = numpy.vsplit(ims,3) #number of columns should be 
print(lst , "\n")         #divisable by the paramter given 
