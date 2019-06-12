import maya.cmds as cmds



cmds.polyCube(name = "cube")
#----------
cmds.getAttr("cube.translateX") #get attribute value .. use "objectname.attributename"
cmds.select("cube")				#you can use attribute short name
cmds.getAttr(".translate")

cmds.getAttr("cube.tX" , lock = True) #is the translate x locked ? 
cmds.getAttr("cube.tX" , keyable = True) #is the translate x keyable ? 
#----------
cmds.setAttr("cube.tx" ,10)
cmds.setAttr("cube.translate" , 5 , 4 , 3  , type = "double3") 
cmds.setAttr("cube.rotate" , 10 , 20 , 30  , type = "double3") 

cmds.setAttr("cube.tx" , lock = True) #lock translate X
cmds.setAttr("cube.tx" , lock = False) #unlock translate X

cmds.setAttr("cube.tx" , keyable = False) #translate X is now not keyable
cmds.setAttr("cube.tx" , keyable = True) #translate X is now keyable
#----------

cmds.ls() #returns a list of all objects in the scene
cmds.ls(transforms = True) #objects with transform nodes
cmds.ls(shapes = True) #objects with transform nodes
cmds.ls(cameras = True) #return shape nodes of cameras in scene

#example : set selected items visibilty to false
selection = cmds.ls(sl = True) #return selected objects
for sel in selection : 
	cmds.setAttr("{0}.v".format(sel) , False)

cmds.ls(sl = True , showType = True) #return selected objects each is followed by its type
#[u'pSphere1' , u'transform' , u'pCube1' ,u'transform']

'''
What are shapes in Maya ? 
each object has an un diplsyed child which is shape child
the actually is transform point in the viewport 
and the shape object is its mesh
'''

cmds.ls(type = "mesh") #return all objects that hs mesh types
			#which are the objects' shape nodes

cmds.ls(assemblies = True) #return top level nodes in the scene 
cmds.ls("presp")#return prespective camera
cmds.ls("p*") #return all objects that starts with p
cmds.ls("p*" , transform = True) 	#filter results to get transforms only 

#--------
#Diplay messages to users 
#import maya.cmds as cmds
import maya.OpenMaya as om

#Errors 
cmds.error("This is an error") #raise excption
om.MGlobal.displayError("This is a displayError")#code doesn't intrrupted

#Warnings
cmds.warning("this is an warning") #print warning message
om.MGlobal.displayWarning("This is a displayWarning") #no difference

#Info
print("this is an Info")
om.MGlobal.displayInfo("This is a displayInfo") #no difference

#Example 
sel = cmds.ls(sl = True)
num_sel = len (sel)
if num_sel >= 2 :
    for s in sel : 
	print (s)
elif num_sel ==1 : 
    om.MGlobal.displayError("Please select atleast two objects")
else:
    om.MGlobal.displayError("No Objects Selected")

#--------------
cmds.select("cone" , replace = True)
cmds.select("cone" , toggle = True) #used multi selection
cmds.select("cube" , add = True) #add cube to selection
cmds.select("cube" , deselect = True)
cmds.select(all = True) #without selecting default cameras
cmds.select(clear = True)#clear all selection

cmds.select(all = True) #select objects more than you think look at the commands window
cmds.ls(sl = True) #get a list of the selected objects
#----------
def maya_version() : 
    return cmds.about(version = True)

print(maya_version())
#---------
def create_sphere(name_ = "sphere" , tx=0,ty=0,tz=0 , sx = 1 , sy = 1 , sz =1):
    print("translate -> ({0},{1},{2})".format(tx,ty,tz)))
    print("scale -> ({0},{1},{2})".format(sx,sy,sz)))
    cmds.polySphere(name = name_ )
    cmds.setAttr(".translate" , tx , ty , tz  , type = "double3")     
    cmds.setAttr(".scale" , sx , sy , sz  , type = "double3") 