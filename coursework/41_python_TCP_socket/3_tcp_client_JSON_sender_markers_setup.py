# ref : 
# https://medium.com/podiihq/networking-how-to-communicate-between-two-python-programs-abd58b97390a

import socket
import json 
import select

timeout_in_seconds = 3 


def get_message(flag) : 
  print()
  if flag == "z" : 
    values = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]   
  else : 
    values = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12)]
  '''
  keys = [ "leftouterbrow", "leftinnerbrow","rightinnerbrow", "rightouterbrow",
    "leftcheek", "rightcheek", "leftnose", "rightnose",
    "leftmouth", "upperlip", "rightmouth", "lowerlip" ]
  '''
  keys = ["lob" , "lib" , "rib" , "rob" ,
          "lc"  , "rc"  , "ln"  , "rn"  ,
          "ul"  , "lm"  , "rm"  , "ll"  ]
          
  message_dict = dict(zip(keys, values))
  message = json.dumps(message_dict) 
  return message

def client():
  host = socket.gethostname()  # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()

  s.connect((host, port))
  
  s.setblocking(0)
  

  flag = "z"
  message = get_message(flag) 
   

  while flag != "q" : 
    print(message)
    s.send(message.encode('utf-8'))
    data_ready = select.select([s], [], [], timeout_in_seconds )
    
    if data_ready[0] :
      data = s.recv(1024).decode('utf-8')
      print('Received from server: ' + data)
    else :
      print("server does not respond\n")
    
    flag = input("Enter q to exit , any to resend\n")
    message = get_message(flag) 
   
    
  s.close()

if __name__ == '__main__' :
    client()