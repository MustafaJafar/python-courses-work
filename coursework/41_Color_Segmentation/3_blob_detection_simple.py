# Standard imports
import cv2
import numpy as np;
 
# Read image
im = cv2.imread("images/th_global_blue.png", cv2.IMREAD_GRAYSCALE)


# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs
#im=cv2.bitwise_not(im) #we invert colors when detecting white blobs in black image
                        #as Its an opencv bug in the filter by color 
keypoints = detector.detect(im)
#im=cv2.bitwise_not(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im)
cv2.imwrite('images/th_global_blue_keypoints_simple.png',im_with_keypoints)
cv2.waitKey(0)