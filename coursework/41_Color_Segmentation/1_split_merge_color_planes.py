import cv2 
import numpy as np

#Get the image : 
img = cv2.imread("images/candy2.PNG" , 1)

#Separate imge into 3 planes 
'''
red = img[:,:,2]
green = img[:,:,1]
blue = img[:,:,0]
'''

blue,green,red = cv2.split(img)

#show each color plane 
for values, color, channel in zip((red, green, blue), ('red', 'green', 'blue'), (2,1,0)):
    new_img = np.zeros((values.shape[0], values.shape[1], 3), dtype = values.dtype)    
    new_img[:,:,channel] = values

    #show image  
    cv2.imshow( color , values )

    #show image + change background to visualize color channel 
    cv2.imshow( color + "1", new_img ) 

#Merge colors back into 1 image 
new_img = cv2.merge((blue , green , red ))


cv2.imshow("image" , new_img )
cv2.waitKey(0)
cv2.destroyAllWindows()