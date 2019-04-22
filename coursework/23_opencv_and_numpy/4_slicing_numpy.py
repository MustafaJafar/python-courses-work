import cv2

#slicing a list : 
a = [1,2,3]
print(a[0:2] , "\n")

im_g = cv2.imread("smallgray.png",0) #0 == gray scale , 1 == BGR
print("image Shape : \n" , im_g.shape , "\n")

print(im_g,"\n")

#slicing in numpy
print(im_g[0:2] , "\n")
print(im_g[0:2 , 2:4] , "\n")
print(im_g[0 , 0] , "\n")

#iterating :
for i in im_g : # i represents a row 
    print(i) 
print()
for i in im_g.T : # i represents a column
    print(i)
print()
for i in im_g.flat : # i represents elements
    print(i) 