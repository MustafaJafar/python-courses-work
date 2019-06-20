# ref : 
# https://medium.com/podiihq/networking-how-to-communicate-between-two-python-programs-abd58b97390a

import socket
import json 
import select

timeout_in_seconds = 3 


def get_message() :
  message_raw = input("Enter 3 numbers separated by commas\n")
  print()
  values  = message_raw.split(",")
  keys = [ "a" , "b" , "c"]
  
  message_dict = dict(zip(keys, values))
  message = json.dumps(message_dict) 
  return message

def client():
  host = socket.gethostname()  # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()

  s.connect((host, port))
  
  s.setblocking(0)
  
  message = get_message()

  while message[7] != "q" :
    
    s.send(message.encode('utf-8'))
    
    data_ready = select.select([s], [], [], timeout_in_seconds )
    if data_ready[0] :
      data = s.recv(1024).decode('utf-8')
      print('Received from server: ' + data)
    else :
      print("server does not respond\n")
    
    message = get_message() 

  s.close()

if __name__ == '__main__' :
    client()