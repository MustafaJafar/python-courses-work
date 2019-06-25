#https://www.learnopencv.com/blob-detection-using-opencv-python-c/

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
 

#----------------------

#code starts here : 

# Read image
im = cv2.imread("marks_simulation/marks_sim.png", cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)
 
# Detect blobs.
im=cv2.bitwise_not(im) 
keypoints = detector.detect(im)
im=cv2.bitwise_not(im)

# Draw detected blobs as red circles.
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

new_im = im_with_keypoints.copy()

xylist = list(range(0 , len(keypoints)))

#type each blob number
for i in range (0 , len(keypoints) ) : 
        xylist[i] = (int(keypoints[i].pt[0]) ,  int(keypoints[i].pt[1]))

        cv2.putText(im_with_keypoints,str(i + 1) , 
                (int(keypoints[i].pt[0]),int(keypoints[i].pt[1])), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1,
                (0,255,0), 2)

print(xylist)

#Srot Keypoints : I sorted manually on paper to test the algorithm 
sorted_keypoints = sort_xy_list(xylist)

for i in range (0 , len(sorted_keypoints) ) : 
    cv2.putText(new_im,str(i + 1) , 
        (sorted_keypoints[i][0],sorted_keypoints[i][1]), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1,
        (0,255,0), 2)


# Show keypoints
cv2.imshow("im_with_keypoints", im_with_keypoints)
cv2.imshow("new_im", new_im)

#cv2.imwrite('marks_simulation/marks_sim_keypoints.png',im_with_keypoints)
#cv2.imwrite('marks_simulation/marks_sim_keypoints_arranged.png',new_im)

cv2.waitKey(0)