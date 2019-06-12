import maya.cmds as cmds 


#create cube and adding key frame
frame = cmds.currentTime(1 , edit = True  )
cmds.polyCube(name = "cube")
cmds.setKeyframe("cube" , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )


frame = cmds.currentTime(20 , edit = True  )
cmds.setAttr("cube.translate" , 5 , 4 , 3  , type = "double3") 
cmds.setAttr("cube.rotate" , 10 , 20 , 30  , type = "double3") 
cmds.setKeyframe("cube" , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )


frame = cmds.currentTime(40 , edit = True  )
cmds.setAttr("cube.translate" , 8 , 10 , 5  , type = "double3") 
cmds.setAttr("cube.rotate" , 40 , 20 , 50  , type = "double3") 
cmds.setKeyframe("cube" , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )


frame = cmds.currentTime(60 , edit = True  )
cmds.setAttr("cube.translate" , 0 , 5 , 15  , type = "double3") 
cmds.setAttr("cube.rotate" , 30 , 10 , 90  , type = "double3") 
cmds.setKeyframe("cube" , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )



'''
#get current frame "cursoe position on timeline"
#frame = cmds.currentTime(query = True)

#move cursor to frame 1 on timeline
frame = cmds.currentTime(1 , edit = True  )

print(frame)

#move cursor to frame 50 on timeline
frame = cmds.currentTime(50 , edit = True  )

print(frame)

#move cursor to frame 90 on timeline
frame = cmds.currentTime(90 , edit = True  )

print(frame)

#same as pressing 's' in keyboard 
cmds.setKeyframe("pCube1" , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )




'''
'''
Two methods to set keys 
1 : cmds.keyframe ( 'name.attribute' , edit = True) 
cmds.keyframe('surface1.translateX',edit=True,index=(1,1),timeChange='1.5sec',valueChange=10.25)


2 : cmds.setKeyframe
myCone = cmds.cone()
cmds.setKeyframe( myCone[0], time=[0,5,10], attribute='translateX' , v=5 )
cmds.setKeyframe( myCone[0], t=[2,7,12], at='ty', v=10 )
cmds.setKeyframe( myCone[0], t=[4,9,14], at='tz', v=15 )
cmds.selectKey( t=[(5,5),(12,12),(4,4)] )
cmds.selectKey( animation='objects', add=True, t=(14,14) )
cmds.selectKey( t=[(5,5),(12,12),(4,4)] )
cmds.selectKey( animation='objects', add=True, t=(14,14) )

nodes = cmds.keyframe(myCone,query=True,name=True)

'''