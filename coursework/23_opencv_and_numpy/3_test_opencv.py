import cv2
im_g = cv2.imread("smallgray.png",0) #0 == gray scale , 1 == BGR
print(im_g,"\n")

im_g = cv2.imread("smallgray.png",1)
print(im_g,"\n")

cv2.imwrite("new_smallgray.png" , im_g)