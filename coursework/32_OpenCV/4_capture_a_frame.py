import cv2 , time

video = cv2.VideoCapture(0)

#boolean and video frame
check , frame = video.read()

print(check)
#print(frame)

gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(gray)

b, g, r = cv2.split(frame)
red = cv2.equalizeHist(r)
green = cv2.equalizeHist(g)
blue = cv2.equalizeHist(b)
frame_equ = cv2.merge((blue, green, red))

time.sleep(3)
cv2.imshow("Capturing" , equ)
cv2.imwrite("4\\image_RGB.jpg" , frame)
cv2.imwrite("4\\image_RGB_equlized.jpg" ,frame_equ )
cv2.imwrite("4\\image_gray.jpg" , gray)
cv2.imwrite("4\\image_gray_equalized.jpg" , equ)


cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()

