import vrep , time , sys , numpy as np , math
from  matplotlib import pyplot as plt
from tkinter import *

jointHandles=[-1,-1,-1,-1,-1,-1,-1]

vrep.simxFinish(-1) #just in case, close all opened connections

clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
print(clientID) # if 1, then we are connected.

if clientID!=-1:
    print ("Connected to remote API server")
else:
    print("Not connected to remote API server")
    sys.exit("Could not connect")

for i in range(0,7) :
    err_code,jointHandles[i]=vrep.simxGetObjectHandle(clientID , 'LBR_iiwa_7_R800_joint%s'%(i+1) , vrep.simx_opmode_blocking )

err_code,camera = vrep.simxGetObjectHandle(clientID,"Vision_sensor",vrep.simx_opmode_blocking)
err_code,resolution,image = vrep.simxGetVisionSensorImage(clientID,camera,0,vrep.simx_opmode_streaming)

fig = plt.gcf() #plt
fig.show()      #plt
fig.canvas.draw()#plt

#-----------------------
def move_J1(var1):
    vrep.simxSetJointTargetPosition(clientID,jointHandles[0],(float(var1) * math.pi / 180),vrep.simx_opmode_blocking)
    

def move_J2(var2):
    vrep.simxSetJointTargetPosition(clientID,jointHandles[1],(float(var2) * math.pi / 180),vrep.simx_opmode_blocking)
    

def move_J3(var3):
    vrep.simxSetJointTargetPosition(clientID,jointHandles[2],(float(var3) * math.pi / 180),vrep.simx_opmode_blocking)

def move_J4(var4):
    vrep.simxSetJointTargetPosition(clientID,jointHandles[3],(float(var4) * math.pi / 180),vrep.simx_opmode_blocking)

def move_J5(var5):
    vrep.simxSetJointTargetPosition(clientID,jointHandles[4],(float(var5) * math.pi / 180),vrep.simx_opmode_blocking)

def move_J6(var6):
    vrep.simxSetJointTargetPosition(clientID,jointHandles[5],(float(var6) * math.pi / 180),vrep.simx_opmode_blocking)

def move_J7(var7):
    vrep.simxSetJointTargetPosition(clientID,jointHandles[6],(float(var7) * math.pi / 180),vrep.simx_opmode_blocking)

def get_frame(): 
    err_code,resolution,image = vrep.simxGetVisionSensorImage(clientID,camera,0,vrep.simx_opmode_buffer)
    img = np.array(image, dtype = np.uint8)
    img.resize([resolution[0],resolution[1],3])
    plt.imshow(img,origin="lower")#the image is upside down.#plt
    fig.canvas.draw() #plt

def program_exit():
    vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)
    plt.close('all')
    print("Done")
    window.destroy()

#create window 
window = Tk()

#create frames 
lframe = Frame(window)
lframe.pack( side = LEFT )#anchor=CENTER)

rframe = Frame(window)
rframe.pack( side = RIGHT )#anchor=CENTER)


var1 = DoubleVar()
scale1 = Scale( lframe,from_=-180, to=180 , variable = var1 , command = move_J1 )
scale1.set(0)
scale1.grid(row = 0 , column = 0 ) 

var2 = DoubleVar()
scale2 = Scale( lframe,from_=-180, to=180 , variable = var2 , command = move_J2 )
scale2.set(0)
scale2.grid(row = 0 , column = 1 ) 

var3 = DoubleVar()
scale3 = Scale( lframe,from_=-180, to=180 , variable = var3 , command = move_J3 )
scale3.set(0)
scale3.grid(row = 0 , column = 2 ) 

var4 = DoubleVar()
scale4 = Scale( lframe,from_=-180, to=180 , variable = var4 , command = move_J4 )
scale4.set(0)
scale4.grid(row = 0 , column = 3 )

var5 = DoubleVar()
scale5 = Scale( lframe,from_=-180, to=180 , variable = var5 , command = move_J5 )
scale5.set(0)
scale5.grid(row = 0 , column = 4 ) 

var6 = DoubleVar()
scale6 = Scale( lframe,from_=-180, to=180 , variable = var6 , command = move_J6 )
scale6.set(0)
scale6.grid(row = 0 , column = 5 )

var7 = DoubleVar    ()
scale7 = Scale( lframe,from_=-180, to=180 , variable = var7 , command = move_J7 )
scale7.set(0)
scale7.grid(row = 0 , column = 6 )

#--------------------Labels
label1 = Label(lframe , text="       J1")
label1.grid(row = 1 , column = 0 ) 

label2 = Label(lframe , text="       J2")
label2.grid(row = 1 , column = 1 ) 

label3 = Label(lframe , text="       J3")
label3.grid(row = 1 , column = 2 ) 

label4 = Label(lframe , text="       J4")
label4.grid(row = 1 , column = 3 ) 

label5 = Label(lframe , text="       J5")
label5.grid(row = 1 , column = 4 ) 

label6 = Label(lframe , text="       J6")
label6.grid(row = 1 , column = 5 ) 

label7 = Label(lframe , text="       J7")
label7.grid(row = 1 , column = 6 ) 

#---------------------buttons 
b1=Button(rframe,text="Close", width=12,command=program_exit)
b1.grid(row=0,column=0)

b2=Button(rframe,text="Show Camera", width=12,command=get_frame)
b2.grid(row=1,column=0)








window.mainloop()
