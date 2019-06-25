#https://www.learnopencv.com/blob-detection-using-opencv-python-c/
#https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

# Standard imports
import cv2
import numpy as np
 

def sort_xy_list(xylist) :
        #sort all small y 
        xylist = sorted(xylist , key=lambda x:x[1])
        #sort :4 small x 
        xylist[:4] = sorted(xylist[:4] , key=lambda x:x[0])
        #sort 4:6 small x 
        xylist[4:6] = sorted(xylist[4:6] , key=lambda x:x[0])
        #sort 6:8 small x 
        xylist[6:8] = sorted(xylist[6:8] , key=lambda x:x[0])
        #sort 8: small x 
        xylist[8:] = sorted(xylist[8:] , key=lambda x:x[0])
        #sort 9:11 small y 
        xylist[9:11] = sorted(xylist[9:11] , key=lambda x:x[1])
        
        return xylist

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10
params.maxThreshold = 300
 
# Filter by Area.
params.filterByArea = True
params.minArea = 10
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.80
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
 


#-------------------------------------

# Create a VideoCapture object
cap = cv2.VideoCapture("marks_simulation\marks_sim.mp4")

# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('marks_simulation\marks_sim_outpy_2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)
 
xylist = list(range(0 , 12))
xyoldlist = []

framenum = 0 

while(True):
        ret, frame = cap.read()
 
        if ret == True: 

                frame=cv2.bitwise_not(frame) 
                keypoints = detector.detect(frame)
                frame=cv2.bitwise_not(frame)

                frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                
                                
                for i in range (0 , len(keypoints) ) : 
                        xylist[i] = (int(keypoints[i].pt[0]) ,  int(keypoints[i].pt[1]))
                
                sorted_keypoints = sort_xy_list(xylist)


               

                for i in range(1 , len(xyoldlist)) : 
                        for j in range(0 , len(sorted_keypoints) ) : 
                                if (xyoldlist[i - 1][j] != xyoldlist[i][j]) :
                                        cv2.line(frame_with_keypoints, xyoldlist[i - 1][j] , xyoldlist[i][j], (0, 0, 255), int(i/5) + 4  )

                for i in range (0 , len(sorted_keypoints) ) : 
                        cv2.putText(frame_with_keypoints,str(i + 1) , 
                         (sorted_keypoints[i][0] - 10 ,sorted_keypoints[i][1] + 10), 
                         cv2.FONT_HERSHEY_SIMPLEX, 
                         1,
                         (255,0,0), 2)

                #Save Points History
                xyoldlist.append(sorted_keypoints.copy())
                if (len(xyoldlist) > 20) : 
                        xyoldlist.pop(0)


                # Write the frame into the file 'output.avi'
                out.write(frame_with_keypoints)
                
                # Display the resulting frame    
                cv2.imshow('frame_with_keypoints',frame_with_keypoints)
                
                # Press Q on keyboard to stop recording
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                
        # Break the loop
        else:
                break 
        
# When everything done, release the video capture and video write objects
cap.release()
out.release()

print (len(xyoldlist))

for xy in xyoldlist : 
        print (xy)

# Closes all the frames
cv2.destroyAllWindows() 
