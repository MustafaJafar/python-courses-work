import cv2


face_cascade = cv2.CascadeClassifier('Files\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Files\\haarcascade_eye.xml')

img = cv2.imread('Files\\photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)

print (type(faces))
print("Faces Coordinates: x y w h \n",faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print("Eyes Coordinates: x y w h \n", eyes)
    for (ex,ey,ew,eh) in eyes: #draw box on eyes
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)



cv2.imshow("image" , img)
cv2.imwrite("Files\\news_result.jpg" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()