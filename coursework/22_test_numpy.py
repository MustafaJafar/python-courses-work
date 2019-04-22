import numpy as np 

n = np.arange(27)    #1D
print(n , "\n")

n2 = n.reshape(3,9)  #2D
print(n2 , "\n")
 
n3 = n.reshape(3,3,3)#3D
print(n3 , "\n")

mylist = [[1,2,3],[4,5,6],[7,8,9]]

m = np.asarray(mylist)
print(m , "\n  " , type(m) , "\n")