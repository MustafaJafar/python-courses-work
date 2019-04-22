import cv2 

img = cv2.imread("1_galaxy.jpg" , 0)# 1 : color , 0 : BW , -1 : transparency

print (type(img))
print (img)
print(img.shape)
#new_size = map(lambda x: x/2, img.shape)
#new_size = [x/2 for x in img.shape]
new_size =  tuple(int(x/2) for x in reversed(img.shape))
print(new_size)
print((int(img.shape[1]/2) , int(img.shape[0]/2)))
print(img.ndim)

resized_img = cv2.resize(img ,new_size )
cv2.imshow("Galaxy" , resized_img)
cv2.imwrite("1_galaxy_resized.jpg" , resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()