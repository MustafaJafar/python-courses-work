import cv2 
import os 

photos_list = os.listdir("2_practice")

for photo in photos_list : 
    img = cv2.imread(r"2_practice/" + photo  , 1)
    print(img.shape)
    resized_img = cv2.resize(img ,(int(img.shape[1]/2) , int(img.shape[0]/2)) )
    cv2.imshow(photo[:-4] , resized_img)
    cv2.imwrite(r"2_practice/" + photo[:-4] + "_resized.jpg", resized_img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()