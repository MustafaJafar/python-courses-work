#https://forums.autodesk.com/t5/motionbuilder-forum/how-to-get-a-function-to-update-on-every-frame/td-p/4150440

'''I am explaining this so that in futer I can make my own implementation
The main idea : is to get the cursoe on the animation time line 
define start , end , current positions 
when cursor moves that a fram 
also you can change animation settings before making any thing 
    so that you make sure how fast frames are displayed (e.g. 24fps)

what if you want to make it each second ? 
you can use python time module 
or 
maya timer : https://download.autodesk.com/us/maya/2011help/CommandsPython/timer.html
'''


startList =[]
frameList = []
FBPlayerControl().GotoEnd()  
endFrame = FBSystem&#40;&#41;.LocalTime
FBPlayerControl().GotoStart()  
startFrame = FBSystem&#40;&#41;.LocalTime
print "Start Frame: %s" ûTime.GetTimeString(startFrame) + " End Frame: %s" ûTime.GetTimeString(endFrame)

for each in range(int(FBTime.GetTimeString(startFrame))):
   startList.append(each)
for each in range(int(FBTime.GetTimeString(endFrame))):
   frameList.append(each)
for startnum in startList:    
   for endnum in frameList:
      if endnum == startnum:
         frameList.remove(endnum)
frameList.append(int(FBTime.GetTimeString(endFrame)))
print "Frame List = %s"  r;ameList

head = FBFindModelByName("Head")
for frame in frameList:
   FBPlayerControl().Goto(FBTime(0,0,0, frame))
   null = FBModelMarker("%s_Frame" êch)
   FBSystem&#40;&#41;.Scene.Evaluate()
   null.Show = True
   Trns = FBVector3d()
   head.GetVector(Trns, FBModelTransformationMatrix.kModelTranslation, True)
   null.SetVector(Trns, FBModelTransformationMatrix.kModelTranslation, True)
   FBSystem&#40;&#41;.Scene.Evaluate()