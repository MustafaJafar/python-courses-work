#https://realpython.com/python-opencv-color-spaces/


#Color explorer : http://colorizer.org/

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import hsv_to_rgb

'''
segmenting one clownfish with particular lighting and background 
may not necessarily generalize well to segmenting all clownfish.
'''

def create_RGB_plot(img) : #this is not working 
    r, g, b = cv2.split(img)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    
    pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors= pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")

def create_HSV_plot(img_hsv): #this is not working 
    h, s, v = cv2.split(img_hsv)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    
    pixel_colors = img_hsv.reshape((np.shape(img_hsv)[0]*np.shape(img_hsv)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors= pixel_colors , marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")

def display_colors (color1 , color2 ) : 
    lo_square = np.full((10, 10, 3), color1, dtype=np.uint8) / 255.0
    do_square = np.full((10, 10, 3), color2, dtype=np.uint8) / 255.0
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(hsv_to_rgb(do_square))
    plt.subplot(1, 2, 2)
    plt.imshow(hsv_to_rgb(lo_square))
    plt.show()

for i in range(6):
    #read image and convert to HSV 
    nemo_BGR = cv2.imread('images2/'+ str(i) +'.jpg')
    nemo_RGB = cv2.cvtColor(nemo_BGR, cv2.COLOR_BGR2RGB)
    nemo_HSV = cv2.cvtColor(nemo_RGB, cv2.COLOR_RGB2HSV)


    #plt.imshow(nemo_RGB)

    #create_RGB_plot(nemo_RGB)
    #create_HSV_plot(nemo_HSV)

    #Pick Range 
    light_orange = (1, 190, 200)
    dark_orange = (18, 255, 255)

    #display_colors(light_orange , dark_orange)

    mask = cv2.inRange(nemo_HSV , light_orange, dark_orange)
    result = cv2.bitwise_and(nemo_RGB, nemo_RGB, mask=mask)

    plt.figure(figsize=(8,9))
    
    plt.subplot(3, 2, 1)
    plt.imshow(mask, cmap="gray")
    plt.title("BW after orange Mask")
    plt.xticks([]),plt.yticks([])

    plt.subplot(3, 2, 2)
    plt.imshow(result)
    plt.title("RGB after orange Mask")
    plt.xticks([]),plt.yticks([])

    light_white = (0, 0, 200)
    dark_white = (145, 60, 255)

    mask_white = cv2.inRange(nemo_HSV, light_white, dark_white)
    result_white = cv2.bitwise_and(nemo_RGB, nemo_RGB, mask=mask_white)

    plt.subplot(3, 2, 3)
    plt.imshow(mask_white, cmap="gray")
    plt.title("BW after white Mask")
    plt.xticks([]),plt.yticks([])

    plt.subplot(3, 2, 4)
    plt.imshow(result_white)
    plt.title("RGB after white Mask")
    plt.xticks([]),plt.yticks([])

    final_mask = mask + mask_white
    
    final_result = cv2.bitwise_and(nemo_RGB , nemo_RGB, mask=final_mask)
    #final_result = cv2.GaussianBlur(final_result,(5,5),0)
    
    
    plt.subplot(3, 2, 5)
    plt.imshow(final_mask, cmap="gray")
    plt.title("BW final result")
    plt.xticks([]),plt.yticks([])
    
    plt.subplot(3, 2, 6)
    plt.imshow(final_result)
    plt.title("RGB final result")
    plt.xticks([]),plt.yticks([])
    
    plt.savefig('images2/further display/'+ str(i) +'_result_1.jpg')
    #cv2.imwrite('images2/'+ str(i) +'_result_1.jpg' ,final_result)


plt.show()
