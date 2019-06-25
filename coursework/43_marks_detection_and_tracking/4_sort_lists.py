import cv2
import numpy as np

xylist = [(473, 347), (399, 321), (547, 320), (473, 289),   
    (531, 252), (420, 252), (572, 225), (374, 218), 
    (588, 134), (496, 120), (360, 134), (443, 118)]

#xylist[:4] = sorted(xylist[:4])


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


print (xylist)

