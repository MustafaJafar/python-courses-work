import maya.cmds as cmds 
from math import sin , cos , pi
import time

#Cone

def init():
    cmds.currentTime(1 , edit = True  )
    cmds.polyCube(name = "cube")
    cmds.setKeyframe("cube" , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )

def move_save(r , h, f ) :
    cmds.currentTime(f , edit = True  )
    move_frame(r , h) 
    cmds.setKeyframe("cube" , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )
    
def move_frame(r , h):
    z = r * cos(r * pi) 
    x = r * sin(r * pi)
    print (z ,x) 
    #print (r * 180  ,rr )
    cmds.setAttr("cube.translate" , x,h, z  , type = "double3") 
    cmds.setAttr("cube.rotate" ,  0 ,r * 180, 0 , type = "double3") 
    
raduis = 6

r = 0  # float (6 / 120) 
f = 1 
h = 0 

print(r)
print(f)

init()
while h <= 6  : 
    move_save(r , h, f)
    r += 0.4
    h += 0.2
    
    
    f = (f  + 5 )
    
    print(f)
    time.sleep(0.4)
    