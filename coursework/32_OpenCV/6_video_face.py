import cv2 , time

face_cascade = cv2.CascadeClassifier('3_face_detector\\Files\\haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)
time.sleep(1)
while True : 
    check , frame = video.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 6)
    #print("Faces Coordinates: x y w h \n",faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("Capturing" , frame)
    key = cv2.waitKey(1)
    if key == ord('q') : 
        break


video.release()
cv2.destroyAllWindows()

