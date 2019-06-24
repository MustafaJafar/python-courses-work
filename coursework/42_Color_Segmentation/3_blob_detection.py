#https://www.learnopencv.com/blob-detection-using-opencv-python-c/

# Standard imports
import cv2
import numpy as np
 
# Read image
im = cv2.imread("images/th_global_blue.png", cv2.IMREAD_GRAYSCALE)
 
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
 

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)
 
# Detect blobs.
#im=cv2.bitwise_not(im) #we invert colors when detecting white blobs in black image
                        #as Its an opencv bug in the filter by color 
keypoints = detector.detect(im)
#im=cv2.bitwise_not(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


print (len(keypoints))
# Show keypoints
cv2.imshow("im_with_keypoints", im_with_keypoints)
cv2.imwrite('images/th_global_blue_keypoints.png',im_with_keypoints)

cv2.waitKey(0)