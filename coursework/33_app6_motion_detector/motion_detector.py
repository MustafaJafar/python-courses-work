import cv2 , time , pandas
from datetime import datetime

#the main idea : 
    #1.capture a static frame
    #2.difference between new frames and that static frame 
    #3.threshold

first_frame = None 
status_list = [None , None]
times = []
df = pandas.DataFrame(columns = ["Start" , "End"])

video = cv2.VideoCapture(0) #camera selection , 0 : first cam , 1 : second cam , ...
time.sleep(1)

#read the first frame
check , frame = video.read()
gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(gray , (21,21) , 0)

while True : 
    check , frame = video.read()
    status = 0 
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray , (21,21) , 0)
    
    delta_frame = cv2.absdiff(first_frame , gray)
    thresh_frame = cv2.threshold(delta_frame , 30 , 255 , cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame , None , iterations = 2)

    (_,cnts,_)  = cv2.findContours(thresh_frame.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts :
        if cv2.contourArea(contour) < 10000 : #some threshold area
            continue
        status = 1 
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0 , 255 ,0) , 3)
    
    status_list.append(status) 
    status_list = status_list [-2:]

    if (status_list[-1] != status_list[-2] ):#or status_list[-1] == 1 ) : #if the last two items not the same
        print(status_list[-1] , status_list[-2])                                                                    #or the last item == 1
        times.append (datetime.now())                                       
    
    cv2.imshow("Gray Frame" , gray)
    cv2.imshow("Delta Frame" , delta_frame)
    cv2.imshow("Thresh Frame" , thresh_frame)
    cv2.imshow("Countour" , frame)

    key = cv2.waitKey(1)
    if key == ord('q') : 
        break

print(len(times))
print(status_list)
for i in range (0 , len(times) , 2) :
    try:
        df = df.append({"Start" : times[i] , "End" : times[i+1]} , ignore_index= True)
    except IndexError:
        pass
        #df = df.append({"Start" : times[i] , "End" : times[i]} , ignore_index= True)

df.to_csv("Times.csv")
print(df)
video.release()
cv2.destroyAllWindows()

