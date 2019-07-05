# ref : 
# https://medium.com/podiihq/networking-how-to-communicate-between-two-python-programs-abd58b97390a
# https://stackoverflow.com/questions/29382456/maya-threading-causing-crash
# Excute functions in main thread : 
# https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2015/ENU/Maya/files/Python-Python-and-threading-htm.html
'''
from maya.utils import executeInMainThreadWithResult 
import maya.cmds
def doSphere( radius ):
	maya.cmds.sphere( radius=radius )
maya.utils.executeInMainThreadWithResult( doSphere, 5.0 )

'''


import socket
import json 
import threading
import maya.cmds as cmds 
from maya.utils import executeInMainThreadWithResult 

#every thing were working fine 
#till frames two line of code were added 
#python code recevied : server doesn't respond 
#solution : excute in main Maya's thread

def trans_cmds(data):
  modifier = 1.4
  frame = cmds.currentTime( query = True )
  print (frame)
  
  for key, value in data.items():  
    cmds.setAttr("%s.translate" % key , value[0] , value[1]  , 0  , type = "double3")
    cmds.setKeyframe(key , breakdown = False , hierarchy = "none" , controlPoints = False , shape = False )
    cmds.setKeyframe(key)

    cmds.move( value[0], value[1], 0, key ) 
    print(key , value[0],value[1])
  cmds.refresh()
  #update frame to be used in the next call
  frame += 1  
  cmds.currentTime(frame , edit = True  )  
  #return the current frame number
  return (frame-1) 

def server():
  host = socket.gethostname()   # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()
  
  s.bind((host, port))
  print("Server has started")
  
  s.listen(1)

  print("Server is listening")
  
  client_socket, adress = s.accept()
  print("Connection from: " + str(adress) + "\n")

  #s.setblocking(0)

  while True: 

    #wait till client sends some data
    data = client_socket.recv(1024).decode('utf-8') #1024 is the max byte buffer size
    
    if not data:
      print ("connection has closed")
      break
    
    #print(data , type(data))
    
    data = json.loads(data)
    frame = executeInMainThreadWithResult( trans_cmds ,data )
    #print("%s , %s \n" % (data , type(data) ) )
    
    #data = data.upper()
    #client_socket.send(data.encode('utf-8'))
    
    client_socket.send(str(frame).encode('utf-8'))
  
  client_socket.close()

if __name__ == '__main__':
    cmds.currentTime(1 , edit = True  )
    t=threading.Thread(target= server)
    try:
      t.start()
    except:
      print ("Error: unable to start thread")
