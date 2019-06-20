# ref : 
# https://medium.com/podiihq/networking-how-to-communicate-between-two-python-programs-abd58b97390a

import socket
import json 
import threading

def server():
  host = socket.gethostname()   # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()
  
  
  
  s.bind((host, port))
  print("Server has started")
  
  s.listen(1)

  print("Server is listening")
  
  client_socket, adress = s.accept()
  print("Connection from: " + str(adress))
  
  s.setblocking(0)

  while True: 

    #wait till client sends some data
    data = client_socket.recv(1024).decode('utf-8') #1024 is the max byte buffer size
    
    if not data:
      print ("connection has closed")
      break
    
    data = json.loads(data)
    
    print(data , type(data))
    
    #data = data.upper()
    #client_socket.send(data.encode('utf-8'))
    
    client_socket.send("1".encode('utf-8'))
  
  client_socket.close()

if __name__ == '__main__':
    t=threading.Thread(target= server)
    try:
      t.start()
    except:
      print ("Error: unable to start thread")
