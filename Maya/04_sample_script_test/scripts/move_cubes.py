import maya.cmds as cmds 
import maya.OpenMaya as om


sel = cmds.select("row*") #select all objects starts with raw
sel = cmds.ls(sl = True)  #get selected objects
print(sel)

children = cmds.listRelatives(sel , children = True)
print(children)

frame = cmds.currentTime(query = True) #get current frame
print(frame)

if sel : #name objects unique names !
    for child in children :
        attr = "{0}.ty".format(child) #transform y of the child
        print(attr)
        if child.startswith("left"):
            cmds.setAttr(attr , frame)
        elif child.startswith("right"):
            cmds.setAttr(attr , -frame)
else : 
    om.MGlobal.displayError("No objects selected")
