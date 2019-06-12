#import maya.cmds as mc

#sample test , all these commands works with the current selected object!!!
#mc.polySphere()
#mc.select("pSphere1") #to select , pass its name as the first parameter
#mc.delete("pSphere1") #auto select and delete pSphere1

#ctrl + enter : excute 
#alt + ctrl + enter : excute current line

#change flags
#mc.polySphere(radius = 10 , name = "lala")
#mc.delete("lala")

#to know all the parameters (flags) of a command
#mc.help("polySphere")

#each command has 3 modes : create - query - edit 
#create is the default 
#mc.polySphere(radius = 10 , name = "lala") 
#mc.polySphere(query = True , radius = True )  # Result: 10.0 #
#mc.polySphere(edit = True , radius = 5 )

#get list of all objects
#mc.ls() 
#mc.ls(shapes = True)  # filter
#mc.ls(selection = True)#current selected object

#mc.select()
#mc.select(clear = True)
#mc.select("name" , add = True)
#mc.select("name" , replace = True)

